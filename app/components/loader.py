"""Shiny summon-loader markup and client script."""

from __future__ import annotations

import json
from typing import Any

from shiny import ui

from app.components.symbols import PLANET_SYMBOLS
from app.components.symbols import SOL_SYMBOLS
from app.components.symbols import symbols_for_planets
from app.components.symbols import symbols_for_sol


_LOADER_SCRIPT_TAIL = ';\n\n  let statusTicker = null;\n  let typingTicker = null;\n  let autoHideTimer = null;\n  let statusIndex = 0;\n\n  function randomFrom(list) {\n    return list[Math.floor(Math.random() * list.length)];\n  }\n\n  function getLoader() {\n    return document.getElementById(\'loader\');\n  }\n\n  function getMessageNode() {\n    return document.getElementById(\'loader-message\');\n  }\n\n  function populatePlanets() {\n    const loader = getLoader();\n    if (!loader) return;\n\n    const sun = loader.querySelector(\'.sol-layer\');\n    if (sun) sun.textContent = randomFrom(SOL_SYMBOLS);\n\n    loader.querySelectorAll(\'.orbit-layer\').forEach((orbit, orbitIndex) => {\n      // Planets live inside the inner .orbit-ring so the spin animation\n      // doesn\'t clash with the outer flip-y transform on .orbit-layer.\n      const ring = orbit.querySelector(\'.orbit-ring\');\n      if (!ring) return;\n      ring.innerHTML = \'\';\n      const count = orbitIndex + 3;\n      const radius = Math.max(20, orbit.offsetWidth / 2);\n      for (let i = 0; i < count; i += 1) {\n        const angle = (360 * i) / count;\n        const planet = document.createElement(\'div\');\n        planet.className = \'planet\';\n        planet.textContent = randomFrom(PLANET_SYMBOLS);\n        planet.style.transform = `rotate(${angle}deg) translate(${radius}px)`;\n        ring.appendChild(planet);\n      }\n    });\n  }\n\n  function typeLine(text) {\n    const node = getMessageNode();\n    if (!node) return;\n    if (typingTicker) clearInterval(typingTicker);\n    let i = 0;\n    node.textContent = \'\';\n    typingTicker = setInterval(() => {\n      i += 1;\n      node.textContent = text.slice(0, i);\n      if (i >= text.length) {\n        clearInterval(typingTicker);\n        typingTicker = null;\n      }\n    }, 30);\n  }\n\n  function startStatus() {\n    if (statusTicker) clearInterval(statusTicker);\n    typeLine(STATUS_LINES[statusIndex % STATUS_LINES.length]);\n    statusTicker = setInterval(() => {\n      statusIndex += 1;\n      typeLine(STATUS_LINES[statusIndex % STATUS_LINES.length]);\n    }, 2200);\n  }\n\n  // ── Orbit coin-flip scheduler ────────────────────────────────────────────\n  // Every discrete 1-5 seconds, pick a random orbit and flip it 180° on Y.\n  let flipTimer = null;\n\n  function scheduleNextFlip() {\n    const delaySec = Math.floor(Math.random() * 5) + 1;  // 1,2,3,4 or 5 s\n    flipTimer = setTimeout(() => {\n      const loader = getLoader();\n      if (!loader) return;\n      const orbits = Array.from(loader.querySelectorAll(\'.orbit-layer\'));\n      if (orbits.length === 0) return;\n      const target = orbits[Math.floor(Math.random() * orbits.length)];\n      target.classList.toggle(\'flip-y\');\n      scheduleNextFlip();\n    }, delaySec * 1000);\n  }\n\n  function startOrbitFlips() {\n    if (flipTimer) clearTimeout(flipTimer);\n    scheduleNextFlip();\n  }\n\n  function stopOrbitFlips() {\n    if (flipTimer) {\n      clearTimeout(flipTimer);\n      flipTimer = null;\n    }\n    // Reset all orbits to unflipped state\n    const loader = getLoader();\n    if (loader) loader.querySelectorAll(\'.orbit-layer\').forEach(o => o.classList.remove(\'flip-y\'));\n  }\n  // ────────────────────────────────────────────────────────────────────────\n\n  function stopStatus() {\n    if (statusTicker) {\n      clearInterval(statusTicker);\n      statusTicker = null;\n    }\n    if (typingTicker) {\n      clearInterval(typingTicker);\n      typingTicker = null;\n    }\n  }\n\n  function showLoader() {\n    const loader = getLoader();\n    if (!loader) return;\n    loader.classList.add(\'show\');\n    loader.style.pointerEvents = \'none\';\n    populatePlanets();\n    startStatus();\n    startOrbitFlips();\n    if (autoHideTimer) clearTimeout(autoHideTimer);\n    autoHideTimer = setTimeout(() => {\n      hideLoader();\n    }, AUTO_HIDE_MS);\n  }\n\n  function hideLoader() {\n    const loader = getLoader();\n    if (!loader) return;\n    loader.classList.remove(\'show\');\n    stopStatus();\n    stopOrbitFlips();\n    if (autoHideTimer) {\n      clearTimeout(autoHideTimer);\n      autoHideTimer = null;\n    }\n  }\n\n  window.summonLoader = { show: showLoader, hide: hideLoader };\n\n  document.addEventListener(\'click\', (event) => {\n    const target = event.target.closest(\'button, input[type="submit"], [data-show-loader]\');\n    if (!target) return;\n    if (target.hasAttribute(\'data-show-loader\') || ACTION_IDS.has(target.id || \'\')) {\n      showLoader();\n    }\n  }, true);\n\n  function installShinyLoaderHandler() {\n    if (typeof Shiny === \'undefined\' || !Shiny.addCustomMessageHandler) return false;\n    if (window.__summonLoaderHandlerInstalled) return true;\n    window.__summonLoaderHandlerInstalled = true;\n    Shiny.addCustomMessageHandler(\'set_loader\', function(msg) {\n      if (msg && msg.action === \'show\') {\n        showLoader();\n      } else {\n        hideLoader();\n      }\n    });\n    return true;\n  }\n\n  function installOutputObservers() {\n    const outputIds = [\'character_result\', \'npc_result\', \'npc_list_result\'];\n    outputIds.forEach((id) => {\n      const root = document.getElementById(id);\n      if (!root || root.__loaderObserverInstalled) return;\n      root.__loaderObserverInstalled = true;\n      const observer = new MutationObserver(() => {\n        hideLoader();\n      });\n      observer.observe(root, { childList: true, subtree: true });\n    });\n  }\n\n  if (!installShinyLoaderHandler()) {\n    let tries = 0;\n    const timer = setInterval(() => {\n      tries += 1;\n      if (installShinyLoaderHandler() || tries >= 80) {\n        clearInterval(timer);\n      }\n    }, 100);\n    window.addEventListener(\'shiny:connected\', installShinyLoaderHandler, { once: true });\n  }\n\n  installOutputObservers();\n  document.addEventListener(\'shiny:idle\', () => {\n    hideLoader();\n    installOutputObservers();\n  });\n  document.addEventListener(\'shiny:disconnected\', hideLoader);\n  window.addEventListener(\'hashchange\', hideLoader);\n\n  window.addEventListener(\'load\', hideLoader);\n})();\n'


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
AUTO_HIDE_MS = 12000


def loader_panel(
        ) -> ui.Tag:
    """Return the loader overlay with its sun, orbits, and status line."""
    return ui.div(
            {
                "id": "loader",
                "aria-live": "polite",
                "aria-busy": "true",
                },
            ui.div(
                    {"class": "sol-layer"}
                    ),
            ui.div(
                    {"class": "orbit-layer orbit1"},
                    ui.div(
                            {"class": "orbit-ring"}
                            ),
                    ),
            ui.div(
                    {"class": "orbit-layer orbit2"},
                    ui.div(
                            {"class": "orbit-ring"}
                            ),
                    ),
            ui.div(
                    {"class": "orbit-layer orbit3"},
                    ui.div(
                            {"class": "orbit-ring"}
                            ),
                    ),
            ui.div(
                    {"id": "loader-message"},
                    "Summoning your legend...",
                    ),
            )


def loader_script(
        *,
        sol_symbols: tuple[str, ...] | None = None,
        planet_symbols: tuple[str, ...] | None = None,
        species: str | None = None,
        char_class: str | None = None,
        ) -> str:
    """Return the loader IIFE, using themed symbol pools by default."""
    sol = sol_symbols or symbols_for_sol(
            species=species,
            char_class=char_class,
            )
    planets = planet_symbols or symbols_for_planets(
            species=species,
            char_class=char_class,
            )
    sol_json = json.dumps(
            list(sol),
            ensure_ascii=False,
            )
    planet_json = json.dumps(
            list(planets),
            ensure_ascii=False,
            )
    action_ids_json = json.dumps(
            list(ACTION_IDS)
            )
    status_lines_json = json.dumps(
            list(STATUS_LINES),
            ensure_ascii=False,
            )
    return (
            "(() => {\n  const AUTO_HIDE_MS = "
            + str(AUTO_HIDE_MS)
            + ";\n  const ACTION_IDS = new Set("
            + action_ids_json
            + ");\n  const STATUS_LINES = "
            + status_lines_json
            + ";\n  const SOL_SYMBOLS = "
            + sol_json
            + ";\n  const PLANET_SYMBOLS = "
            + planet_json
            + _LOADER_SCRIPT_TAIL
            )


def loader_head_tags(
        **symbol_options: Any,
        ) -> list[ui.Tag]:
    """Return the loader's inline script tag."""
    return [
            ui.tags.script(
                    ui.HTML(
                            loader_script(
                                    **symbol_options
                                    )
                            )
                    ),
            ]


__all__ = [
        "ACTION_IDS",
        "AUTO_HIDE_MS",
        "PLANET_SYMBOLS",
        "SOL_SYMBOLS",
        "STATUS_LINES",
        "loader_head_tags",
        "loader_panel",
        "loader_script",
        ]
