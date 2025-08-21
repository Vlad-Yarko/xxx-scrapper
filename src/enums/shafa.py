import enum


class URLEnum(str, enum.Enum):
    BASE_URL = "https://shafa.ua/api/v3/"
    PRODUCTS_ENDPOINT_URL = "graphiql"


class StateEnum(enum.Enum):
    new = [1]
    used = [2, 3, 4, 5]
