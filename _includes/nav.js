(function () {
    var nav = document.querySelector('.nav');
    if (!nav) return;

    var toggle = nav.querySelector('.nav-toggle');
    var menu = nav.querySelector('.nav-links');
    if (!toggle || !menu) return;

    /* Below this width the links live in a panel behind the hamburger and the
       dropdowns are tap-driven. Above it the panel does not exist and the
       dropdowns open on hover or focus, with no class involved. Keep in step
       with the max-width: 900px block in style.css. */
    var panelLayout = window.matchMedia('(max-width: 900px)');

    function setDropdown(item, open) {
        item.classList.toggle('is-open', open);
        var trigger = item.querySelector('.nav-dropdown-trigger');
        if (trigger) trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    function closeDropdowns() {
        Array.prototype.forEach.call(nav.querySelectorAll('.nav-dropdown'), function (item) {
            setDropdown(item, false);
        });
    }

    function setMenu(open) {
        menu.classList.toggle('nav-open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        if (!open) closeDropdowns();
    }

    function menuIsOpen() {
        return menu.classList.contains('nav-open');
    }

    toggle.addEventListener('click', function () {
        setMenu(!menuIsOpen());
    });

    Array.prototype.forEach.call(nav.querySelectorAll('.nav-dropdown'), function (item) {
        var trigger = item.querySelector('.nav-dropdown-trigger');
        if (!trigger) return;

        trigger.addEventListener('click', function () {
            if (!panelLayout.matches) return;
            var open = !item.classList.contains('is-open');
            closeDropdowns();
            setDropdown(item, open);
        });

        /* On the wide layout CSS opens the menu on hover and focus without
           asking us, so mirror that into aria-expanded rather than leaving it
           stuck on the markup's initial false. */
        function mirror(open) {
            return function (event) {
                if (panelLayout.matches) return;
                if (event.type === 'focusout' && item.contains(event.relatedTarget)) return;
                trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
            };
        }

        item.addEventListener('mouseenter', mirror(true));
        item.addEventListener('mouseleave', mirror(false));
        item.addEventListener('focusin', mirror(true));
        item.addEventListener('focusout', mirror(false));
    });

    /* Following a link closes the panel. Matters most for the in-page anchors,
       where nothing navigates and the panel would otherwise cover the target. */
    menu.addEventListener('click', function (event) {
        if (event.target.closest('a')) setMenu(false);
    });

    document.addEventListener('click', function (event) {
        if (nav.contains(event.target)) return;
        if (menuIsOpen()) setMenu(false);
        else closeDropdowns();
    });

    document.addEventListener('keydown', function (event) {
        if (event.key !== 'Escape') return;
        if (menuIsOpen()) {
            setMenu(false);
            toggle.focus();
            return;
        }
        closeDropdowns();
        /* The wide layout holds a dropdown open through :focus-within, so
           dropping focus is the only way to dismiss it. */
        if (document.activeElement && nav.contains(document.activeElement)) {
            document.activeElement.blur();
        }
    });

    panelLayout.addEventListener('change', function (event) {
        if (!event.matches) setMenu(false);
    });
})();
