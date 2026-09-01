(function() {
    var dialog = document.querySelector('.news-lightbox');
    if (!dialog) return;

    var image = dialog.querySelector('.news-lightbox-image');
    var caption = dialog.querySelector('.news-lightbox-caption');
    var close = dialog.querySelector('.news-lightbox-close');

    function closeDialog() {
        if (dialog.open) dialog.close();
    }

    document.querySelectorAll('.news-screenshot-button').forEach(function(button) {
        button.addEventListener('click', function() {
            var src = button.dataset.fullSrc;
            if (typeof dialog.showModal !== 'function') {
                window.location.href = src;
                return;
            }

            image.src = src;
            image.alt = button.dataset.alt || '';
            caption.textContent = button.dataset.caption || '';
            dialog.showModal();
        });
    });

    close.addEventListener('click', closeDialog);
    dialog.addEventListener('click', function(event) {
        if (event.target === dialog) closeDialog();
    });
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && dialog.open) {
            event.preventDefault();
            closeDialog();
        }
    });
    dialog.addEventListener('close', function() {
        image.removeAttribute('src');
        image.alt = '';
        caption.textContent = '';
    });
})();
