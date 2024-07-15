from dataclasses import dataclass


@dataclass
class Card:
    recalc: bool
    quantity: int
    rarity: str
    card_name: str
    unit_price: float
    total_price: float
    set_number: str
    edition: str
    condition: str
