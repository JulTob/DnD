(() => {
  'use strict';

  // Glyph pools for the Great Old One patron text.  Deliberately plain Unicode
  // rather than a webfont: a general standard is a better dependency than a
  // CDN, and where a machine cannot render a glyph the failure is the point.
  const POOLS = [
    // Alchemical Symbols (U+1F700).  Plane 1, so coverage varies by machine,
    // which is wanted here.
    '\u{1F701}\u{1F702}\u{1F703}\u{1F704}\u{1F707}\u{1F70D}\u{1F70F}\u{1F714}\u{1F71A}\u{1F71B}\u{1F720}\u{1F728}',
    // Planetary and astrological, the symbols of a summoning circle.
    '☉☽☿♃♄♅♆⚸⚹⚴⚵⚶⚷',
    // Mathematical operators.  Lovecraft's horror is geometric before it is
    // anything else, and the logic signs carry meaning that helps: U+22A5 is
    // falsehood, U+2204 is "there does not exist", U+2205 is nothing.
    '∀∃∄∅∈∉∋∏∑√∞∫∮≡≠≢⊂⊃⊕⊗⊥¬∧∨∴∵⋰⋱⨀⨂⫯≬',
    ].join('');

  const GLYPHS = [...POOLS];

  // One glyph per second, held for 280ms.  Slow and patient on purpose: this
  // patron is asleep, and it is not in a hurry about you.
  const DEFAULT_RATE = 10;      // occurrences per ten seconds
  const DEFAULT_HOLD = 280;     // ms a glyph stays before the letter returns

  const reduced = window.matchMedia
    && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function textNodes(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const out = [];
    let node;
    while ((node = walker.nextNode())) {
      if (/\S/.test(node.nodeValue)) out.push(node);
      }
    return out;
    }

  // Nothing is wrapped while at rest.  Each occurrence splits one text node,
  // wraps a single character, and merges it back afterwards, so between
  // occurrences the DOM is byte-identical to the text the generator produced.
  // The original character is never removed: it stays in place holding its own
  // width and stays readable to copy-paste, find-in-page and screen readers,
  // while the glyph is painted over it and marked aria-hidden.
  function occur(root) {
    if (root.querySelector('.eldritch-glyph')) return;

    const nodes = textNodes(root);
    if (!nodes.length) return;
    const node = nodes[(Math.random() * nodes.length) | 0];
    const text = node.nodeValue;

    const spots = [];
    for (let i = 0; i < text.length; i++) {
      if (/\S/.test(text[i])) spots.push(i);
      }
    if (!spots.length) return;

    const at = spots[(Math.random() * spots.length) | 0];
    const hold = Number(root.dataset.eldritchHold) || DEFAULT_HOLD;

    const span = document.createElement('span');
    span.className = 'eldritch-glyph';

    // The real letter gets its own element so that *it* can be made
    // transparent while the wrapper keeps the surrounding text colour.  Do not
    // collapse these two: colouring the wrapper transparent makes the glyph
    // inherit transparent too, and the letter blinks out with nothing in its
    // place.
    const letter = document.createElement('span');
    letter.textContent = text[at];
    span.appendChild(letter);

    // The glyph is drawn by a ::after pseudo-element rather than a real node,
    // which is what keeps the sheet honest: generated content is not in the
    // DOM, so it cannot be selected, copied, matched by find-in-page, or read
    // by a screen reader.  Whatever anyone extracts from this page is the text
    // the generator wrote, no matter what it looks like at the time.
    span.style.setProperty(
      '--eldritch-glyph',
      '"' + GLYPHS[(Math.random() * GLYPHS.length) | 0] + '"',
      );

    const tail = node.splitText(at);
    tail.nodeValue = tail.nodeValue.slice(1);
    node.parentNode.insertBefore(span, tail);

    window.setTimeout(() => {
      if (!span.parentNode) return;
      span.parentNode.replaceChild(
        document.createTextNode(letter.textContent),
        span,
        );
      root.normalize();
      }, hold);
    }

  const running = new WeakSet();

  function start(root) {
    if (running.has(root)) return;
    running.add(root);
    const rate = Number(root.dataset.eldritchRate) || DEFAULT_RATE;
    window.setInterval(() => occur(root), 10000 / rate);
    }

  function scan() {
    if (reduced) return;
    document.querySelectorAll('.eldritch').forEach(start);
    }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', scan);
    } else {
    scan();
    }

  // Shiny swaps the sheet in and out without a page load.
  new MutationObserver(scan).observe(
    document.documentElement,
    { childList: true, subtree: true },
    );
  })();
