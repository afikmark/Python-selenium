from enum import Enum


class SortProducts(Enum):
    SORTBY = "Sort by"
    DEFAULT = "default sorting"
    POPULARITY = f"{SORTBY} popularity"
    AVERAGE_RATING = f"{SORTBY} average rating"
    LATEST = f"{SORTBY} latest"
    HIGH = f"{SORTBY} price: high to low"
    LOW = f"{SORTBY} price: low to high"
