(function() {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;

    function getTheme() {
        var stored = localStorage.getItem('theme');
        if (stored) return stored;
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    btn.addEventListener('click', function() {
        var current = getTheme();
        var next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
    });
})();
