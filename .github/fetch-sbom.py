#!/usr/bin/env python3
"""Fetch the newest published MDB/DBC SPDX pair and summarize its build packages."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import urllib.request


API = 'https://api.github.com/repos/librescoot/librescoot/releases?per_page=100'
ASSET_PREFIX = 'https://github.com/librescoot/librescoot/releases/download/'


def packages_from_spdx(document):
    graph = document['@graph']
    index = {node.get('spdxId', node.get('@id')): node for node in graph}
    licenses = {}
    for node in graph:
        if node.get('relationshipType') == 'hasDeclaredLicense':
            expressions = [index[target]['simplelicensing_licenseExpression']
                           for target in node.get('to', [])
                           if 'simplelicensing_licenseExpression' in index.get(target, {})]
            licenses.setdefault(node['from'], set()).update(expressions)
    packages = {}
    for node in graph:
        if node.get('type') != 'software_Package' or node.get('software_primaryPurpose') != 'install':
            continue
        identifier = node.get('spdxId', node.get('@id'))
        name = node['name']
        version = node.get('software_packageVersion', '')
        expressions = sorted(licenses.get(identifier, []))
        package = {'name': name, 'version': version,
                   'license': ' AND '.join(f'({value})' for value in expressions) if expressions else 'NOASSERTION'}
        packages[(name, version, package['license'])] = package
    if not packages:
        raise ValueError('SPDX image document has no build packages')
    return sorted(packages.values(), key=lambda package: (package['name'], package['version'], package['license']))


def newest_complete_release(releases):
    for release in sorted(releases, key=lambda row: row['published_at'] or '', reverse=True):
        if release.get('draft'):
            continue
        tag = release['tag_name']
        assets = {asset['name']: asset for asset in release['assets']}
        names = {board: f'librescoot-unu-{board}-{tag}.spdx.json.gz' for board in ('mdb', 'dbc')}
        if all(name in assets for name in names.values()):
            return release, {board: assets[name] for board, name in names.items()}
    return None, {}


def download(url, authenticated=False):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'librescoot-license-page'}
    if authenticated and os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
        return response.read()


def fetch():
    releases = json.loads(download(API, authenticated=True))
    release, assets = newest_complete_release(releases)
    result = {'release': None, 'images': []}
    if release is None:
        return result
    result['release'] = {'tag': release['tag_name'], 'url': release['html_url'], 'published': release['published_at']}
    for board, asset in assets.items():
        url = asset['browser_download_url']
        if not url.startswith(ASSET_PREFIX):
            raise ValueError('Unexpected SPDX asset URL')
        compressed = download(url)
        digest = 'sha256:' + hashlib.sha256(compressed).hexdigest()
        if asset.get('digest') and asset['digest'] != digest:
            raise ValueError('SPDX download checksum mismatch: ' + asset['name'])
        document = json.loads(gzip.decompress(compressed))
        result['images'].append({'board': board.upper(), 'name': asset['name'], 'url': url,
                                 'sha256': digest.removeprefix('sha256:'),
                                 'packages': packages_from_spdx(document)})
    return result


def main():
    output = Path('_data/firmware_sbom.json')
    result = fetch()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(output)
    print('SPDX:', result['release']['tag'] if result['release'] else 'no published image SBOM pair yet')


if __name__ == '__main__':
    main()
