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

// Copy BibTeX to clipboard
function copyBibTeX() {
    const bibtexElement = document.getElementById('bibtex-code');
    const button = document.querySelector('.copy-bibtex-btn');
    const copyText = button.querySelector('.copy-text');
    
    if (bibtexElement) {
        navigator.clipboard.writeText(bibtexElement.textContent).then(function() {
            // Success feedback
            button.classList.add('copied');
            copyText.textContent = 'Cop';
            
            setTimeout(function() {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        }).catch(function(err) {
            console.error('Failed to copy: ', err);
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = bibtexElement.textContent;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            
            button.classList.add('copied');
            copyText.textContent = 'Cop';
            setTimeout(function() {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        });
    }
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

function formatDisplayNumber(value) {
    return new Intl.NumberFormat('en-US').format(value);
}

function formatDateParam(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

function createLocalDate(dateLike) {
    const date = new Date(dateLike);
    return new Date(date.getFullYear(), date.getMonth(), date.getDate(), 12);
}

function daysBetween(startDate, endDate) {
    const start = createLocalDate(startDate);
    const end = createLocalDate(endDate);
    return Math.round((end - start) / 86400000);
}

function buildVisitSampleDates(startDate, endDate) {
    const spanDays = Math.max(daysBetween(startDate, endDate), 0);
    let stepDays = 1;

    if (spanDays > 540) {
        stepDays = 30;
    } else if (spanDays > 240) {
        stepDays = 14;
    } else if (spanDays > 90) {
        stepDays = 7;
    } else if (spanDays > 45) {
        stepDays = 3;
    }

    const dates = [];
    const cursor = createLocalDate(startDate);
    const last = createLocalDate(endDate);

    while (cursor <= last) {
        dates.push(new Date(cursor));
        cursor.setDate(cursor.getDate() + stepDays);
    }

    const finalLabel = formatDateParam(last);
    if (dates.length === 0 || formatDateParam(dates[dates.length - 1]) !== finalLabel) {
        dates.push(last);
    }

    return dates;
}

function parseCounterValue(value) {
    if (typeof value === 'number') return value;
    if (typeof value === 'string') {
        const normalized = value.replace(/[^\d.-]/g, '');
        return Number.parseInt(normalized || '0', 10);
    }
    return 0;
}

function niceCeil(value) {
    if (value <= 5) return 5;
    const exponent = 10 ** Math.floor(Math.log10(value));
    const fraction = value / exponent;
    let niceFraction = 10;

    if (fraction <= 1) niceFraction = 1;
    else if (fraction <= 2) niceFraction = 2;
    else if (fraction <= 5) niceFraction = 5;

    return niceFraction * exponent;
}

function buildTickIndices(length, maxTicks) {
    if (length <= 1) return [0];
    const ticks = new Set([0, length - 1]);
    const segments = Math.min(maxTicks - 1, length - 1);

    for (let index = 1; index < segments; index += 1) {
        ticks.add(Math.round((index * (length - 1)) / segments));
    }

    return Array.from(ticks).sort((a, b) => a - b);
}

async function fetchCumulativeVisitCount(siteCode, startDate, endDate) {
    const url = new URL(`https://${siteCode}.goatcounter.com/counter/TOTAL.json`);
    url.searchParams.set('start', startDate);
    url.searchParams.set('end', endDate);

    const response = await fetch(url.toString(), {
        headers: { 'Accept': 'application/json' }
    });

    if (!response.ok) {
        throw new Error(`GoatCounter request failed with status ${response.status}`);
    }

    const payload = await response.json();
    return parseCounterValue(payload.count);
}

async function fetchVisitSeries(siteCode, startDate, sampleDates) {
    const results = [];
    const batchSize = 6;

    for (let index = 0; index < sampleDates.length; index += batchSize) {
        const batch = sampleDates.slice(index, index + batchSize);
        const series = await Promise.all(batch.map(async (date) => ({
            date,
            count: await fetchCumulativeVisitCount(siteCode, startDate, formatDateParam(date))
        })));
        results.push(...series);
    }

    return results;
}

function renderVisitChart(svg, points) {
    const width = 960;
    const height = 360;
    const padding = { top: 28, right: 28, bottom: 52, left: 62 };
    const innerWidth = width - padding.left - padding.right;
    const innerHeight = height - padding.top - padding.bottom;
    const counts = points.map(point => point.count);
    const yMax = niceCeil(Math.max(...counts, 0));
    const baselineY = padding.top + innerHeight;
    const spanDays = Math.max(daysBetween(points[0].date, points[points.length - 1].date), 0);
    const dateFormatter = new Intl.DateTimeFormat('en-US', spanDays > 365
        ? { month: 'short', year: 'numeric' }
        : { month: 'short', day: 'numeric' });

    const xForIndex = (index) => {
        if (points.length === 1) return padding.left + innerWidth / 2;
        return padding.left + (index / (points.length - 1)) * innerWidth;
    };

    const yForValue = (value) => padding.top + innerHeight - (value / yMax) * innerHeight;
    const linePath = points.map((point, index) => `${index === 0 ? 'M' : 'L'} ${xForIndex(index).toFixed(2)} ${yForValue(point.count).toFixed(2)}`).join(' ');
    const areaPath = `${linePath} L ${xForIndex(points.length - 1).toFixed(2)} ${baselineY.toFixed(2)} L ${xForIndex(0).toFixed(2)} ${baselineY.toFixed(2)} Z`;
    const yTicks = 4;
    const xTickIndices = buildTickIndices(points.length, 5);
    const finalPoint = points[points.length - 1];
    const finalX = xForIndex(points.length - 1);
    const finalY = yForValue(finalPoint.count);
    const calloutWidth = 86;
    const calloutHeight = 34;
    const calloutX = Math.max(padding.left + 8, Math.min(finalX - calloutWidth / 2, width - padding.right - calloutWidth));
    const calloutY = Math.max(padding.top + 4, finalY - 48);

    let gridMarkup = '';
    for (let tick = 0; tick <= yTicks; tick += 1) {
        const value = (yMax / yTicks) * tick;
        const y = yForValue(value);
        gridMarkup += `
            <line class="chart-grid-line" x1="${padding.left}" y1="${y}" x2="${width - padding.right}" y2="${y}"></line>
            <text class="chart-axis-label" x="${padding.left - 12}" y="${y + 5}" text-anchor="end">${formatDisplayNumber(Math.round(value))}</text>
        `;
    }

    let xAxisMarkup = '';
    xTickIndices.forEach((tickIndex) => {
        const x = xForIndex(tickIndex);
        xAxisMarkup += `
            <line class="chart-tick-mark" x1="${x}" y1="${baselineY}" x2="${x}" y2="${baselineY + 6}"></line>
            <text class="chart-axis-label" x="${x}" y="${height - 14}" text-anchor="middle">${dateFormatter.format(points[tickIndex].date)}</text>
        `;
    });

    const pointMarkup = points.length <= 40
        ? points.map((point, index) => `<circle class="chart-point" cx="${xForIndex(index)}" cy="${yForValue(point.count)}" r="4.5"></circle>`).join('')
        : '';

    svg.innerHTML = `
        <title id="visit-chart-title">Cumulative page clicks</title>
        <desc id="visit-chart-desc">A cumulative line chart of project page clicks tracked by GoatCounter.</desc>
        <defs>
            <linearGradient id="visit-area-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#2563eb" stop-opacity="0.24"></stop>
                <stop offset="100%" stop-color="#0ea5e9" stop-opacity="0.03"></stop>
            </linearGradient>
            <filter id="visit-line-shadow" x="-10%" y="-10%" width="120%" height="140%">
                <feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#2563eb" flood-opacity="0.18"></feDropShadow>
            </filter>
        </defs>
        ${gridMarkup}
        <line class="chart-baseline" x1="${padding.left}" y1="${baselineY}" x2="${width - padding.right}" y2="${baselineY}"></line>
        ${xAxisMarkup}
        <path class="chart-area" d="${areaPath}"></path>
        <path class="chart-line" d="${linePath}" filter="url(#visit-line-shadow)"></path>
        ${pointMarkup}
        <circle class="chart-point-final" cx="${finalX}" cy="${finalY}" r="6.5"></circle>
        <rect class="chart-callout" x="${calloutX}" y="${calloutY}" rx="12" ry="12" width="${calloutWidth}" height="${calloutHeight}"></rect>
        <text class="chart-callout-text" x="${calloutX + calloutWidth / 2}" y="${calloutY + 22}" text-anchor="middle">${formatDisplayNumber(finalPoint.count)}</text>
    `;
}

async function setupVisitChart() {
    const section = document.getElementById('visits');
    const svg = document.getElementById('visit-chart');
    const loading = document.getElementById('visit-chart-loading');
    const empty = document.getElementById('visit-chart-empty');
    const total = document.getElementById('visit-total');
    const footnote = document.getElementById('visit-footnote');

    if (!section || !svg || !loading || !empty || !total || !footnote) return;

    const siteCode = section.dataset.goatcounterSite;
    const startDate = section.dataset.goatcounterStart;

    if (!siteCode || !startDate) return;

    const start = createLocalDate(startDate);
    const today = createLocalDate(new Date());

    if (start > today) {
        loading.hidden = true;
        empty.hidden = false;
        footnote.textContent = 'The tracking start date is later than today. Update the visit chart configuration in index.html.';
        return;
    }

    try {
        const sampleDates = buildVisitSampleDates(start, today);
        const points = await fetchVisitSeries(siteCode, formatDateParam(start), sampleDates);

        renderVisitChart(svg, points);
        total.textContent = formatDisplayNumber(points[points.length - 1].count);
        footnote.textContent = `Tracking starts on ${start.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}. If you want every refresh to count as a click, disable Sessions in GoatCounter settings. Public counter data is cached and may lag slightly behind real time.`;
        loading.hidden = true;
    } catch (error) {
        console.error('Failed to load visit chart:', error);
        loading.hidden = true;
        empty.hidden = false;
        total.textContent = '--';
        footnote.textContent = 'If this stays empty after deployment, enable the public counter in GoatCounter or check whether a privacy blocker is preventing the request.';
    }
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
    setupVisitChart();

})
