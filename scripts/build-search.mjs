import { readFile, readdir, rm } from 'node:fs/promises';
import path from 'node:path';
import * as pagefind from 'pagefind';

const site = path.resolve(process.argv[2] ?? '_site');
const config = await readFile('_config.yml', 'utf8');
const stable = config.match(/^docs_path_prefix: "\/docs\/([^"/]+)"/m)?.[1];
if (!stable) throw new Error('docs_path_prefix missing from _config.yml');

async function* htmlFiles(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const name = path.join(directory, entry.name);
    if (entry.isDirectory() && !['pagefind', 'pagefind-fallback'].includes(entry.name)) yield* htmlFiles(name);
    else if (entry.isFile() && entry.name.endsWith('.html')) yield name;
  }
}

const entries = [];
for await (const file of htmlFiles(site)) {
  const relative = path.relative(site, file).split(path.sep).join('/');
  const pathname = relative.replace(/^en\//, '');
  const version = pathname.match(/^docs\/(dev|\d+\.\d+)\//)?.[1];
  const section = version ? 'docs' : pathname.startsWith('handbook/') ? 'handbook' : 'site';
  if (!version && !/^(?:index\.html|(?:handbook|news|integrations|garages|screenshots|privacy)\/|changelog\.html)/.test(pathname)) continue;
  const html = await readFile(file, 'utf8');
  if (html.includes('class="i18n-fallback"') || /<meta[^>]*http-equiv=["']?refresh/i.test(html)) continue;
  const main = html.match(/<main\b[^>]*>/i);
  if (!main) continue;
  const url = '/' + relative.replace(/index\.html$/, '');
  entries.push({ relative, html, main, url, version, section });
}

const nativeUrls = new Set(entries.map(entry => entry.url));
const renamedHandbook = new Map([
  ['battery', 'akku'], ['changes-from-scooteros', 'aenderungen'],
  ['getting-started', 'erste-schritte'], ['quick-start', 'schnellstart'],
  ['riding', 'fahren'], ['states', 'zustaende'], ['troubleshooting', 'fehlerbehebung'],
]);
const counterpartFor = (url) => {
  for (const [en, de] of renamedHandbook) {
    if (url === `/en/handbook/${en}.html`) return `/handbook/${de}.html`;
    if (url === `/handbook/${de}.html`) return `/en/handbook/${en}.html`;
  }
  return null;
};
const { index } = await pagefind.createIndex();
const { index: fallbackIndex } = await pagefind.createIndex();
let fallbacks = 0;
for (const entry of entries) {
  const { relative, html, main, url, version, section } = entry;
  const current = !version || version === stable;
  const markers = `<span hidden data-pagefind-filter="current:${current ? 'yes' : 'no'}"></span>`;
  const indexed = html.replace(main[0], main[0].replace(/>$/, ` data-pagefind-body data-pagefind-filter="section:${section}">${markers}`));
  const { errors } = await index.addHTMLFile({ url, content: indexed });
  if (errors.length) throw new Error(`${relative}: ${errors.join('; ')}`);

  const otherLang = relative.startsWith('en/') ? 'de' : 'en';
  const alternate = [...html.matchAll(/<link\b[^>]*rel="alternate"[^>]*hreflang="(en|de)"[^>]*href="([^"]+)"/g)]
    .find(match => match[1] === otherLang)?.[2];
  const counterpart = counterpartFor(url) ?? (alternate ? new URL(alternate, 'https://librescoot.org').pathname
    : otherLang === 'en' ? '/en' + url : url.replace(/^\/en/, ''));
  if (!nativeUrls.has(counterpart)) {
    const result = await fallbackIndex.addHTMLFile({ url, content: indexed });
    if (result.errors.length) throw new Error(`${relative}: ${result.errors.join('; ')}`);
    fallbacks++;
  }
}

const indexes = [[index, 'pagefind']];
if (fallbacks) indexes.push([fallbackIndex, 'pagefind-fallback']);
else await rm(path.join(site, 'pagefind-fallback'), { recursive: true, force: true });
for (const [name, output] of indexes) {
  const { errors } = await name.writeFiles({ outputPath: path.join(site, output) });
  if (errors.length) throw new Error(errors.join('; '));
}
await pagefind.close();
console.log(`Search: ${entries.length} site pages indexed (${fallbacks} without a translation)`);
