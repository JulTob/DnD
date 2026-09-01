(() => {
    function initGeneratorTablet() {
        const tablet = document.getElementById('generator-tablet');
        if (!tablet || tablet.dataset.ready === 'true') return false;

        const rotator = tablet.querySelector('.tablet-rotator');
        const panels = Array.from(tablet.querySelectorAll('.generator-panel'))
            .filter((panel) => !panel.classList.contains('is-parked'));
        const titleEl = tablet.querySelector('#tablet-title');
        const dotsRoot = tablet.querySelector('.tablet-dots');
        const prevBtn = tablet.querySelector('.tablet-nav.prev');
        const nextBtn = tablet.querySelector('.tablet-nav.next');

        if (!rotator || panels.length === 0) return false;

        tablet.dataset.ready = 'true';

        let currentIndex = panels.findIndex((panel) => panel.classList.contains('is-active'));
        let autoTimer = null;
        let stopped = false;
        const playerOnly = tablet.dataset.playerOnly === 'true' || panels.length < 2;

        if (currentIndex < 0) {
            currentIndex = 0;
            }

    const restartAutoRotate = () => {
        if (stopped || playerOnly) return;
        if (autoTimer) clearInterval(autoTimer);
        autoTimer = setInterval(goNext, 12000);
        };

    // Any interaction with the tablet permanently stops the auto-rotation.
    const stopAutoRotate = () => {
        stopped = true;
        if (autoTimer) {
            clearInterval(autoTimer);
            autoTimer = null;
            }
        };

    const goTo = (index) => {
        currentIndex = (index + panels.length) % panels.length;
        rotator.style.transform = `translateX(${-100 * currentIndex}%)`;

        panels.forEach((panel, idx) => {
            panel.classList.toggle('is-active', idx === currentIndex);
            });

      if (dotsRoot) {
        dotsRoot.querySelectorAll('.tablet-dot').forEach((dot, idx) => {
          dot.classList.toggle('is-active', idx === currentIndex);
        });
      }

    if (titleEl) {
        titleEl.textContent = panels[currentIndex]?.dataset.title || 'Generator';
        }

      restartAutoRotate();
    };

    const goNext = () => goTo(currentIndex + 1);
    const goPrev = () => goTo(currentIndex - 1);

    if (dotsRoot) {
        dotsRoot.innerHTML = '';

        panels.forEach((panel, index) => {
            const dot = document.createElement('button');
            dot.type = 'button';
            dot.className = 'tablet-dot';
            dot.setAttribute('aria-label', `Show ${panel.dataset.title || 'generator'}`);
            dot.addEventListener('click', () => goTo(index));
            dotsRoot.appendChild(dot);
        });
    }

    prevBtn?.addEventListener('click', goPrev);
    nextBtn?.addEventListener('click', goNext);

    tablet.addEventListener('mouseenter', () => {
        if (autoTimer) clearInterval(autoTimer);
        });

    tablet.addEventListener('mouseleave', restartAutoRotate);

    // Stop auto-rotation for good on the first real interaction (click, tap, key).
    tablet.addEventListener('pointerdown', stopAutoRotate, true);
    tablet.addEventListener('keydown', stopAutoRotate, true);

    tablet.querySelectorAll('.number-input').forEach((element) => {
        const input = element.querySelector('input[type="number"]');
        const minus = element.querySelector('.minus');
        const plus = element.querySelector('.plus');
        if (!input || !minus || !plus) return;

        minus.addEventListener('click', () => {
            const min = Number(input.min || 1);
            const current = Number(input.value || min);
            input.value = String(Math.max(min, current - 1));
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
        });

        plus.addEventListener('click', () => {
            const max = Number(input.max || 100);
            const min = Number(input.min || 1);
            const current = Number(input.value || min);
            input.value = String(Math.min(max, current + 1));
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
            });
        });

    goTo(currentIndex);

    if (window.Shiny && typeof window.Shiny.bindAll === 'function') {
        window.Shiny.bindAll(tablet);
        }

    return true;
    }

    const scheduleInit = () => {
        window.requestAnimationFrame(initGeneratorTablet);
        window.setTimeout(initGeneratorTablet, 50);
        window.setTimeout(initGeneratorTablet, 250);
        };

    document.addEventListener('DOMContentLoaded', scheduleInit);
    document.addEventListener('shiny:connected', scheduleInit);
    document.addEventListener('shiny:value', scheduleInit);

    scheduleInit();
    window.setInterval(initGeneratorTablet, 500);
})();
