from enum import Enum


class SortProducts(Enum):
    SORTBY: str = "Sort by"
    DEFAULT: str = "default sorting"
    POPULARITY: str = f"{SORTBY} popularity"
    AVERAGE_RATING: str = f"{SORTBY} average rating"
    LATEST: str = f"{SORTBY} latest"
    HIGH: str = f"{SORTBY} price: high to low"
    LOW: str = f"{SORTBY} price: low to high"
