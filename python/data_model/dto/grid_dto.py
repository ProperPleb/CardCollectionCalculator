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
    sellerStatus: str
    productLineName: list
    setName: list
    language: list


@dataclass(init=False)
class Exclude:
    channelExclusions: int


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


