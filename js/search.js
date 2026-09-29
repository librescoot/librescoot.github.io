const dialog = document.querySelector('#search-dialog');
const form = document.querySelector('#site-search');
const query = document.querySelector('#search-query');
const scope = document.querySelector('#search-scope');
const status = document.querySelector('#search-status');
const results = document.querySelector('#search-results');
const panel = document.querySelector('.search-results-panel');
const more = document.querySelector('#search-more');
let pagefind;
let searchReady;
let matches = [];
let shown = 0;
let sequence = 0;
let timer;

function openSearch(event) {
    event?.preventDefault();
    if (!dialog.open) dialog.showModal();
    query.focus();
}

function versionLabel(version) {
    return version === 'dev' ? 'dev' : `v${version}`;
}

function isFallback(url) {
    const english = new URL(url, location.origin).pathname.startsWith('/en/');
    return english !== (document.documentElement.lang === 'en');
}

function loadSearch() {
    searchReady ??= (async () => {
        pagefind = await import('/pagefind/pagefind.js');
        try {
            const response = await fetch('/pagefind-fallback/pagefind-entry.json');
            if (response.ok) {
                const { languages } = await response.json();
                const other = document.documentElement.lang === 'de' ? 'en' : 'de';
                if (languages[other]) await pagefind.mergeIndex('/pagefind-fallback/', { language: other });
            }
        } catch (error) {
            console.warn('Other-language search unavailable:', error);
        }
        return pagefind;
    })();
    return searchReady;
}

async function groupDocs(found) {
    const pages = await Promise.all(found.map(result => result.data()));
    const groups = new Map();
    for (const page of pages) {
        const match = page.url.match(/\/docs\/(dev|\d+\.\d+)\/(.*)/);
        if (!match) continue;
        const [, version, basePath] = match;
        if (!groups.has(basePath)) groups.set(basePath, []);
        groups.get(basePath).push({ page, version });
    }
    return [...groups.values()].map(variants => {
        variants.sort((a, b) => {
            if (a.version === dialog.dataset.stable) return -1;
            if (b.version === dialog.dataset.stable) return 1;
            if (a.version === 'dev') return 1;
            if (b.version === 'dev') return -1;
            return b.version.localeCompare(a.version, undefined, { numeric: true });
        });
        return { data: async () => variants[0].page, variants };
    });
}

async function showMore() {
    const current = sequence;
    const batch = matches.slice(shown, shown + 10);
    const pages = await Promise.all(batch.map(result => result.data()));
    if (current !== sequence) return;
    for (const [index, page] of pages.entries()) {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.className = 'search-result-title';
        link.href = page.url;
        link.textContent = page.meta.title || page.url;
        item.append(link);
        if (isFallback(page.url)) {
            const badge = document.createElement('span');
            badge.className = 'search-result-version';
            badge.textContent = dialog.dataset.fallback;
            item.append(badge);
        }
        if (!batch[index].variants) {
            const version = page.url.match(/\/docs\/(dev|\d+\.\d+)\//)?.[1];
            if (version) {
                const badge = document.createElement('span');
                badge.className = 'search-result-version';
                badge.textContent = versionLabel(version);
                link.append(badge);
            }
        }
        if (page.meta.description || page.plain_excerpt) {
            const excerpt = document.createElement('p');
            excerpt.textContent = page.meta.description || page.plain_excerpt;
            item.append(excerpt);
        }
        if (batch[index].variants) {
            const versions = document.createElement('div');
            versions.className = 'search-result-versions';
            for (const [position, variant] of batch[index].variants.entries()) {
                const chip = document.createElement(position ? 'a' : 'span');
                chip.textContent = versionLabel(variant.version);
                if (isFallback(variant.page.url)) {
                    chip.textContent += document.documentElement.lang === 'de' ? ' · EN' : ' · DE';
                    chip.title = dialog.dataset.fallback;
                }
                if (position) chip.href = variant.page.url;
                else chip.className = 'is-primary';
                versions.append(chip);
            }
            item.append(versions);
        }
        results.append(item);
    }
    shown += pages.length;
    more.hidden = shown >= matches.length;
}

async function search(event) {
    event?.preventDefault();
    clearTimeout(timer);
    ++sequence;
    matches = [];
    shown = 0;
    results.replaceChildren();
    more.hidden = true;
    const term = query.value.trim();
    panel.hidden = !term;
    if (!term) { status.textContent = ''; query.focus(); return; }
    const current = sequence;
    status.textContent = dialog.dataset.loading;
    try {
        await loadSearch();
        const filters = scope.value === 'all' ? { current: 'yes' }
            : { section: scope.value };
        const found = await pagefind.search(term, { filters });
        if (current !== sequence) return;
        matches = scope.value === 'docs' ? await groupDocs(found.results) : found.results;
        if (current !== sequence) return;
        status.textContent = matches.length ? `${matches.length} ${dialog.dataset.results}` : dialog.dataset.empty;
        await showMore();
    } catch (error) {
        if (current === sequence) status.textContent = dialog.dataset.error;
        console.error('Search failed:', error);
    }
}

function scheduleSearch() {
    clearTimeout(timer);
    ++sequence;
    results.replaceChildren();
    more.hidden = true;
    panel.hidden = !query.value.trim();
    status.textContent = query.value.trim() ? dialog.dataset.loading : '';
    if (query.value.trim()) timer = setTimeout(search, 200);
}

for (const opener of document.querySelectorAll('[data-search-open]')) opener.addEventListener('click', openSearch);
document.addEventListener('keydown', event => {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') openSearch(event);
});
document.querySelector('#search-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
dialog.addEventListener('keydown', event => {
    if (event.key !== 'ArrowDown' && event.key !== 'ArrowUp') return;
    const links = [...results.querySelectorAll('.search-result-title')];
    const row = document.activeElement.closest('#search-results li');
    const position = links.findIndex(link => link.closest('li') === row);
    if (!links.length || (document.activeElement !== query && position < 0)) return;
    event.preventDefault();
    const next = document.activeElement === query ? (event.key === 'ArrowDown' ? links[0] : links.at(-1))
        : event.key === 'ArrowUp' && position === 0 ? query
        : links[(position + (event.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length];
    next.focus();
    if (next !== query) next.scrollIntoView({ block: 'nearest' });
});
form.addEventListener('submit', search);
query.addEventListener('input', scheduleSearch);
scope.addEventListener('change', () => { if (query.value.trim()) search(); });
more.addEventListener('click', () => {
    showMore().catch(error => {
        status.textContent = dialog.dataset.error;
        console.error('Search failed:', error);
    });
});

if (/\/(?:en\/)?search\/$/.test(location.pathname)) {
    const initial = new URLSearchParams(location.search);
    query.value = initial.get('q') || '';
    if ([...scope.options].some(option => option.value === initial.get('in'))) scope.value = initial.get('in');
    openSearch();
    if (query.value) search();
}
