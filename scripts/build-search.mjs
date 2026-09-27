import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import * as pagefind from 'pagefind';

const site = path.resolve(process.argv[2] ?? '_site');
const config = await readFile('_config.yml', 'utf8');
const stable = config.match(/^docs_path_prefix: "\/docs\/([^"/]+)"/m)?.[1];
if (!stable) throw new Error('docs_path_prefix missing from _config.yml');

async function* htmlFiles(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const name = path.join(directory, entry.name);
    if (entry.isDirectory() && entry.name !== 'pagefind') yield* htmlFiles(name);
    else if (entry.isFile() && entry.name.endsWith('.html')) yield name;
  }
}

const { index } = await pagefind.createIndex();
let pages = 0;
for await (const file of htmlFiles(site)) {
  const relative = path.relative(site, file).split(path.sep).join('/');
  const pathname = relative.replace(/^en\//, '');
  const version = pathname.match(/^docs\/(dev|\d+\.\d+)\//)?.[1];
  const section = version ? 'docs' : pathname.startsWith('handbook/') ? 'handbook' : 'site';
  if (!version && !/^(?:index\.html|(?:handbook|news|integrations|garages|screenshots|privacy)\/|changelog\.html)/.test(pathname)) continue;
  const html = await readFile(file, 'utf8');
  if (html.includes('class="i18n-fallback"') || /<meta[^>]*http-equiv=["']?refresh/i.test(html)) continue;
  const current = !version || version === stable;
  const main = html.match(/<main\b[^>]*>/i);
  if (!main) continue;
  const markers = `<span hidden data-pagefind-filter="current:${current ? 'yes' : 'no'}"></span>`;
  const indexed = html.replace(main[0], main[0].replace(/>$/, ` data-pagefind-body data-pagefind-filter="section:${section}">${markers}`));
  const url = '/' + relative.replace(/index\.html$/, '');
  const { errors } = await index.addHTMLFile({ url, content: indexed });
  if (errors.length) throw new Error(`${relative}: ${errors.join('; ')}`);
  pages++;
}

const { errors } = await index.writeFiles({ outputPath: path.join(site, 'pagefind') });
if (errors.length) throw new Error(errors.join('; '));
await pagefind.close();
console.log(`Search: ${pages} site pages indexed`);
