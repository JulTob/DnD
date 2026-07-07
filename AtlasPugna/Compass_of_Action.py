from dataclasses import dataclass

@dataclass(frozen=True)
class Action:
    name: str
    description: str
    cost: str = ""
