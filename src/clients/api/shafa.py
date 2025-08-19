from typing import Union

from src.utils.client import JSONClient
from src.clients.product import ProductClient
from src.enums.shafa import URLEnum


class ShafaClient(ProductClient, JSONClient):
    def __init__(self):
        super().__init__(
            base_url=URLEnum.BASE_URL.value
        )

    async def get_products(self) -> None:
        pass

    async def get_products_all(
        self,
        search_text: str,
        page_enum: int = 1,
        first: int = 44
    ) -> Union[None, dict, list]:
        self.endpoint = URLEnum.PRODUCTS_ENDPOINT_URL.value
        self.payload = {
            "operationName": "WEB_CatalogProducts",
            "variables": {
                "catalogSlug": "clothes",
                "sizes": [],
                "conditions": [],
                "characteristics": [],
                "brands": [],
                "colors": [],
                "ukrainian": False,
                "searchText": search_text,
                "cities": [],
                "priceId": [],
                "pageNum": page_enum,
                "first": first
            },
            "query": "query WEB_CatalogProducts($first: Int!, $pageNum: Int!, $catalogSlug: String, $brands: [Int], $orderBy: String, $sizes: [Int], $conditions: [Int], $colors: [Int], $priceTo: Int, $priceFrom: Int, $priceId: [Int], $ukrainian: Boolean, $searchText: String, $freeShipping: Boolean, $isOnSale: Boolean, $characteristics: [Int!], $cities: [Int!], $lastViewedProductId: Int, $indexedFilter: IndexedFilterInput) {\n  products(\n    first: $first\n    pageNum: $pageNum\n    orderBy: $orderBy\n    sizes: $sizes\n    condition: $conditions\n    colors: $colors\n    priceTo: $priceTo\n    priceFrom: $priceFrom\n    catalogSlug: $catalogSlug\n    brands: $brands\n    priceId: $priceId\n    ukrainian: $ukrainian\n    searchText: $searchText\n    freeShipping: $freeShipping\n    isOnSale: $isOnSale\n    characteristics: $characteristics\n    cities: $cities\n    lastViewedProductId: $lastViewedProductId\n    indexedFilter: $indexedFilter\n  ) {\n    mostFrequentCatalogSlug\n    topLevelCategories {\n      id\n      name\n      slug\n      countOfProducts\n      __typename\n    }\n    edges {\n      node {\n        id\n        ...productCardFeedData\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      endCursor\n      hasNextPage\n      total\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment productCardFeedData on Product {\n  id\n  url\n  thumbnail\n  name\n  price\n  oldPrice\n  statusTitle\n  discountPercent\n  ...productLikes\n  brand {\n    id\n    name\n    __typename\n  }\n  catalogSlug\n  isNew\n  sizes {\n    id\n    name\n    __typename\n  }\n  saleLabel {\n    status\n    date\n    price\n    __typename\n  }\n  freeDeliveryServices\n  isUkrainian\n  ownerHasRecentActivity\n  tags\n  rating\n  ratingAmount\n  seller {\n    id\n    isTopSeller\n    __typename\n  }\n  isViewed\n  createdAt\n  sellingCondition\n  __typename\n}\n\nfragment productLikes on Product {\n  likes\n  isLiked\n  __typename\n}"
        }
        data = await self.post()
        return data

    async def get_products_top(
        self,
        search_text: str,
        page_enum: int = 1,
        first: int = 8
    ) -> Union[None, dict, list]:
        self.endpoint = URLEnum.PRODUCTS_ENDPOINT_URL.value
        self.payload = {
            "operationName": "WEB_CatalogTopProductsV2",
            "variables": {
                "catalogSlug": "clothes",
                "sizes": [],
                "conditions": [],
                "characteristics": [],
                "brands": [],
                "colors": [],
                "ukrainian": False,
                "searchText": search_text,
                "priceId": [],
                "first": first,
                "pageNum": page_enum,
                "paginationType": "PAGE"
            },
            "query": "query WEB_CatalogTopProductsV2($first: Int!, $catalogSlug: String, $dynamicCollectionSlug: String, $brands: [Int], $sizes: [Int], $conditions: [Int], $colors: [Int], $priceTo: Int, $priceFrom: Int, $priceId: [Int], $ukrainian: Boolean, $freeShipping: Boolean, $isOnSale: Boolean, $characteristics: [Int!], $searchText: String, $paginationType: ProductPaginationType!, $pageNum: Int, $after: String) {\n  topProductsV2(\n    first: $first\n    sizes: $sizes\n    condition: $conditions\n    colors: $colors\n    priceTo: $priceTo\n    priceFrom: $priceFrom\n    catalogSlug: $catalogSlug\n    dynamicCollectionSlug: $dynamicCollectionSlug\n    brands: $brands\n    priceId: $priceId\n    ukrainian: $ukrainian\n    freeShipping: $freeShipping\n    isOnSale: $isOnSale\n    characteristics: $characteristics\n    searchText: $searchText\n    paginationType: $paginationType\n    pageNum: $pageNum\n    after: $after\n  ) {\n    edges {\n      node {\n        id\n        isTop\n        ...productCardFeedData\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment productCardFeedData on Product {\n  id\n  url\n  thumbnail\n  name\n  price\n  oldPrice\n  statusTitle\n  discountPercent\n  ...productLikes\n  brand {\n    id\n    name\n    __typename\n  }\n  catalogSlug\n  isNew\n  sizes {\n    id\n    name\n    __typename\n  }\n  saleLabel {\n    status\n    date\n    price\n    __typename\n  }\n  freeDeliveryServices\n  isUkrainian\n  ownerHasRecentActivity\n  tags\n  rating\n  ratingAmount\n  seller {\n    id\n    isTopSeller\n    __typename\n  }\n  isViewed\n  createdAt\n  sellingCondition\n  __typename\n}\n\nfragment productLikes on Product {\n  likes\n  isLiked\n  __typename\n}"
        }
        data = await self.post()
        return data
