function toggleMoreWorks() {
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');
    if (!dropdown || !button) return;

    const isOpen = dropdown.classList.toggle('show');
    button.classList.toggle('active', isOpen);
    button.setAttribute('aria-expanded', String(isOpen));
}

document.addEventListener('click', function(event) {
    const container = document.querySelector('.more-works-container');
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');

    if (container && dropdown && button && !container.contains(event.target)) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
        button.setAttribute('aria-expanded', 'false');
    }
});

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const dropdown = document.getElementById('moreWorksDropdown');
        const button = document.querySelector('.more-works-btn');
        if (!dropdown || !button) return;
        dropdown.classList.remove('show');
        button.classList.remove('active');
        button.setAttribute('aria-expanded', 'false');
    }
});

function copyUsingExecCommand(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.setAttribute('readonly', '');
    textArea.style.position = 'fixed';
    textArea.style.top = '0';
    textArea.style.left = '0';
    textArea.style.opacity = '0';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    textArea.setSelectionRange(0, textArea.value.length);
    const copied = document.execCommand('copy');
    document.body.removeChild(textArea);
    return copied;
}

function updateCopyFeedback(button, copyText, ok) {
    if (!button || !copyText) return;
    button.classList.remove('copy-pop');
    // Force reflow so repeated clicks replay the animation.
    void button.offsetWidth;
    button.classList.add('copy-pop');
    button.classList.toggle('copied', ok);
    copyText.textContent = ok ? 'Copied' : 'Failed';
    setTimeout(function() {
        button.classList.remove('copy-pop');
        button.classList.remove('copied');
        copyText.textContent = 'Copy';
    }, 1800);
}

function copyBibTeX() {
    const bibtexElement = document.getElementById('bibtex-code');
    const button = document.querySelector('.copy-bibtex-btn');
    const copyText = button ? button.querySelector('.copy-text') : null;
    if (!bibtexElement || !button || !copyText) return;

    const text = bibtexElement.innerText.trim();
    // Always try synchronous copy first to keep iOS/Safari user-gesture context.
    const copiedSync = copyUsingExecCommand(text);
    if (copiedSync) {
        updateCopyFeedback(button, copyText, true);
        return;
    }

    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(function() {
            updateCopyFeedback(button, copyText, true);
        }).catch(function(err) {
            console.warn('Clipboard API failed:', err);
            updateCopyFeedback(button, copyText, false);
        });
        return;
    }

    updateCopyFeedback(button, copyText, false);
}

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

window.addEventListener('scroll', function() {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (!scrollButton) return;
    if (window.pageYOffset > 300) {
        scrollButton.classList.add('visible');
    } else {
        scrollButton.classList.remove('visible');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const quickLinksButton = document.querySelector('.more-works-btn');
    const closeButton = document.querySelector('.close-btn');
    const scrollButton = document.querySelector('.scroll-to-top');
    const copyButton = document.querySelector('.copy-bibtex-btn');

    if (quickLinksButton) quickLinksButton.addEventListener('click', toggleMoreWorks);
    if (closeButton) closeButton.addEventListener('click', toggleMoreWorks);
    if (scrollButton) scrollButton.addEventListener('click', scrollToTop);
    if (copyButton) copyButton.addEventListener('click', copyBibTeX);
});
