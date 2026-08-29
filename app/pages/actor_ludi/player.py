                    },
                )

    @output
    @render.text
    def char_level_display() -> str:
        current = (
            state.player_parameters()
            or _parameters_from_data(
                state.player()
                )
            )
        lvl = max(
                1,
                min(
                    20,
                    safe_int(
                        current.get(
                            "level"
                            ),
                        1,
                        ),
                    ),
                )
        return f"Level {lvl}"

    @output
    @render.ui
    def character_result() -> ui.Tag:
        error = state.player_error()

        if error:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.h3(
                            "Character generation failed"
                            ),
                    ui.p(
                            error
                            ),
                    )

        data = state.player()

        if not data:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.p(
                            "Generate a character from Home."
                            ),
                    )

        return build_character_sheet(