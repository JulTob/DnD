(() => {
  const GRID_SELECTOR = '.npc-grid, .spellcaster-box';
  const ITEM_SELECTOR = ':scope > .npc-box, :scope > .npc-textbox, :scope > .npc-textbox--full, :scope > .npc-scores, :scope > .npc-header';
  const ROW_PX = 10;
  let raf = null;

  function getColumnCount(grid) {
    const template = getComputedStyle(grid).gridTemplateColumns || '';
    if (!template) return 1;
    const cols = template.split(/\s+(?![^(]*\))/).filter(Boolean);
    return Math.max(1, cols.length);
  }

  function getGridItems(grid) {
    try {
      return grid.querySelectorAll(ITEM_SELECTOR);
    } catch (_e) {
      return grid.children;
    }
  }

  function applyMasonry(grid) {
    if (!grid) return;
    const items = getGridItems(grid);
    const columnCount = getColumnCount(grid);
    const disableMasonry = columnCount <= 1;

    if (disableMasonry) {
      grid.removeAttribute('data-masonry');
      grid.style.gridAutoRows = '';
      grid.style.gridAutoFlow = 'row';
      items.forEach((item) => {
        item.style.gridRowEnd = '';
      });
      return;
    }

    grid.setAttribute('data-masonry', 'on');
    grid.style.gridAutoRows = `${ROW_PX}px`;
    grid.style.gridAutoFlow = 'dense';

    const gap = parseFloat(getComputedStyle(grid).rowGap || '0') || 0;
    items.forEach((item) => {
      if (!(item instanceof HTMLElement)) return;
      item.style.gridRowEnd = 'auto';
      const h = item.getBoundingClientRect().height;
      const span = Math.max(1, Math.ceil((h + gap) / (ROW_PX + gap)));
      item.style.gridRowEnd = `span ${span}`;
    });
  }

  function runMasonry() {
    document.querySelectorAll(GRID_SELECTOR).forEach(applyMasonry);
  }

  function scheduleMasonry() {
    if (raf !== null) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      raf = null;
      runMasonry();
    });
  }

  document.addEventListener('DOMContentLoaded', scheduleMasonry);
  window.addEventListener('load', scheduleMasonry);
  window.addEventListener('resize', scheduleMasonry);
  // Web fonts change box heights after first paint — recompute spans once they settle.
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(scheduleMasonry); }

  const observer = new MutationObserver(scheduleMasonry);
  observer.observe(document.documentElement, { childList: true, subtree: true });
})();
