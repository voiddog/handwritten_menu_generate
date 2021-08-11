# coding: utf-8

import math
import random
from DrawBox import DrawBox

from PIL import Image


class FoodItem:

    def __init__(self, name: str, min_price: int, max_price: int, kind: str):
        super().__init__()
        self.name = name
        self.min_price = min_price
        self.max_price = max_price
        self.kind = kind

    def getPrice(self) -> int:
        ratio = random.random()
        return math.ceil((1 - ratio) * self.min_price + ratio * self.max_price)


def _generateRandomFood(menu: list[FoodItem], used_list: list[FoodItem]) -> FoodItem:
    random_index = math.floor(random.random() * len(menu))
    for i in range(len(menu)):
        tmp = menu[random_index]
        if tmp in used_list:
            random_index = (random_index + 1) % len(menu)
            continue
        return tmp
    return menu[random_index]


def renderRandomMenuList(drawBox: DrawBox, menu: list[FoodItem], count: int) -> tuple[Image, int]:
    text = ""
    price_sum = 0
    used_list = []
    for i in range(0, count):
        food_item = _generateRandomFood(menu, used_list)
        used_list.append(food_item)
        price = food_item.getPrice()
        tmp = "%s %s\n" % (food_item.name, price)
        text += tmp
        price_sum += price

    return (drawBox.render(text), price_sum)
