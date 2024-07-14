from dataclasses import dataclass


@dataclass(init=False)
class Quantity:
    gte: int


@dataclass(init=False)
class Range:
    quantity: Quantity


@dataclass(init=False)
class Term:
    channelId: int
    condition: list
    productLineName: list
    setName: list
    language: list
    listingType: str
    printing: list
    sellerStatus: str


@dataclass(init=False)
class Exclude:
    channelExclusion: int
    listingType: str


@dataclass(init=False)
class UserProfile:
    priceAffinity: int


@dataclass(init=False)
class Context:
    cart: dict
    shippingCountry: str
    userProfile: UserProfile


@dataclass(init=False)
class Filters:
    match_: dict
    term: Term
    exclude: Exclude
    range_: Range


@dataclass(init=False)
class ListingSearch:
    context: Context
    filters: Filters


@dataclass(init=False)
class Settings:
    didYouMean: dict
    useFuzzySearch: bool


@dataclass(init=False)
class Sort:
    field: str
    order: str


@dataclass(init=False)
class GridDTO:
    algorithm: str
    size: int
    from_: int
    context: Context
    filters: Filters
    listingSearch: ListingSearch
    settings: Settings
    sort: Sort


@dataclass(init=False)
class DetailViewDTO:
    from_: int
    size: int
    context: Context
    filters: Filters
    sort: Sort
