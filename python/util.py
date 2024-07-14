import constants as C

from data_model.dto.request_dto import *


class GridUtil:

    @staticmethod
    def instantiateGridDTO() -> GridDTO:
        grid = GridDTO()
        grid.algorithm = C.DEFAULT_ALGO
        grid.from_ = C.DEFAULT_FROM
        grid.size = C.DEFAULT_GRID_SIZE
        grid.context = GridUtil.instantiateContext()
        grid.filters = GridUtil.instantiateFilter("GRID")
        grid.listingSearch = GridUtil.instantiateListingSearch()
        grid.settings = GridUtil.instantiateSettings()
        grid.sort = GridUtil.instantiateSort()
        return grid

    @staticmethod
    def instantiateContext() -> Context:
        context = Context()
        context.cart = {}
        context.shippingCountry = C.COUNTRY_CODE_US
        user_profile = UserProfile()
        user_profile.priceAffinity = C.DEFAULT_PRICE_AFFINITY
        context.userProfile = user_profile
        return context

    @staticmethod
    def instantiateFilter(level: str) -> Filters:
        if level == "GRID":
            return GridUtil.instantiateGridFilter(level)
        elif level == "LISTING_SEARCH":
            return GridUtil.instantiateLSFilter(level)
        return Filters()

    @staticmethod
    def instantiateGridFilter(level: str) -> Filters:
        filters = Filters()
        filters.match_ = {}
        filters.range = Range()
        term = GridUtil.instantiateTerm(level)
        filters.term = term
        return filters

    @staticmethod
    def instantiateTerm(level: str) -> Term:
        if level == "GRID":
            return GridUtil.instantiateGridTerm()
        elif level == "LISTING_SEARCH":
            return GridUtil.instantiateLSTerm()
        return Term()

    @staticmethod
    def instantiateGridTerm() -> Term:
        term = Term()
        term.productLineName = [C.YUGIOH_LOWER]
        term.setName = []
        return term

    @staticmethod
    def instantiateListingSearch() -> ListingSearch:
        listing_search = ListingSearch()
        context = Context()
        context.cart = {}
        listing_search.context = context
        listing_search.filters = GridUtil.instantiateFilter("LISTING_SEARCH")
        return listing_search

    @staticmethod
    def instantiateLSFilter(level: str) -> Filters:
        filters = Filters()
        exclude = Exclude()
        exclude.channelExclusions = C.DEFAULT_CHANNEL_EXCLUSION
        filters.exclude = exclude
        range_ = Range()
        quantity = Quantity()
        quantity.gte = C.DEFAULT_GTE
        range_.quantity = quantity
        filters.range_ = range_
        filters.term = GridUtil.instantiateTerm(level)
        return filters

    @staticmethod
    def instantiateLSTerm() -> Term:
        term = Term()
        term.channelId = C.DEFAULT_CHANNEL_ID
        term.language = [C.LANGUAGE_ENGLISH]
        term.sellerStatus = C.SELLER_STATUS_LIVE
        term.condition = [C.CONDITION_NM]
        term.listingType = [C.DEFAULT_LISTING_TYPE]
        return term

    @staticmethod
    def instantiateSettings() -> Settings:
        settings = Settings()
        settings.didYouMean = {}
        settings.useFuzzySearch = C.DEFAULT_FUZZY_SEARCH
        return settings

    @staticmethod
    def instantiateSort() -> Sort:
        sort = Sort()
        sort.field = C.DEFAULT_GRID_SORT_FIELD
        sort.order = C.DEFAULT_SORT_ORDER
        return sort


class DetailViewUtil:

    @staticmethod
    def instantiateDetailViewDTO() -> DetailViewDTO:
        detail_view = DetailViewDTO()
        detail_view.context = DetailViewUtil.instantiateContext()
        detail_view.filters = DetailViewUtil.instantiateFilters()
        detail_view.from_ = C.DEFAULT_FROM
        detail_view.size = C.DEFAULT_DETAIL_VIEW_SIZE
        detail_view.sort = DetailViewUtil.instantiateSort()
        return detail_view

    @staticmethod
    def instantiateContext() -> Context:
        context = Context()
        context.cart = {}
        shippingCountry: C.COUNTRY_CODE_US
        return context

    @staticmethod
    def instantiateFilters() -> Filters:
        filters = Filters()
        exclude = Exclude()
        exclude.channelExclusions = C.DEFAULT_CHANNEL_EXCLUSION
        filters.exclude = exclude
        range_ = Range()
        quantity = Quantity()
        quantity.gte = C.DEFAULT_GTE
        range_.quantity = quantity
        filters.range_ = range_
        term = Term()
        term.channelId = C.DEFAULT_CHANNEL_ID
        term.condition = [C.CONDITION_NM]
        term.language = [C.LANGUAGE_ENGLISH]
        term.listingType = [C.DEFAULT_LISTING_TYPE]
        term.printing = [C.PRINTING_1ST_ED]
        term.sellerStatus = C.SELLER_STATUS_LIVE
        filters.term = term
        return filters

    @staticmethod
    def instantiateSort() -> Sort:
        sort = Sort()
        sort.field = C.DEFAULT_DETAIL_VIEW_SORT_FIELD
        sort.order = C.DEFAULT_SORT_ORDER
        return sort


class JSONUtil:

    @staticmethod
    def overrideVariableNames(string: str) -> str:
        string = string.replace("range_", "range")
        string = string.replace("match_", "match")
        string = string.replace("from_", "from")
        return string
