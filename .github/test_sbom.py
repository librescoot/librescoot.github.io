"""Offline checks for the SPDX license-page importer."""
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('fetch_sbom', ROOT / '.github/fetch-sbom.py')
IMPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMPORTER)


class SbomTests(unittest.TestCase):
    def test_license_relationships_versions_and_build_package_filter(self):
        document = {'@graph': [
            {'type': 'software_Package', 'spdxId': 'recipe', 'name': 'recipe',
             'software_primaryPurpose': 'specification'},
            {'type': 'software_Package', 'spdxId': 'source', 'name': 'source',
             'software_primaryPurpose': 'source'},
            {'type': 'software_Package', 'spdxId': 'package', 'name': 'example',
             'software_primaryPurpose': 'install', 'software_packageVersion': '1.2.3'},
            {'type': 'software_Package', 'spdxId': 'unknown', 'name': 'unknown',
             'software_primaryPurpose': 'install', 'software_packageVersion': '2.0'},
            {'type': 'simplelicensing_LicenseExpression', 'spdxId': 'license',
             'simplelicensing_licenseExpression': 'AGPL-3.0-only OR CC-BY-NC-SA-4.0'},
            {'type': 'Relationship', 'from': 'package', 'to': ['license'],
             'relationshipType': 'hasDeclaredLicense'},
        ]}
        result = IMPORTER.packages_from_spdx(document)
        self.assertEqual(result, [
            {'name': 'example', 'version': '1.2.3', 'license': '(AGPL-3.0-only OR CC-BY-NC-SA-4.0)'},
            {'name': 'unknown', 'version': '2.0', 'license': 'NOASSERTION'},
        ])

    def test_empty_package_list_is_rejected(self):
        with self.assertRaises(ValueError):
            IMPORTER.packages_from_spdx({'@graph': []})

    def test_newest_complete_published_pair(self):
        def release(tag, published, boards, draft=False):
            return {'tag_name': tag, 'published_at': published, 'draft': draft,
                    'assets': [{'name': f'librescoot-unu-{board}-{tag}.spdx.json.gz'} for board in boards]}
        older = release('nightly-old', '2026-10-24T01:00:00Z', ['mdb', 'dbc'])
        newest = release('nightly-new', '2026-10-25T01:00:00Z', ['mdb', 'dbc'])
        incomplete = release('nightly-partial', '2026-10-26T01:00:00Z', ['mdb'])
        draft = release('nightly-draft', '2026-10-27T01:00:00Z', ['mdb', 'dbc'], True)
        selected, assets = IMPORTER.newest_complete_release([older, draft, newest, incomplete])
        self.assertEqual(selected['tag_name'], newest['tag_name'])
        self.assertEqual(set(assets), {'mdb', 'dbc'})
        self.assertEqual(IMPORTER.newest_complete_release([incomplete, draft]), (None, {}))

    def test_component_inventory_has_unique_entries_and_noncommercial_alternatives(self):
        data = json.loads((ROOT / '_data/component_licenses.json').read_text())
        rows = [component for group in data['groups'] for component in group['components']]
        self.assertEqual(len({row['name'] for row in rows}), len(rows))
        self.assertGreater(len(rows), 50)
        by_name = {row['name']: row for row in rows}
        for name in ['pm-service', 'data-server', 'event-service', 'modem-service', 'librefsm', 'redis-ipc']:
            self.assertIn(' OR CC-BY-NC-SA-4.0', by_name[name]['licenseExpression'])
        for name in ['boot-animation', 'pn7150', 'installer']:
            self.assertEqual(by_name[name]['licenseExpression'], 'CC-BY-NC-SA-4.0')
        self.assertEqual(by_name['carplay-service']['licenseExpression'], 'MIT')
        self.assertEqual(by_name['unu-garages-data']['licenseExpression'], 'ODbL-1.0')
        self.assertNotIn('/home/', json.dumps(data))


if __name__ == '__main__':
    unittest.main()
