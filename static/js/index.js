window.HELP_IMPROVE_VIDEOJS = false;

// More Works Dropdown Functionality
function toggleMoreWorks() {
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');
    if (!dropdown || !button) return;
    
    if (dropdown.classList.contains('show')) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
    } else {
        dropdown.classList.add('show');
        button.classList.add('active');
    }
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const container = document.querySelector('.more-works-container');
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');
    
    if (container && dropdown && button && !container.contains(event.target)) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
    }
});

// Close dropdown on escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const dropdown = document.getElementById('moreWorksDropdown');
        const button = document.querySelector('.more-works-btn');
        if (!dropdown || !button) return;
        dropdown.classList.remove('show');
        button.classList.remove('active');
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

// Copy BibTeX to clipboard
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

// Scroll to top functionality
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Show/hide scroll to top button
window.addEventListener('scroll', function() {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (window.pageYOffset > 300) {
        scrollButton.classList.add('visible');
    } else {
        scrollButton.classList.remove('visible');
    }
});

// Auto-play videos when they enter the viewport; pause when they leave.
function setupViewportVideoAutoplay() {
    const videos = document.querySelectorAll('.auto-play-video');
    if (videos.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;
            if (entry.isIntersecting) {
                video.play().catch(e => {
                    console.log('Autoplay prevented:', e);
                });
            } else {
                video.pause();
            }
        });
    }, {
        threshold: 0.35
    });
    
    videos.forEach(video => {
        observer.observe(video);
    });
}

$(document).ready(function() {
    // Check for click events on the navbar burger icon

    var options = {
		slidesToScroll: 1,
		slidesToShow: 1,
		loop: true,
		infinite: true,
		autoplay: true,
		autoplaySpeed: 5000,
    }

	// Initialize all div with carousel class
    var carousels = bulmaCarousel.attach('.carousel', options);
	
    bulmaSlider.attach();
    
    setupViewportVideoAutoplay();

})
