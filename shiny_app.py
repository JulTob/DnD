from __future__ import annotations

import asyncio
import inspect
from html import escape
from pathlib import Path
from random import choice, randint
from typing import Any
from app.character_url import (
    character_params_to_hash,
    parse_character_params_from_path,
    parse_character_params_from_url,
)

import app.random as random
from AtlasVenustas.Kit_of_Loader import loader_head_tags, loader_panel
from Minion import chronicler, minion
from shiny import App, reactive, render, ui  
# pyright: ignore[reportMissingImports]

# Atlas imports — plain and loud on purpose (QST-0009, Decree 0003).
# If an Atlas is broken the app must refuse to start with the real traceback,
# never run on placeholder shadows. Resilience lives at the summoning layer,
# where the Minions report every failure and recovery rerolls the seed.
from AtlasActorLudi.Map_of_Scores import Modifier
from AtlasAlusoris.Grimoire_of_NPC import NPC
from AtlasAlusoris.Map_of_Archetypes import Archetype, Archetypes
from AtlasAlusoris.Map_of_Races import Race, race_weights
from AtlasLusoris.Grimoire_of_Characters import Character
from AtlasLusoris.Map_of_Backgrounds import backgrounds
from AtlasLusoris.Map_of_Classes import classes
from AtlasLusoris.Map_of_Species import species as species_dict
from AtlasPugna.Map_of_Legendary_Actions import Lair, Legendary, Region


STYLE_PATH = Path(__file__).parent / "app" / "static" / "style.css"
BASE_STYLE = STYLE_PATH.read_text(encoding="utf-8") if STYLE_PATH.exists() else ""

EXTRA_STYLE = """
html, body {
    min-height: 100%;
}

.container-fluid {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.main-wrap {
    flex: 1 0 auto;
}

.container {
    flex: 1 0 auto;
    width: min(1100px, 96%);
    padding-bottom: 2rem;
}

header, footer {
    flex: 0 0 auto;
    position: static !important;
}

.npc-page {
    width: min(100%, 980px);
    height: auto;
    min-height: 0;
    overflow: visible;
}

.note-lines {
    position: relative;
}

.npc-grid {
    display: grid !important;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    grid-auto-flow: row;
    align-items: start;
    gap: 8px;
    width: 100%;
    max-width: 980px;
    margin: 0 auto;
}

@media (max-width: 1080px) {
    .npc-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }
}

@media (max-width: 820px) {
    .npc-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 560px) {
    .npc-grid {
        grid-template-columns: minmax(0, 1fr);
    }
}

.npc-grid > .npc-box,
.npc-grid > .npc-textbox,
.npc-grid > .npc-scores {
    width: 100%;
    min-width: 0;
    max-width: none;
    overflow-wrap: anywhere;
    align-self: start;
}

.npc-scores {
    display: grid;
    grid-template-columns: minmax(0, 1fr);
    gap: 6px;
}

.npc-scores > .npc-box {
    width: 100%;
    min-width: 0;
    max-width: none;
}

.npc-grid > .npc-header,
.npc-grid > .npc-textbox--full {
    grid-column: 1 / -1;
}

/* Character sheet: a left rail (scores / skills / saves) beside packed stat boxes, prose below. */
.sheet {
    width: min(100%, 980px);
    margin: 0 auto;
}

.sheet-body {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    gap: 12px;
    margin-top: 10px;
}

.sheet-rail {
    flex: 0 0 252px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.sheet-rail > .npc-box,
.sheet-rail > .npc-textbox,
.sheet-rail > .stat-flow {
    width: 100%;
    margin: 0;
}

.sheet-main {
    flex: 1 1 380px;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.stat-flow {
    display: grid;
    grid-template-columns: minmax(0, 1fr);
    gap: 6px;
}

.stat-flow > .npc-box {
    width: 100%;
    max-width: none;
    min-width: 0;
    margin: 0;
    flex: unset;
}

/* Record chip: one per line; icon sits behind-left like score boxes. */
.stat-chip {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    text-align: right;
    gap: 2px;
    padding: 8px 10px;
    position: relative;
}

.stat-chip .symbol {
    position: absolute;
    top: 5px;
    left: 5px;
    transform: none;
    width: 30px;
    height: 30px;
    font-size: 17px;
    line-height: 1;
    margin: 0;
    z-index: -1;
}

.stat-chip .record {
    font-family: var(--font-record);
    font-size: 0.8em;
    letter-spacing: 0.01em;
    color: var(--secondary-color);
    line-height: 1.15;
    overflow-wrap: anywhere;
}

.stat-chip .value {
    font-family: var(--font-value);
    font-size: 1.2em;
    font-weight: 700;
    line-height: 1.1;
    overflow-wrap: anywhere;
}

.sheet-rail .npc-scores > .npc-box {
    width: 100%;
    min-width: 0;
    max-width: none;
    box-sizing: border-box;
}

.sheet-rail .npc-scores > .score-row {
    width: 100%;
    min-width: 0;
    max-width: none;
    box-sizing: border-box;
}

/* Ability scores live inside a wrapper: `class="npc-box npc-scores"`.
   `.npc-box` has `max-width: 180px` in base CSS, which caps the whole rail.
   Override in the rail so the wrapper can fill the column. */
.sheet-rail .npc-box.npc-scores {
    width: 100%;
    min-width: 0;
    max-width: none;
    box-sizing: border-box;
}

/* Character name & title in IM Fell English SC. */
.npc-header h2 {
    font-family: var(--font-name);
    font-weight: 700;
    font-size: clamp(3.1rem, 2.6vw, 1.45rem);
    line-height: 1.5;
}

/* Name is h2:first-of-type; the next h2 is the "Title" line. */
.npc-header h2:nth-of-type(2) {
    font-size: calc(clamp(3.1rem, 2.6vw, 1.45rem) * 0.80);
    line-height: 1.05;
}

/* Fantasy section titles (e.g. Spells) in Eagle Lake. */
.sheet-section.is-fantasy > h1,
.sheet-section.is-fantasy > h2,
.sheet-section.is-fantasy > h3 {
    font-family: var(--font-fantasy);
}

/* Everything else: clean prose, each section parted by a gold horizontal rule. */
.sheet-section {
    border-top: 1px solid var(--gold-color);
    padding-top: 0.7rem;
    margin-top: 1rem;
}

.sheet-section:first-of-type {
    border-top: 0;
    margin-top: 0.4rem;
}

.sheet-section > h1,
.sheet-section > h2,
.sheet-section > h3 {
    margin: 0 0 0.45rem;
}

.sheet-section .prose-body {
    max-width: 70ch;
    font-family: var(--font-text);
    font-size: 1.04rem;
    line-height: 1.7;
}

.sheet-section .prose-body p { margin: 0 0 0.7em; }
.sheet-section .prose-body table { width: 100%; }

/* Generator HTML (spells in features) must read as body prose, not markdown code blocks. */
.sheet-section .prose-body pre,
.sheet-section .prose-body code {
    font-family: var(--font-text);
    font-size: inherit;
    line-height: inherit;
    background: transparent;
    border: none;
    padding: 0;
    margin: 0;
    white-space: normal;
    overflow: visible;
}

.sheet-section .prose-body .feature-entry {
    margin: 0 0 1.1em;
}

.sheet-section .prose-body .feature-lead {
    margin: 0 0 0.35em;
}

.sheet-section .prose-body .spell {
    font-family: var(--font-text);
    font-size: 1.04rem;
    line-height: 1.7;
    margin: 0.5em 0 0.9em;
}

.sheet-section .prose-body .spell h4 {
    font-family: var(--font-fantasy);
    font-size: 1.25em;
    margin: 0.4em 0 0.15em;
}

.sheet-section .prose-body .spell p {
    margin: 0 0 0.55em;
}

/* Long-form sections — rules, backstory, spells — read as a page, not a box. */
.npc-prose {
    grid-column: 1 / -1;
    text-align: left;
    padding: 1.3rem 1.5rem 1.4rem;
    margin: 8px 0;
}

.npc-prose > h1,
.npc-prose > h2,
.npc-prose > h3 {
    text-align: center;
    margin: 0 0 0.7rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--gold-color);
}

.npc-prose .prose-body {
    max-width: 66ch;
    margin: 0 auto;
    font-family: var(--font-text);
    font-size: 1.06rem;
    line-height: 1.72;
}

.npc-prose .prose-body > :first-child { margin-top: 0; }
.npc-prose .prose-body > :last-child { margin-bottom: 0; }

.npc-prose .prose-body p {
    margin: 0 0 0.85em;
    text-align: justify;
    hyphens: auto;
}

.npc-prose .prose-body h2,
.npc-prose .prose-body h3,
.npc-prose .prose-body h4 {
    text-align: left;
    color: var(--secondary-color);
    margin: 1.05em 0 0.3em;
}

.npc-prose .prose-body ul,
.npc-prose .prose-body ol {
    margin: 0 0 0.85em 1.4em;
    padding: 0;
}

.npc-prose .prose-body li { margin: 0.15em 0; }
.npc-prose .prose-body em { color: var(--primary-color); }

.npc-prose .prose-body blockquote {
    margin: 0 0 0.85em;
    padding-left: 0.9em;
    border-left: 3px solid var(--gold-color);
    font-style: italic;
}

.character-level-controls {
    display: grid;
    grid-template-columns: repeat(2, 2.8rem);
    gap: 0.35rem;
    margin: 0;
}

.character-level-controls .action-button {
    min-width: 2.8rem;
    width: 2.8rem;
    min-height: 2.8rem;
    height: 2.8rem;
    padding: 0;
    line-height: 1;
    font-size: 1.55rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.spellcaster-box {
    overflow-wrap: anywhere;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 8px;
    align-items: start;
}

.spellcaster-box > .npc-textbox {
    width: auto;
    min-width: 0;
    max-width: none;
    margin: 0;
}

.spellcaster-box > .npc-textbox--full {
    grid-column: 1 / -1;
    width: auto;
    max-width: none;
    margin: 0;
}

.spellcaster-box > * {
    min-width: 0;
}

.npc-grid[data-masonry="on"] {
    grid-auto-rows: 10px;
}

.header-actions {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    margin-right: 1rem;
}

.header-actions .action-button {
    width: auto;
}

.shiny-input-container {
    width: 100%;
    margin-bottom: 0.4rem;
}

.shiny-input-container label {
    color: var(--text-color);
    font-family: var(--font-header);
    margin-bottom: 0.25rem;
    font-weight: bold;
}

.shiny-input-select,
.shiny-input-container input[type="number"] {
    background-color: var(--black-color);
    color: var(--gold-color);
    border: 2px solid var(--gold-color);
    padding: 10px;
    font-family: var(--font-fancy);
    border-radius: 8px;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.5);
    text-align: center;
}

.shiny-input-select:focus,
.shiny-input-container input[type="number"]:focus {
    outline: none;
    border-color: var(--primary-color);
}

.page-title {
    margin-top: 1rem;
}

.character-reforge {
    display: grid;
    grid-template-columns: minmax(360px, 580px) minmax(300px, 500px);
    grid-template-areas:
        "species level_block"
        "class generate"
        "background share";
    gap: 1.4rem 3.5rem;
    align-items: stretch;

    width: min(100%, 1080px);
    margin: 0.4rem auto 0.6rem;
}


.character-reforge-field,
.character-level-box,
.character-generate-wrap,
.character-share-wrap {
    min-width: 0;
}

.character-reforge .shiny-input-select,
.character-reforge .action-button,
.character-reforge .fantasy-button,
.character-level-box {
    width: 100%;
    box-sizing: border-box;
}

.character-reforge-field {
    min-width: 0;
}

.character-reforge .shiny-input-container {
    margin: 0;
}

.character-reforge-field--species {
    grid-area: species;
}

.character-reforge-field--class {
    grid-area: class;
}

.character-reforge-field--background {
    grid-area: background;
}

.character-level-box {
    grid-area: level_block;
    display: grid;
    grid-template-columns: 2.8rem minmax(4.5rem, 1fr) 2.8rem;
    align-items: center;
    gap: 0.35rem;
    min-height: 3.05rem;
    padding: 0;
    border: 2px solid var(--gold-color);
    border-radius: 8px;
    background: rgba(0, 0, 0, 0.92);
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.35);
    overflow: hidden;
}

.character-level-label {
    grid-column: 2;
    grid-row: 1;
    margin: 0;
    padding: 0;
    font-family: var(--font-header);
    font-size: 0.9rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--gold-color);
}

.character-reforge .control-label,
.character-reforge .shiny-input-container > label,
.character-reforge label[for^="char_sheet_"] {
    display: none;
}

.character-reforge .fantasy-button {
    width: 100%;
    font-size: 1rem;
}

.character-reforge .fantasy-button:hover {
    font-size: 1rem;
}

.character-reforge .character-level-controls .fantasy-button {
    width: 2.8rem;
    min-width: 2.8rem;
    min-height: 3.05rem;
    height: 3.05rem;
    flex: 0 0 2.8rem;
    border: 0;
    border-radius: 0;
    box-shadow: none;
}

.character-level-controls {
    display: contents;
}

.character-level-controls .minus {
    grid-column: 1;
    grid-row: 1;
}

.character-level-controls .plus {
    grid-column: 3;
    grid-row: 1;
}

.character-generate-wrap {
    grid-area: generate;
    align-self: stretch;
}

.character-generate-wrap .action-button {
    margin: 0;
    min-height: 3.05rem;
}

.character-share-wrap {
    grid-area: share;
    align-self: stretch;
}

.character-share-wrap .action-button {
    margin: 0;
    width: 100%;
    min-height: 3.05rem;
}

.character-share-wrap .share-button {
    min-width: 6.4rem;
}

.character-reforge-status {
    grid-column: 1 / -1;
    margin-top: 0.05rem;
}

@media (max-width: 900px) {
    .character-reforge {
        grid-template-columns: minmax(0, 1fr);
        grid-template-areas:
            "species"
            "class"
            "background"
            "level_block"
            "generate"
            "share";
        align-items: stretch;
        width: 100%;
    }

    .character-level-box {
        align-items: stretch;
    }

    .character-level-label {
        text-align: center;
    }

    .character-generate-wrap {
        flex-wrap: wrap;
    }

    .character-generate-wrap .action-button {
        flex: 1 1 100%;
    }

    .character-share-wrap .action-button {
        width: 100%;
    }
}

.share-copy-status {
    min-height: 1.2rem;
    color: var(--primary-color);
    font-family: var(--font-header);
    font-size: 0.95rem;
}

.fallback-card {
    border: 2px solid #333;
    border-radius: 8px;
    background: #fff;
    padding: 0.8rem;
}

#loader-message {
    position: absolute;
    top: calc(50% + 180px);
    left: 50%;
    transform: translateX(-50%);
    color: #f6d67c;
    font-family: var(--font-header);
    letter-spacing: 0.04em;
    text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
    font-size: 1.05rem;
    pointer-events: none;
    min-width: 260px;
    text-align: center;
}

.npc-list a {
    color: black;
    text-decoration: none;
    position: relative;
    overflow: hidden;
    display: inline-block;
    padding: 2px 4px;
    border-radius: 4px;
    transition: transform 0.2s ease;
}

.npc-list a::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(120deg, transparent, rgba(255, 255, 255, 0.5), transparent);
    transition: left 0.8s;
}

.npc-list a:hover::before {
    left: 100%;
}

.npc-list a:hover {
    transform: scale(1.02);
}
"""

HOME_SCRIPT = """
(() => {
    function initGeneratorTablet() {
        const tablet = document.getElementById('generator-tablet');
        if (!tablet || tablet.dataset.ready === 'true') return false;

        const rotator = tablet.querySelector('.tablet-rotator');
        const panels = Array.from(tablet.querySelectorAll('.generator-panel'));
        const titleEl = tablet.querySelector('#tablet-title');
        const dotsRoot = tablet.querySelector('.tablet-dots');
        const prevBtn = tablet.querySelector('.tablet-nav.prev');
        const nextBtn = tablet.querySelector('.tablet-nav.next');

        if (!rotator || panels.length === 0) return false;

        tablet.dataset.ready = 'true';

        let currentIndex = panels.findIndex((panel) => panel.classList.contains('is-active'));
        let autoTimer = null;

        if (currentIndex < 0) {
            currentIndex = 0;
            }

    const restartAutoRotate = () => {
        if (autoTimer) clearInterval(autoTimer);
        autoTimer = setInterval(goNext, 12000);
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
"""

MASONRY_SCRIPT = """
(() => {
  const GRID_SELECTOR = '.npc-grid, .spellcaster-box';
  const ITEM_SELECTOR = ':scope > .npc-box, :scope > .npc-textbox, :scope > .npc-textbox--full, :scope > .npc-scores, :scope > .npc-header';
  const ROW_PX = 10;
  let raf = null;

  function getColumnCount(grid) {
    const template = getComputedStyle(grid).gridTemplateColumns || '';
    if (!template) return 1;
    const cols = template.split(/\\s+(?![^(]*\\))/).filter(Boolean);
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
"""


def _safe_str(value: Any, fallback: str = "-") -> str:
    if value is None:
        return fallback
    return str(value)


def _safe_int(value: Any, fallback: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


def _selection_or_none(value: str | None) -> str | None:
    if not value or value == "Random":
        return None
    return value


@minion  # every failed attempt reports its full bug tree; the caller recovers
def _attempt_character(**kwargs: Any) -> Character:
    """One summoning attempt. Reporting is the Minion's job; recovery is the caller's."""
    return Character(**kwargs)


@minion  # every failed attempt reports its full bug tree; the caller recovers
def _attempt_npc(**kwargs: Any) -> NPC:
    """One summoning attempt. Reporting is the Minion's job; recovery is the caller's."""
    return NPC(**kwargs)


@chronicler  # one creation = one account: repeats collapse to ×N, errors gather at the end
def summon_character(
    species: str | None = None,
    char_class: str | None = None,
    background: str | None = None,
    level: int = 1,
    gender: str | None = None,
    seed: int | None = None,
) -> Character:
    """Always hand the user a character: retry fresh seeds on failure, report every error (QST-0009)."""
    max_attempts = 5
    try:
        base_seed = int(seed) if seed is not None else None
    except (TypeError, ValueError):
        base_seed = None

    if base_seed is None:
        base_seed = random.randint(0, 2**16)

    current_seed = base_seed
    last_error: Exception | None = None

    for _ in range(max_attempts):
        try:
            return _attempt_character(
                species=species,
                char_class=char_class,
                background=background,
                level=level,
                gender=gender,
                seed=current_seed,
            )
        except Exception as exc:  # reported by the @minion above; recover with a fresh seed
            last_error = exc
            current_seed += 1

    raise RuntimeError("Unable to summon character after retries.") from last_error


@chronicler  # one creation = one account
def summon_npc(
    race: str | None = None,
    archetype: str | None = None,
    level: int = 1,
    seed: int | None = None,
) -> NPC:
    """Always hand the user an NPC: retry fresh seeds on failure, report every error (QST-0009)."""
    max_attempts = 5
    if race == "Random" or not race:
        race = Race()
    if archetype == "Random" or not archetype:
        archetype = Archetype()

    npc_seed = int(seed) if seed is not None else randint(1, 2**16)
    last_error: Exception | None = None

    for _ in range(max_attempts):
        random.seed(npc_seed)
        try:
            return _attempt_npc(race=race, archetype=archetype, lvl=max(int(level), 1), seed=npc_seed)
        except Exception as exc:  # reported by the @minion above; recover with a fresh seed
            last_error = exc
            npc_seed += 1

    raise RuntimeError("Unable to summon NPC after retries.") from last_error


def _prose(text: Any, placeholder: str = "—") -> ui.Tag:
    """Render generator text as flowing markdown prose — a page, not a cramped box."""
    body = _safe_str(text, "").strip()
    return ui.markdown(body) if body else ui.p(placeholder)


def _html_prose(html: str, placeholder: str = "—") -> ui.Tag:
    """Render pre-built HTML as flowing prose (spells, features with embedded markup)."""
    body = _safe_str(html, "").strip()
    return ui.HTML(body) if body else ui.p(placeholder)


def _text_html(value: Any, placeholder: str = "-") -> ui.Tag:
    """Plain model text as HTML: escape first, then honor newlines as <br> (QST-0012).

    The one safe door for generator strings (skills, saves, senses, story...).
    Code-authored HTML goes through _html_prose instead — never through here.
    """
    text = _safe_str(value, placeholder)
    return ui.HTML(escape(text).replace("\n", "<br>"))


def _feature_item(name: str, description: str) -> ui.Tag:
    """Feature blurbs often embed spell HTML — render as HTML, not markdown."""
    body = _safe_str(description, "").strip()
    return ui.div(
        {"class": "feature-entry"},
        ui.HTML(f"<p class='feature-lead'><strong>{escape(_safe_str(name))}.</strong></p>{body}"),
    )


def prose_block(title: str, *content: Any, level: int = 2) -> ui.Tag:
    """A full-width tome section: a heading and long-form prose (rules, backstory, spells).

    No callers since QST-0008 moved the NPC sheet onto prose_section.
    Kept only while QST-0026's spell-render audit is Working - retire with it.
    """
    heading = {1: ui.h1, 2: ui.h2, 3: ui.h3}.get(level, ui.h2)
    return ui.div(
        {"class": "npc-textbox npc-textbox--full npc-prose"},
        heading(title),
        ui.div({"class": "prose-body"}, *content),
    )


def prose_section(title: str, *content: Any, level: int = 3, accent: bool = False) -> ui.Tag:
    """A titled prose section in the sheet's main column, divided by a gold rule.
    accent=True styles the heading in the fantasy display face (--font-fantasy)."""
    heading = {1: ui.h1, 2: ui.h2, 3: ui.h3}.get(level, ui.h3)
    cls = "sheet-section is-fantasy" if accent else "sheet-section"
    return ui.div(
        {"class": cls},
        heading(title),
        ui.div({"class": "prose-body"}, *content),
    )


def stat_chip(emoji: str, label: str, value: str) -> ui.Tag:
    """One short stat as a chip: symbol, record label, value. Shared by both sheets."""
    return ui.div(
        {"class": "npc-box stat-chip"},
        ui.div({"class": "symbol"}, emoji),
        ui.div({"class": "record"}, label),
        ui.div({"class": "value"}, value),
    )


def spellbook_prose(caster: Any) -> str:
    """Render a spellcaster's book as flowing markdown — no boxes, grouped by level."""
    spells = list(getattr(caster, "spells_known", []) or [])
    lines: list[str] = []
    try:
        lines.append(f"**Spell Save DC** {caster.spell_save_dc()} · **Attack** +{caster.spell_attack_bonus()}")
    except Exception:
        pass
    slots = getattr(caster, "spell_slots", None)
    if slots:
        try:
            lines.append("**Slots** — " + ", ".join(f"L{lvl}: {n}" for lvl, n in slots.items()))
        except Exception:
            pass
    by_level: dict[int, list[str]] = {}
    for s in spells:
        lvl = _safe_int(getattr(s, "level", 0), 0)
        by_level.setdefault(lvl, []).append(_safe_str(getattr(s, "name", s)))
    for lvl in sorted(by_level):
        label = "Cantrips" if lvl == 0 else f"Level {lvl}"
        lines.append(f"**{label}:** " + ", ".join(sorted(by_level[lvl])))
    return "\n\n".join(lines) if lines else "No spells known."


def build_character_sheet(data: dict[str, Any]) -> ui.Tag:
    stats = data.get("Stats") or {}
    ability_emoji = {
        "Strength": "🦾",
        "Dexterity": "🥢",
        "Constitution": "🫀",
        "Intelligence": "🧩",
        "Wisdom": "🦉",
        "Charisma": "🎭",
    }
    feature_items: list[Any] = []
    for feat in data.get("features", []) or []:
        fname = getattr(feat, "name", None)
        if fname:
            fdesc = _safe_str(getattr(feat, "description", ""), "")
            feature_items.append(_feature_item(_safe_str(fname), fdesc))
        else:
            feature_items.append(_prose(str(feat)))

    spellcaster = data.get("Spellcaster")

    skill_lines: list[Any] = []
    skills_obj = data.get("Skills")
    if hasattr(skills_obj, "list"):
        try:
            for skill, label in skills_obj.list:
                prof = getattr(skill, "proficiency_level", 0)
                mark = "⭐️" if prof == 2 else ("⚫" if prof == 1 else "⚪")
                mod = skill.calculate_modifier() if hasattr(skill, "calculate_modifier") else ""
                skill_lines.append(ui.tags.tr(ui.tags.td(mark), ui.tags.td(_safe_str(label)), ui.tags.td(_safe_str(mod))))
        except Exception:
            skill_lines = [ui.tags.tr(ui.tags.td("⚪"), ui.tags.td(_safe_str(skills_obj)), ui.tags.td(""))]
    else:
        skill_lines = [ui.tags.tr(ui.tags.td("⚪"), ui.tags.td(_safe_str(skills_obj)), ui.tags.td(""))]

    stat_boxes: list[Any] = []
    for stat, value in stats.items():
        ivalue = _safe_int(value, 10)
        mod = (ivalue - 10) // 2
        emoji = ability_emoji.get(_safe_str(stat), "")
        stat_boxes.append(
            ui.div(
                {"class": "npc-box score-row", "style": "text-align: right;"},
                *( [ui.div({"class": "symbol"}, emoji)] if emoji else [] ),
                ui.h4(ui.HTML(f"{escape(_safe_str(stat))}<br>{ivalue} ({mod:+d})")),
            )
        )

    prof_list = data.get("other_proficiencies") or []
    equipment = data.get("equipment")

    equipment_lines = []
    if equipment is not None:
        for label, attr in [
            ("Defense", "defense"),
            ("Melee", "melee"),
            ("Ranged", "ranged"),
            ("Right", "right"),
            ("Left", "left"),
        ]:
            equipment_lines.append(
                ui.tags.tr(
                    ui.tags.td(label),
                    ui.tags.td(ui.tags.b(_safe_str(getattr(equipment, attr, "-")))),
                )
            )

    bag_rows = []
    if equipment is not None:
        for item in getattr(equipment, "bag", []) or []:
            bag_rows.append(
                ui.tags.tr(
                    ui.tags.td(_safe_str(getattr(item, "name", "item"))),
                    ui.tags.td(f"x{_safe_str(getattr(item, 'quantity', 1))}"),
                    ui.tags.td(f"{_safe_str(getattr(item, 'weight', 0))} lbs"),
                    ui.tags.td(f"{_safe_str(getattr(item, 'value', 0))} gp"),
                )
            )

    saving_throw_obj = data.get("SavingThrow")
    saving_throw_value = getattr(saving_throw_obj, "string", saving_throw_obj)
    if callable(saving_throw_value):
        try:
            saving_throw_value = saving_throw_value()
        except Exception:
            saving_throw_value = saving_throw_obj
    saving_throw_html = _text_html(saving_throw_value, "-")

    story_html = _text_html(data.get("Story", ""))

    scores_box = ui.div({"class": "npc-box npc-scores"}, *stat_boxes)
    skills_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Skills"),
        ui.tags.table({"class": "skills-table"}, ui.tags.tbody(*skill_lines)),
        ui.h4(f"Passive Perception: {_safe_str(data.get('passive_perception', '-'))}"),
    )
    saves_box = ui.div({"class": "npc-textbox"}, ui.h2("Saving Throws"), saving_throw_html)

    stat_chips = [
        stat_chip("⚖️", "Alignment", _safe_str(data.get("Alignment", "-"))),
        stat_chip("⚧", "Gender", _safe_str(data.get("Gender", "-"))),
        stat_chip("📏", "Size", _safe_str(data.get("size", "-"))),
        stat_chip("👟", "Speed", _safe_str(data.get("Speed", "-"))),
        stat_chip("⬆️", "Level", _safe_str(data.get("Level", "-"))),
        stat_chip("⚜️", "Proficiency Bonus", f"+{_safe_str(data.get('PB', '-'))}"),
        stat_chip("💚", "Hit Points", _safe_str(data.get("Health", "-"))),
        stat_chip("🎲", "Hit Dice", _safe_str(data.get("HPD", "-"))),
        stat_chip("🛡️", "Armor Class", _safe_str(data.get("AC", "-"))),
    ]

    rail_items: list[Any] = [scores_box, skills_box, saves_box]
    if prof_list:
        rail_items.append(
            ui.div(
                {"class": "npc-textbox"},
                ui.h2("Proficiencies"),
                ui.tags.ul(*[ui.tags.li(_safe_str(p)) for p in prof_list]),
            )
        )

    prose_sections: list[Any] = []
    if equipment is not None:
        equip_content: list[Any] = [ui.tags.table({"class": "objects-table"}, ui.tags.tbody(*equipment_lines))]
        if bag_rows:
            equip_content.append(ui.h4("Bag"))
            equip_content.append(ui.tags.table({"class": "objects-table"}, ui.tags.tbody(*bag_rows)))
        equip_content.append(ui.h4(f"Purse: {_safe_str(getattr(equipment, 'purse', '-'))} gp"))
        prose_sections.append(prose_section("Equipment", *equip_content))
    prose_sections.append(prose_section("Backstory", _prose(data.get("Story", ""))))
    prose_sections.append(
        prose_section("Features", *feature_items) if feature_items else prose_section("Features", ui.p("None"))
    )
    if spellcaster is not None:
        prose_sections.append(prose_section("Spells", _prose(spellbook_prose(spellcaster)), accent=True))

    return ui.div(
        {"class": "sheet note-lines"},
        ui.div(
            {"class": "npc-header"},
            ui.h2(_safe_str(data.get("name", "Unknown"), "Unknown")),
            ui.h2(_safe_str(data.get("title", ""), "")),
            ui.h1(
                f"{_safe_str(data.get('Class', '-'))}, "
                f"{_safe_str(data.get('Subclass', '-'))}"
            ),
            ui.h1(f"{_safe_str(data.get('Species', '-'))} {_safe_str(data.get('Background', '-'))}"),
        ),
        ui.div(
            {"class": "sheet-body"},
            ui.div(
                {"class": "sheet-rail"},
                ui.div({"class": "stat-flow"}, *stat_chips),
                *rail_items,
            ),
            ui.div(
                {"class": "sheet-main"},
                *prose_sections,
            ),
        ),
    )


def build_npc_sheet(npc: NPC) -> ui.Tag:
    """The NPC page in the character sheet's vocabulary: rail + chips + prose (QST-0008)."""
    race = _safe_str(getattr(npc, "race", "-"))
    subrace = _safe_str(getattr(npc, "subrace", "-"))
    background = _safe_str(getattr(npc, "background", "-"))
    score_emojis = {
        "STR": "\U0001f9be",
        "DEX": "\U0001f962",
        "CON": "\U0001fac0",
        "INT": "\U0001f9e9",
        "WIS": "\U0001f989",
        "CHA": "\U0001f3ad",
    }

    try:
        legendary = str(Legendary(npc))
    except Exception:
        legendary = "Unavailable"

    try:
        lair = str(Lair(npc))
    except Exception:
        lair = "Unavailable"

    try:
        region = str(Region(npc))
    except Exception:
        region = "Unavailable"

    ability = getattr(npc, "ability_scores", None)
    story_text = getattr(npc, "Story", None)
    if story_text in (None, ""):
        try:
            story_text = getattr(npc, "story")
        except Exception:
            story_text = "-"

    def score(name: str) -> int:
        if ability is None:
            return 10
        return _safe_int(getattr(ability, name, 10), 10)

    def row(name: str, emoji: str) -> ui.Tag:
        value = score(name)
        mod = Modifier(value)
        return ui.div(
            {"class": "npc-box", "style": "text-align: right;"},
            ui.div({"class": "symbol"}, emoji),
            ui.h2(f"{name}: {value} {mod:+d}"),
        )

    # --- The rail: scores, skills, saves, and the short list boxes ---
    scores_box = ui.div(
        {"class": "npc-box npc-scores"},
        row("STR", score_emojis["STR"]),
        row("DEX", score_emojis["DEX"]),
        row("CON", score_emojis["CON"]),
        row("INT", score_emojis["INT"]),
        row("WIS", score_emojis["WIS"]),
        row("CHA", score_emojis["CHA"]),
    )
    skills_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Skills"),
        _text_html(getattr(getattr(npc, "skills", None), "string", lambda *_: "-")(ability)),
        ui.h4(f"Passive Perception: {_safe_str(getattr(npc, 'passive_perception', '-'))}"),
    )
    saves_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Saving Throws"),
        _text_html(getattr(getattr(npc, "saving_throws", None), "string", "-")),
    )
    languages_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Languages"),
        ui.p(_safe_str(getattr(npc, "languages", "-"))),
    )
    movement_box = ui.div({"class": "npc-textbox"}, ui.h2("Movement"), _text_html(getattr(npc, "movement", "-")))
    senses_box = ui.div({"class": "npc-textbox"}, ui.h2("Senses"), _text_html(getattr(npc, "senses", "-")))
    resistances_box = ui.div({"class": "npc-textbox"}, ui.h2("Resistances"), _text_html(getattr(npc, "resistances", "-")))

    # --- Short stats as chips, same vocabulary as the character sheet ---
    stat_chips = [
        stat_chip("\u2696\ufe0f", "Alignment", _safe_str(getattr(npc, "alignment", "-"))),
        stat_chip("\u26a7", "Gender", _safe_str(getattr(npc, "gender", "-"))),
        stat_chip("\U0001f4cf", "Size", _safe_str(getattr(npc, "size", "-"))),
        stat_chip("\u2b06\ufe0f", "Level", _safe_str(getattr(npc, "level", "-"))),
        stat_chip("\u269c\ufe0f", "Proficiency Bonus", f"+{_safe_str(getattr(npc, 'proficiency_bonus', '-'))}"),
        stat_chip("\U0001f49a", "Hit Points", _safe_str(getattr(npc, "HP", "-"))),
        stat_chip("\U0001f6e1\ufe0f", "Armor Class", _safe_str(getattr(npc, "AC", "-"))),
    ]

    # --- Long text flows as prose sections, never boxes (Dialog 0001) ---
    prose_sections = [
        prose_section(
            "Personality",
            ui.h4("Trait"),
            ui.p(ui.tags.i(_safe_str(getattr(npc, "trait", "-")))),
            ui.h4("Ideal"),
            ui.p(ui.tags.i(_safe_str(getattr(npc, "ideal", "-")))),
            ui.h4("Plot Hook"),
            ui.p(ui.tags.i(_safe_str(getattr(npc, "plothook", "-")))),
        ),
        prose_section(
            "Combat Actions",
            ui.h4(f"To hit: +{_safe_str(getattr(npc, 'to_hit_bonus', '-'))}"),
            _prose(getattr(npc, "simple_attacks", "-")),
            _prose(getattr(npc, "special_attack", "-")),
        ),
        prose_section(
            f"Spellcasting: {_safe_str(getattr(npc, 'spellcasting_ability', '-'))}",
            ui.h4(f"Spell Save DC: {_safe_str(getattr(npc, 'spell_save_dc', '-'))}"),
            ui.h4(f"To hit: +{_safe_str(getattr(npc, 'spell_attack_bonus', '-'))}"),
            _prose(getattr(npc, "spells", "-")),
            accent=True,
        ),
        prose_section("Martial Abilities", _prose(getattr(npc, "martial", "-"))),
        prose_section("Legendary", _prose(legendary)),
        prose_section("Lair", _prose(lair)),
        prose_section("Region", _prose(region)),
        prose_section("My Story", _prose(story_text)),
    ]

    return ui.div(
        {"class": "sheet note-lines"},
        ui.div(
            {"class": "npc-header"},
            ui.h2(_safe_str(getattr(npc, "name", "Unknown"))),
            ui.h2(_safe_str(getattr(npc, "title", ""))),
            ui.h1(f"{race}: {subrace}"),
            ui.h1(background),
        ),
        ui.div(
            {"class": "sheet-body"},
            ui.div(
                {"class": "sheet-rail"},
                ui.div({"class": "stat-flow"}, *stat_chips),
                scores_box,
                skills_box,
                saves_box,
                languages_box,
                movement_box,
                senses_box,
                resistances_box,
            ),
            ui.div(
                {"class": "sheet-main"},
                *prose_sections,
            ),
        ),
    )


RACES = sorted([race for race in race_weights.keys() if race])
RACES.insert(0, "Random")

SPECIES = sorted(species_dict.keys())
SPECIES.insert(0, "Random")

CLASSES = ["Random", *sorted(classes)]
BACKGROUNDS = ["Random", *sorted(backgrounds)]
ARCHETYPES = ["Random", *sorted(Archetypes)]


home_panel = ui.div(
    {"class": "main-content"},
    ui.h2("Welcome to Gen Legend"),
    ui.p("Generate legendary Characters and Non-Player Characters for your next adventure."),
    ui.div(
        {"id": "generator-tablet", "class": "tablet-wrapper"},
        ui.div(
            {"class": "tablet-controls"},
            ui.tags.button(
                {
                    "class": "tablet-nav prev fantasy-button",
                    "type": "button",
                    "aria-label": "Previous generator",
                    "style": "min-width:2.2em; min-height:2.2em; width:2.2em; height:2.2em; font-size:1.3em; line-height:1em; padding:0; display:inline-flex; align-items:center; justify-content:center;",
                },
                ui.HTML("<span aria-hidden='true' style='display:block;'>&#x2039;</span>"),
            ),
            ui.h3({"id": "tablet-title", "class": "tablet-title"}, "NPC Generator"),
            ui.tags.button(
                {
                    "class": "tablet-nav next fantasy-button",
                    "type": "button",
                    "aria-label": "Next generator",
                    "style": "min-width:2.2em; min-height:2.2em; width:2.2em; height:2.2em; font-size:1.3em; line-height:1em; padding:0; display:inline-flex; align-items:center; justify-content:center;",
                },
                ui.HTML("<span aria-hidden='true' style='display:block;'>&#x203A;</span>"),
            ),
        ),
        ui.div(
            {"class": "tablet-viewport"},
            ui.div(
                {"class": "tablet-rotator"},
                ui.tags.section(
                    {"class": "generator-panel", "data-title": "Character Generator"},
                    ui.h3("Generate Character"),
                    ui.input_select("char_species", "Species", SPECIES),
                    ui.input_select("char_class", "Class", CLASSES),
                    ui.input_select("char_background", "Background", BACKGROUNDS),
                    ui.div(
                        {"class": "tablet-actions"},
                        ui.input_action_button(
                            "btn_gen_char",
                            "Generate Character",
                            class_="fantasy-button",
                        ),
                    ),
                ),
                ui.tags.section(
                    {"class": "generator-panel is-active", "data-title": "NPC Generator"},
                    ui.h3("Generate Non Player Character"),
                    ui.div(
                        {"class": "number-input fantasy-input"},
                        ui.tags.button({"type": "button", "class": "minus fantasy-button fantasy-input"}, "-"),
                        ui.input_numeric("npc_level", "Level", value=5, min=1, max=100),
                        ui.tags.button({"type": "button", "class": "plus fantasy-button fantasy-input"}, "+"),
                    ),
                    ui.input_select("npc_race", "Race", RACES),
                    ui.input_select("npc_archetype", "Archetype", ARCHETYPES),
                    ui.div(
                        {"class": "tablet-actions"},
                        ui.input_action_button("btn_gen_npc", "Generate NPC", class_="fantasy-button"),
                        ui.input_action_button("btn_gen_list", "Generate 5 NPCs", class_="fantasy-button"),
                    ),
                ),
            ),
        ),
        ui.div({"class": "tablet-dots", "aria-label": "Generator navigation"}),
    ),
)


character_panel = ui.div(
    ui.h2({"class": "page-title"}, "Character Sheet"),
    ui.div(
        {"class": "character-reforge"},
        ui.div(
            {"class": "character-reforge-field character-reforge-field--species"},
            ui.input_select("char_sheet_species", "", SPECIES, selected="Random"),
        ),
        ui.div(
            {"class": "character-reforge-field character-reforge-field--class"},
            ui.input_select("char_sheet_class", "", CLASSES, selected="Random"),
        ),
        ui.div(
            {"class": "character-level-box"},
            ui.div({"class": "character-level-label"}, "Level"),
            ui.tags.div(
                {"class": "character-level-controls"},
                ui.input_action_button(
                    "btn_char_level_down",
                    "-",
                    class_="minus fantasy-button fantasy-input",
                    title="Level Down",
                    aria_label="Level Down",
                ),
                ui.input_action_button(
                    "btn_char_level_up",
                    "+",
                    class_="plus fantasy-button fantasy-input",
                    title="Level Up",
                    aria_label="Level Up",
                ),
            ),
        ),
        ui.div(
            {"class": "character-reforge-field character-reforge-field--background"},
            ui.input_select("char_sheet_background", "", BACKGROUNDS, selected="Random"),
        ),
        ui.div(
            {"class": "character-generate-wrap"},
            ui.input_action_button("btn_char_apply_selectors", "Generate", class_="fantasy-button"),
        ),
        ui.div(
            {"class": "character-share-wrap"},
            ui.input_action_button("btn_copy_char_link", "Share", class_="fantasy-button share-button"),
        ),
        ui.tags.span(
            {"id": "share-copy-status", "class": "share-copy-status character-reforge-status", "aria-live": "polite"}
        ),
    ),
    ui.hr(),
    ui.output_ui("character_result"),
)


npc_panel = ui.div(
    ui.h2({"class": "page-title"}, "NPC Sheet"),
    ui.div(
        {"class": "npc-button-selectors"},
        ui.input_action_button("btn_gen_npc_again", "Try Again", class_="fantasy-button"),
        ui.input_action_button("go_home_from_npc", "Back Home", class_="fantasy-button"),
    ),
    ui.hr(),
    ui.output_ui("npc_result"),
)


npclist_panel = ui.div(
    {"class": "main-content"},
    ui.h2({"class": "page-title"}, "Legendary NPC List"),
    ui.output_ui("npc_list_result"),
    ui.tags.br(),
    ui.input_action_button("btn_gen_list_again", "5 New NPCs", class_="fantasy-button"),
)


app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.meta(charset="utf-8"),
        ui.tags.meta(name="viewport", content="width=device-width, initial-scale=1"),
        ui.tags.title("Gen Legend (Shiny)"),
        ui.tags.link(rel="preconnect", href="https://fonts.googleapis.com"),
        ui.tags.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Cinzel:ital@0;1&display=swap", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+English", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Great+Primer:ital@0;1", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Great+Primer+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica:ital@0;1", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+English+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Spectral+SC:wght@400;600;700", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Eagle+Lake", rel="stylesheet"),
        ui.tags.style(BASE_STYLE),
        ui.tags.style(EXTRA_STYLE),
        ui.tags.script(ui.HTML(HOME_SCRIPT)),
        *loader_head_tags(),
        ui.tags.script(ui.HTML(MASONRY_SCRIPT)),
        ui.tags.script(ui.HTML("""
            (function() {
                function canonicalPath(pathname) {
                    var path = pathname || '/';
                    var marker = '/character/';
                    var idx = path.indexOf(marker);
                    if (idx >= 0) {
                        path = path.slice(0, idx + 1);
                    } else if (path.endsWith('/character')) {
                        path = path.slice(0, -'character'.length);
                    }
                    return path || '/';
                }

                function installHandler() {
                    if (typeof Shiny === 'undefined' || !Shiny.addCustomMessageHandler) return false;
                    if (window.__characterUrlHandlerInstalled) return true;
                    window.__characterUrlHandlerInstalled = true;

                    function setShareStatus(text, isError) {
                        var statusNode = document.getElementById('share-copy-status');
                        if (!statusNode) return;
                        statusNode.textContent = text || '';
                        statusNode.style.color = isError ? '#aa0a12' : '';
                        if (window.__shareStatusTimer) {
                            clearTimeout(window.__shareStatusTimer);
                        }
                        if (text) {
                            window.__shareStatusTimer = setTimeout(function() {
                                if (statusNode.textContent === text) {
                                    statusNode.textContent = '';
                                }
                            }, 2600);
                        }
                    }

                    function copyText(text) {
                        if (navigator.clipboard && navigator.clipboard.writeText) {
                            return navigator.clipboard.writeText(text);
                        }
                        return new Promise(function(resolve, reject) {
                            try {
                                var ta = document.createElement('textarea');
                                ta.value = text;
                                ta.style.position = 'fixed';
                                ta.style.left = '-9999px';
                                document.body.appendChild(ta);
                                ta.focus();
                                ta.select();
                                var ok = document.execCommand('copy');
                                document.body.removeChild(ta);
                                if (!ok) throw new Error('execCommand copy failed');
                                resolve();
                            } catch (err) {
                                reject(err);
                            }
                        });
                    }

                    function normalizeShareHash(rawValue) {
                        if (rawValue == null) return '';
                        var value = String(rawValue).trim();
                        if (!value) return '';
                        if (/^[a-z]+:\\/\\//i.test(value)) {
                            try {
                                value = new URL(value).hash || '';
                            } catch (_) {
                                return '';
                            }
                        }
                        if (value.startsWith('#')) value = value.slice(1);
                        if (!value) return '';
                        if (value[0] !== '/') {
                            try {
                                var decoded = decodeURIComponent(value);
                                if (decoded && decoded !== value) value = decoded;
                            } catch (_) {
                                // keep original
                            }
                        }
                        value = value.replace(/^\\/+/, '');
                        if (value.toLowerCase().startsWith('character/')) {
                            value = value.slice('character/'.length);
                        }
                        var parts = value.split('/').filter(Boolean);
                        if (parts.length < 6) return '';
                        return '#/' + parts.slice(0, 6).join('/');
                    }

                    function extractHashFromPath(pathname) {
                        var path = pathname || '';
                        var marker = '/character/';
                        var idx = path.indexOf(marker);
                        if (idx < 0) return '';
                        return '#/' + path.slice(idx + marker.length).replace(/^\\/+/, '');
                    }

                    function hashFromQuery(search) {
                        try {
                            var params = new URLSearchParams(search || '');
                            var seed = params.get('seed');
                            if (!seed) return '';
                            var level = params.get('level') || '1';
                            var species = params.get('species') || 'random';
                            var background = params.get('background') || 'random';
                            var charClass = params.get('char_class') || 'random';
                            var gender = params.get('gender') || 'random';
                            return '#/' + [
                                encodeURIComponent(level),
                                encodeURIComponent(species),
                                encodeURIComponent(background),
                                encodeURIComponent(charClass),
                                encodeURIComponent(gender),
                                encodeURIComponent(seed)
                            ].join('/');
                        } catch (_) {
                            return '';
                        }
                    }

                    function buildShareUrl() {
                        var hash = normalizeShareHash(window.location.hash || '');
                        if (!hash && window.__characterShareHash) {
                            hash = normalizeShareHash(window.__characterShareHash);
                        }
                        if (!hash) {
                            hash = normalizeShareHash(extractHashFromPath(window.location.pathname));
                        }
                        if (!hash) {
                            hash = normalizeShareHash(hashFromQuery(window.location.search));
                        }
                        if (!hash) return '';
                        var basePath = canonicalPath(window.location.pathname);
                        var origin = window.location.origin || '';
                        return (origin ? origin : '') + basePath + hash;
                    }

                    function fallbackCopyPrompt(url) {
                        try {
                            window.prompt('Copy this link:', url);
                        } catch (_) {
                            // ignore
                        }
                    }

                    Shiny.addCustomMessageHandler('update_character_url', function(msg) {
                        if (!msg) return;
                        var base = canonicalPath(window.location.pathname);
                        var currentHash = window.location.hash || '';
                        var nextUrl = null;
                        if (typeof msg.hash === 'string' && msg.hash.length > 0) {
                            var nextHash = normalizeShareHash(msg.hash) || (msg.hash.startsWith('#') ? msg.hash : ('#' + msg.hash));
                            window.__characterShareHash = nextHash;
                            nextUrl = base + nextHash;
                        } else if (typeof msg.path === 'string' && msg.path.length > 0) {
                            var pathSuffix = msg.path.replace(/^\\/+/, '');
                            nextUrl = base + pathSuffix + currentHash;
                        } else if (typeof msg.query === 'string') {
                            nextUrl = base + msg.query + currentHash;
                        }
                        if (!nextUrl) return;
                        if (window.history && window.history.replaceState) {
                            window.history.replaceState(null, '', nextUrl);
                        } else {
                            window.location.href = nextUrl;
                        }
                    });

                    Shiny.addCustomMessageHandler('set_share_hash', function(msg) {
                        var incoming = msg && typeof msg.hash === 'string' ? msg.hash : '';
                        var normalized = normalizeShareHash(incoming);
                        if (normalized) {
                            window.__characterShareHash = normalized;
                        }
                    });

                    document.addEventListener('click', function(ev) {
                        var target = ev.target;
                        var btn = target && target.closest ? target.closest('#btn_copy_char_link') : null;
                        if (!btn) return;
                        var shareUrl = buildShareUrl();
                        if (!shareUrl) {
                            setShareStatus('Generate a character first.', true);
                            return;
                        }
                        copyText(shareUrl).then(function() {
                            setShareStatus('Link copied.', false);
                        }).catch(function() {
                            setShareStatus('Clipboard blocked. Copy from dialog.', true);
                            fallbackCopyPrompt(shareUrl);
                        });
                    });
                    return true;
                }

                if (!installHandler()) {
                    var tries = 0;
                    var maxTries = 80;
                    var timer = setInterval(function() {
                        tries += 1;
                        if (installHandler() || tries >= maxTries) {
                            clearInterval(timer);
                        }
                    }, 100);
                    window.addEventListener('shiny:connected', installHandler, { once: true });
                }
            })();
        """)),
    ),
    loader_panel(),
    ui.tags.header(
        ui.h1(ui.tags.a({"href": "#", "style": "color: inherit; text-decoration: none;"}, "Gen Legend")),
        ui.tags.div(
            {"class": "header-actions"},
            ui.input_action_button("go_home", "Home", class_="fantasy-button"),
            ui.input_action_button("go_character", "Character", class_="fantasy-button"),
            ui.input_action_button("go_npc", "NPC", class_="fantasy-button"),
            ui.input_action_button("go_npclist", "NPC List", class_="fantasy-button"),
        ),
    ),
    ui.div(
        {"class": "main-wrap"},
        ui.div(
            {"class": "container"},
            ui.output_ui("active_page"),
        ),
    ),
    ui.tags.footer(
        {
            "style": "background: #231c27; color: #f6d67c; padding: 1.15em 0; text-align: center; font-size: 1.03em; margin-top: 2em; border-top: 3px solid #786110; letter-spacing: 0.01em;"
        },
        ui.tags.a(
            "About Us",
            href="https://github.com/JulTob/DnD#readme",
            target="_blank",
            rel="noopener",
            style="color: #f6d67c; text-decoration: none; font-weight: bold; margin: 0 1.5em;",
        ),
        ui.tags.span("|", style="margin: 0 1.5em;"),
        ui.tags.a(
            "Lore Wiki",
            href="https://github.com/JulTob/DnD/wiki",
            target="_blank",
            rel="noopener",
            style="color: #f6d67c; text-decoration: none; font-weight: bold; margin: 0 1.5em;",
        ),
        ui.tags.span("|", style="margin: 0 1.5em;"),
        ui.tags.span(
            "By ",
            ui.tags.a(
                "Julio Toboso",
                href="https://github.com/JulTob",
                target="_blank",
                rel="noopener",
                style="color: #f6d67c; text-decoration: underline dashed; font-weight: bold;",
            ),
            style="color: #f6d67c;",
        ),
    ),
)



def server(input, output, session):
    page_state = reactive.value("home")
    character_state = reactive.value(None)
    character_params_state = reactive.value(None)
    character_error = reactive.value(None)
    npc_state = reactive.value(None)
    npc_error = reactive.value(None)
    npc_list_state = reactive.value([])
    npc_list_error = reactive.value(None)
    initial_character_url_processed = reactive.value(False)

    def show_page(page: str) -> None:
        page_state.set(page)

    def _send_custom_message(message_type: str, message_data: dict[str, Any]) -> None:
        message = session.send_custom_message(message_type, message_data)

        if inspect.isawaitable(message):
            asyncio.create_task(message)

    def _set_loader(action: str) -> None:
        _send_custom_message("set_loader", {"action": action})

    def _clean_character_param(value: Any) -> str | None:
        if value is None:
            return None
        text = str(value).strip()
        if not text or text == "Random":
            return None
        return text

    def _character_params_from_data(
        data: dict[str, Any] | None,
        fallback: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        base = fallback or {}
        payload = data or {}
        level_value = payload.get("Level", base.get("level", 1))
        level = max(1, min(20, _safe_int(level_value, 1)))
        seed_value = payload.get("Seed", payload.get("seed", base.get("seed")))
        try:
            seed = int(seed_value) if seed_value is not None else None
        except (TypeError, ValueError):
            seed = None
        return {
            "species": _clean_character_param(payload.get("Species", base.get("species"))),
            "char_class": _clean_character_param(payload.get("Class", base.get("char_class"))),
            "background": _clean_character_param(payload.get("Background", base.get("background"))),
            "level": level,
            "gender": _clean_character_param(payload.get("Gender", base.get("gender"))),
            "seed": seed,
        }

    def _apply_character_form_defaults(params: dict[str, Any]) -> None:
        species = params.get("species") if params.get("species") in SPECIES else "Random"
        char_class = params.get("char_class") if params.get("char_class") in CLASSES else "Random"
        background = params.get("background") if params.get("background") in BACKGROUNDS else "Random"
        ui.update_select("char_species", selected=species)
        ui.update_select("char_class", selected=char_class)
        ui.update_select("char_background", selected=background)
        _apply_character_sheet_defaults(params)

    def _apply_character_sheet_defaults(params: dict[str, Any]) -> None:
        species = params.get("species") if params.get("species") in SPECIES else "Random"
        char_class = params.get("char_class") if params.get("char_class") in CLASSES else "Random"
        background = params.get("background") if params.get("background") in BACKGROUNDS else "Random"
        ui.update_select("char_sheet_species", selected=species)
        ui.update_select("char_sheet_class", selected=char_class)
        ui.update_select("char_sheet_background", selected=background)

    def _push_character_url(params: dict[str, Any]) -> None:
        if params.get("seed") is None:
            return
        url_hash = character_params_to_hash(params)
        if url_hash:
            _send_custom_message("update_character_url", {"hash": url_hash})
            _send_custom_message("set_share_hash", {"hash": url_hash})

    def _generate_character_from_params(
        params: dict[str, Any],
        *,
        show_character_page: bool = True,
        sync_form_defaults: bool = False,
    ) -> None:
        try:
            character = summon_character(
                species=params.get("species"),
                char_class=params.get("char_class"),
                background=params.get("background"),
                level=max(1, min(20, _safe_int(params.get("level"), 1))),
                gender=params.get("gender"),
                seed=params.get("seed"),
            )
            data = character.to_dict()
            character_state.set(data)
            character_error.set(None)
            canonical = _character_params_from_data(data, fallback=params)
            character_params_state.set(canonical)
            _apply_character_sheet_defaults(canonical)
            if sync_form_defaults:
                _apply_character_form_defaults(canonical)
            _push_character_url(canonical)
            if show_character_page:
                show_page("character")
        except Exception as exc:
            character_error.set(str(exc))
            if show_character_page:
                show_page("character")
        finally:
            _set_loader("hide")

    @reactive.effect
    def _init_character_from_url() -> None:
        if initial_character_url_processed():
            return
        pathname_fn = getattr(session.clientdata, "url_pathname", None)
        pathname = pathname_fn() if callable(pathname_fn) else None
        search = session.clientdata.url_search()
        hash_fn = getattr(session.clientdata, "url_hash", None)
        hash_value = hash_fn() if callable(hash_fn) else None
        params = parse_character_params_from_url(pathname, search, hash_value)
        if params is None:
            initial_character_url_processed.set(True)
            return
        initial_character_url_processed.set(True)
        _set_loader("show")
        _generate_character_from_params(
            params,
            show_character_page=True,
            sync_form_defaults=True,
        )

    @reactive.effect
    @reactive.event(input.go_home, input.go_home_from_npc)
    def _go_home() -> None:
        show_page("home")

    @reactive.effect
    @reactive.event(input.go_character)
    def _go_character() -> None:
        initial_character_url_processed.set(True)
        _set_loader("show")
        _generate_character_from_params(
            {"level": 1, "seed": randint(0, 2**16)},
            show_character_page=True,
        )

    @reactive.effect
    @reactive.event(input.go_npc)
    def _go_npc() -> None:
        show_page("npc")

    @reactive.effect
    @reactive.event(input.go_npclist)
    def _go_npclist() -> None:
        show_page("npclist")

    @reactive.effect
    @reactive.event(input.btn_gen_char)
    def _generate_character_from_form() -> None:
        initial_character_url_processed.set(True)
        _set_loader("show")
        _generate_character_from_params(
            {
                "species": _selection_or_none(input.char_species()),
                "char_class": _selection_or_none(input.char_class()),
                "background": _selection_or_none(input.char_background()),
                "level": 1,
                "seed": randint(0, 2**16),
            },
            show_character_page=True,
        )

    @reactive.effect
    @reactive.event(input.btn_char_level_down)
    def _level_character_down() -> None:
        initial_character_url_processed.set(True)
        current = character_params_state() or _character_params_from_data(character_state())
        current_level = max(1, min(20, _safe_int(current.get("level"), 1)))
        next_level = max(1, current_level - 1)
        if next_level == current_level or current.get("seed") is None:
            _set_loader("hide")
            return
        next_params = dict(current)
        next_params["level"] = next_level
        _set_loader("show")
        _generate_character_from_params(next_params, show_character_page=False)

    @reactive.effect
    @reactive.event(input.btn_char_level_up)
    def _level_character_up() -> None:
        initial_character_url_processed.set(True)
        current = character_params_state() or _character_params_from_data(character_state())
        current_level = max(1, min(20, _safe_int(current.get("level"), 1)))
        next_level = min(20, current_level + 1)
        if next_level == current_level or current.get("seed") is None:
            _set_loader("hide")
            return
        next_params = dict(current)
        next_params["level"] = next_level
        _set_loader("show")
        _generate_character_from_params(next_params, show_character_page=False)

    @reactive.effect
    @reactive.event(input.btn_char_apply_selectors)
    def _apply_character_selectors() -> None:
        initial_character_url_processed.set(True)
        current = character_params_state() or _character_params_from_data(character_state())
        level = max(1, min(20, _safe_int(current.get("level"), 1)))
        params = {
            "species": _selection_or_none(input.char_sheet_species()),
            "char_class": _selection_or_none(input.char_sheet_class()),
            "background": _selection_or_none(input.char_sheet_background()),
            "gender": current.get("gender"),
            "level": level,
            "seed": randint(0, 2**16),
        }
        _set_loader("show")
        _generate_character_from_params(params, show_character_page=True)

    @reactive.effect
    @reactive.event(input.btn_gen_npc)
    def _generate_npc_from_form() -> None:
        selected_race = input.npc_race()
        selected_archetype = input.npc_archetype()
        level = _safe_int(input.npc_level(), 5)
        _set_loader("show")

        try:
            npc = summon_npc(
                race=selected_race,
                archetype=selected_archetype,
                level=level,
                seed=randint(1, 2**16),
            )
            npc_state.set(npc)
            npc_error.set(None)
            show_page("npc")
        except Exception as exc:
            npc_error.set(str(exc))
            show_page("npc")
        finally:
            _set_loader("hide")

    @reactive.effect
    @reactive.event(input.btn_gen_npc_again)
    def _generate_npc_again() -> None:
        current = npc_state()
        _set_loader("show")

        try:
            if current is None:
                npc = summon_npc(level=_safe_int(input.npc_level(), 5), seed=randint(1, 2**16))
            else:
                npc = summon_npc(
                    race=getattr(current, "race", None),
                    archetype=getattr(current, "archetype", None),
                    level=_safe_int(getattr(current, "level", 1), 1),
                    seed=randint(1, 2**16),
                )
            npc_state.set(npc)
            npc_error.set(None)
        except Exception as exc:
            npc_error.set(str(exc))
        finally:
            _set_loader("hide")

    @reactive.effect
    @reactive.event(input.btn_gen_list, input.btn_gen_list_again)
    def _generate_npc_list() -> None:
        race_in = input.npc_race()
        archetype_in = input.npc_archetype()
        seed = randint(0, 16383)
        _set_loader("show")

        try:
            npcs = []
            for idx in range(5):
                current_race = race_in
                current_archetype = archetype_in

                if current_race == "Random":
                    current_race = choice(list(race_weights.keys()))
                if current_archetype == "Random":
                    current_archetype = choice(Archetypes)

                npcs.append(
                    NPC(
                        race=current_race,
                        archetype=current_archetype,
                        lvl=randint(1, 20),
                        seed=seed + idx,
                        light=True,
                    )
                )

            npc_list_state.set(npcs)
            npc_list_error.set(None)
            show_page("npclist")
        except Exception as exc:
            npc_list_error.set(str(exc))
            show_page("npclist")
        finally:
            _set_loader("hide")

    @output
    @render.ui
    def active_page() -> ui.Tag:
        pages = {
            "home": home_panel,
            "character": character_panel,
            "npc": npc_panel,
            "npclist": npclist_panel,
        }
        return pages.get(page_state(), home_panel)

    @output
    @render.ui
    def character_result() -> ui.Tag:
        err = character_error()
        if err:
            return ui.div({"class": "fallback-card"}, ui.h3("Character generation failed"), ui.p(err))

        data = character_state()
        if not data:
            return ui.div({"class": "fallback-card"}, ui.p("Generate a character from Home."))

        return build_character_sheet(data)

    @output
    @render.ui
    def npc_result() -> ui.Tag:
        err = npc_error()
        if err:
            return ui.div({"class": "fallback-card"}, ui.h3("NPC generation failed"), ui.p(err))

        npc = npc_state()
        if npc is None:
            return ui.div({"class": "fallback-card"}, ui.p("Generate an NPC from Home."))

        return build_npc_sheet(npc)

    @output
    @render.ui
    def npc_list_result() -> ui.Tag:
        err = npc_list_error()
        if err:
            return ui.div({"class": "fallback-card"}, ui.h3("NPC list generation failed"), ui.p(err))

        npcs = npc_list_state()
        if not npcs:
            return ui.div({"class": "fallback-card"}, ui.p("Generate 5 NPCs from Home."))

        rows = []
        for npc in npcs:
            rows.append(
                ui.tags.a(
                    ui.h1(ui.tags.i(_safe_str(getattr(npc, "name", "Unknown")))),
                    ui.h2(_safe_str(getattr(npc, "title", ""))),
                    ui.h3(f"{_safe_str(getattr(npc, 'race', '-'))} {_safe_str(getattr(npc, 'archetype', '-'))}"),
                    href="#",
                )
            )

        return ui.div(
            {"class": "npc-list", "style": "display: flex; flex-direction: column; gap: 1.3em; font-size: 1.1em; padding-top: 1em;"},
            *rows,
        )


def _canonical_base_path(pathname: str) -> str:
    path = pathname or "/"
    marker = "/character/"
    idx = path.find(marker)
    if idx >= 0:
        path = path[: idx + 1]
    elif path.endswith("/character"):
        path = path[: -len("character")]
    return path or "/"


async def _send_redirect(send, location: str, status: int = 307) -> None:
    headers = [
        (b"location", location.encode("utf-8")),
        (b"cache-control", b"no-store"),
    ]
    await send({"type": "http.response.start", "status": status, "headers": headers})
    await send({"type": "http.response.body", "body": b""})


class CharacterPathRedirectASGI:
    """
    Accept legacy/shareable /character/... paths and redirect to canonical hash URLs,
    so direct opens don't hit a 404 before Shiny starts.
    """

    def __init__(self, wrapped_app):
        self.wrapped_app = wrapped_app

    async def __call__(self, scope, receive, send):
        if scope.get("type") == "http" and (scope.get("method") or "GET").upper() == "GET":
            path = str(scope.get("path") or "")
            if path.endswith("/character"):
                await _send_redirect(send, _canonical_base_path(path), status=307)
                return

            if "/character/" in path:
                params = parse_character_params_from_path(path)
                if params is not None:
                    url_hash = character_params_to_hash(params)
                    if url_hash:
                        target = f"{_canonical_base_path(path)}{url_hash}"
                        await _send_redirect(send, target, status=307)
                        return
                # If malformed character path, still land users on app instead of raw 404.
                await _send_redirect(send, _canonical_base_path(path), status=307)
                return

        await self.wrapped_app(scope, receive, send)


_shiny_app = App(app_ui, server, static_assets={"/static": Path(__file__).parent / "app" / "static"})
app = CharacterPathRedirectASGI(_shiny_app)
