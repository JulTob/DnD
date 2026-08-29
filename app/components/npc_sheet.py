                    ),
                ),
        Chip(
                "💚",
                # The ceiling, not the current pool — same wording as the PC sheet.
                "Max Hit Points",
                safe_str(
                        getattr(
                                npc,
                                "HP",
                                "-",