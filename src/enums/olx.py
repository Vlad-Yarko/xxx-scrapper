import enum


class URLEnum(str, enum.Enum):
    BASE_URL = "https://www.olx.ua/api/v1/"
    PRODUCTS_ENDPOINT_URL = "offers/"


class StateEnum(str, enum.Enum):
    used = "used"
    new = "new"
