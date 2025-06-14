
# Compass_of_Recharging.py

from enum import Enum
import random

class RechargeTime(Enum):
    AT_DAWN = "at dawn"
    AT_SUNSET = "at sunset"
    SHORT_OR_LONG_REST = "on a short or long rest"
    LONG_REST = "on a long rest"

    def __str__(self):
        return self.value


recharging = random.choice(["at dawn", "at sunset", "on a short or long rest"])
