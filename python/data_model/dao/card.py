from dataclasses import dataclass


@dataclass
class Card:
    recalc: bool
    quantity: int
    rarity: str
    card_name: str
    unit_price: float
    total_price: float
    set_prefix: str
    edition: str
