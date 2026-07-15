"""Shiny summon-loader: markup and client script."""

from __future__ import annotations

import json
from typing import Any

from shiny import ui

from AtlasVenustas.Lodge_of_Symbols import (
    PLANET_SYMBOLS,
    SOL_SYMBOLS,
    symbols_for_planets,
    symbols_for_sol,
)

ACTION_IDS: tuple[str, ...] = (
    "btn_gen_char",
    "btn_char_apply_selectors",
    "btn_char_level_down",
    "btn_char_level_up",
    "btn_gen_npc",
    "btn_gen_npc_again",
    "btn_gen_list",
    "btn_gen_list_again",
)

STATUS_LINES: tuple[str, ...] = (
    "Summoning your legend...",
    "Inscribing dice runes...",
    "Binding fate...",
    "Consulting the oracle...",
    "Polishing weapons...",
    "Crafting armor...",
    "Infusing potions...",
    "Awakening powers... ",
    "Joining guild...",
    "Writting tragic past...",
    "Finding tavern...",
    "Setting the stars to guide party...",
    "Assembling party...",
    "Enfuriating goblins...",
    "Wake up, traveler...",
    "The journey begins...",
  )

AUTO_HIDE_MS = 12_000


def loader_panel() -> ui.Tag:
    """The #loader overlay (sun, orbits, status message)."""
    return ui.div(
        {"id": "loader", "aria-live": "polite", "aria-busy": "true"},
        ui.div({"class": "sol-layer"}),
        ui.div({"class": "orbit-layer orbit1"}),
        ui.div({"class": "orbit-layer orbit2"}),
        ui.div({"class": "orbit-layer orbit3"}),
        ui.div({"id": "loader-message"}, "Summoning your legend..."),
    )


def loader_script(
    *,
    sol_symbols: tuple[str, ...] | None = None,
    planet_symbols: tuple[str, ...] | None = None,
    species: str | None = None,
    char_class: str | None = None,
) -> str:
    """Return the loader IIFE; symbol pools come from the Lodge by default."""
    sol = sol_symbols or symbols_for_sol(species=species, char_class=char_class)
    planets = planet_symbols or symbols_for_planets(species=species, char_class=char_class)
    sol_json = json.dumps(list(sol), ensure_ascii=False)
    planet_json = json.dumps(list(planets), ensure_ascii=False)
    action_ids_json = json.dumps(list(ACTION_IDS))
    status_lines_json = json.dumps(list(STATUS_LINES), ensure_ascii=False)

    return f"""(() => {{
  const AUTO_HIDE_MS = {AUTO_HIDE_MS};
  const ACTION_IDS = new Set({action_ids_json});
  const STATUS_LINES = {status_lines_json};
  const SOL_SYMBOLS = {sol_json};
  const PLANET_SYMBOLS = {planet_json};

  let statusTicker = null;
  let typingTicker = null;
  let autoHideTimer = null;
  let statusIndex = 0;

  function randomFrom(list) {{
    return list[Math.floor(Math.random() * list.length)];
  }}

  function getLoader() {{
    return document.getElementById('loader');
  }}

  function getMessageNode() {{
    return document.getElementById('loader-message');
  }}

  function populatePlanets() {{
    const loader = getLoader();
    if (!loader) return;

    const sun = loader.querySelector('.sol-layer');
    if (sun) sun.textContent = randomFrom(SOL_SYMBOLS);

    loader.querySelectorAll('.orbit-layer').forEach((orbit, orbitIndex) => {{
      orbit.innerHTML = '';
      const count = orbitIndex + 3;
      const radius = Math.max(20, orbit.offsetWidth / 2);
      for (let i = 0; i < count; i += 1) {{
        const angle = (360 * i) / count;
        const planet = document.createElement('div');
        planet.className = 'planet';
        planet.textContent = randomFrom(PLANET_SYMBOLS);
        planet.style.transform = `rotate(${{angle}}deg) translate(${{radius}}px)`;
        orbit.appendChild(planet);
      }}
    }});
  }}

  function typeLine(text) {{
    const node = getMessageNode();
    if (!node) return;
    if (typingTicker) clearInterval(typingTicker);
    let i = 0;
    node.textContent = '';
    typingTicker = setInterval(() => {{
      i += 1;
      node.textContent = text.slice(0, i);
      if (i >= text.length) {{
        clearInterval(typingTicker);
        typingTicker = null;
      }}
    }}, 30);
  }}

  function startStatus() {{
    if (statusTicker) clearInterval(statusTicker);
    typeLine(STATUS_LINES[statusIndex % STATUS_LINES.length]);
    statusTicker = setInterval(() => {{
      statusIndex += 1;
      typeLine(STATUS_LINES[statusIndex % STATUS_LINES.length]);
    }}, 2200);
  }}

  function stopStatus() {{
    if (statusTicker) {{
      clearInterval(statusTicker);
      statusTicker = null;
    }}
    if (typingTicker) {{
      clearInterval(typingTicker);
      typingTicker = null;
    }}
  }}

  function showLoader() {{
    const loader = getLoader();
    if (!loader) return;
    loader.classList.add('show');
    loader.style.pointerEvents = 'none';
    populatePlanets();
    startStatus();
    if (autoHideTimer) clearTimeout(autoHideTimer);
    autoHideTimer = setTimeout(() => {{
      hideLoader();
    }}, AUTO_HIDE_MS);
  }}

  function hideLoader() {{
    const loader = getLoader();
    if (!loader) return;
    loader.classList.remove('show');
    stopStatus();
    if (autoHideTimer) {{
      clearTimeout(autoHideTimer);
      autoHideTimer = null;
    }}
  }}

  window.summonLoader = {{ show: showLoader, hide: hideLoader }};

  document.addEventListener('click', (event) => {{
    const target = event.target.closest('button, input[type="submit"], [data-show-loader]');
    if (!target) return;
    if (target.hasAttribute('data-show-loader') || ACTION_IDS.has(target.id || '')) {{
      showLoader();
    }}
  }}, true);

  function installShinyLoaderHandler() {{
    if (typeof Shiny === 'undefined' || !Shiny.addCustomMessageHandler) return false;
    if (window.__summonLoaderHandlerInstalled) return true;
    window.__summonLoaderHandlerInstalled = true;
    Shiny.addCustomMessageHandler('set_loader', function(msg) {{
      if (msg && msg.action === 'show') {{
        showLoader();
      }} else {{
        hideLoader();
      }}
    }});
    return true;
  }}

  function installOutputObservers() {{
    const outputIds = ['character_result', 'npc_result', 'npc_list_result'];
    outputIds.forEach((id) => {{
      const root = document.getElementById(id);
      if (!root || root.__loaderObserverInstalled) return;
      root.__loaderObserverInstalled = true;
      const observer = new MutationObserver(() => {{
        hideLoader();
      }});
      observer.observe(root, {{ childList: true, subtree: true }});
    }});
  }}

  if (!installShinyLoaderHandler()) {{
    let tries = 0;
    const timer = setInterval(() => {{
      tries += 1;
      if (installShinyLoaderHandler() || tries >= 80) {{
        clearInterval(timer);
      }}
    }}, 100);
    window.addEventListener('shiny:connected', installShinyLoaderHandler, {{ once: true }});
  }}

  installOutputObservers();
  document.addEventListener('shiny:idle', () => {{
    hideLoader();
    installOutputObservers();
  }});
  document.addEventListener('shiny:disconnected', hideLoader);
  window.addEventListener('hashchange', hideLoader);

  window.addEventListener('load', hideLoader);
}})();
"""


def loader_head_tags(**symbol_options: Any) -> list[ui.Tag]:
    """Script tag(s) for the summon loader."""
    return [ui.tags.script(ui.HTML(loader_script(**symbol_options)))]


if __name__ == "__main__":
    script = loader_script()
    assert "summonLoader" in script
    assert "SOL_SYMBOLS" in script
    assert all(sym in script for sym in SOL_SYMBOLS[:3])
    panel = loader_panel()
    assert panel is not None
    tags = loader_head_tags()
    assert len(tags) == 1
    print("Kit_of_Loader self-test passed.")
