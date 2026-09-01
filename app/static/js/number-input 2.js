(() => {
    function wireNumberInputs() {
        document.querySelectorAll('.number-input').forEach((element) => {
            if (element.closest('#generator-tablet')) return;
            if (element.dataset.numberReady === 'true') return;

            const input = element.querySelector('input[type="number"]');
            const minus = element.querySelector('.minus');
            const plus = element.querySelector('.plus');
            if (!input || !minus || !plus) return;

            element.dataset.numberReady = 'true';

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
    }

    document.addEventListener('DOMContentLoaded', wireNumberInputs);
    document.addEventListener('shiny:connected', wireNumberInputs);
    document.addEventListener('shiny:value', wireNumberInputs);
    window.setInterval(wireNumberInputs, 500);
    wireNumberInputs();
})();
