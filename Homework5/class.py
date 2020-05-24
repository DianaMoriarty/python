import json


class Advert:
    """Класс для объявлений"""
    def __init__(self, s):
        self.price = 0
        if isinstance(s, str):
            data = json.loads(s)
        else:
            data = s

        for key, value in data.items():
            if isinstance(value, dict):
                self.__dict__[key] = Field(value)
            else:
                self.__dict__[key] = value

        if not self.__dict__.get('title'):
            raise ValueError("advert must have title")
        if self.price < 0:
            raise ValueError('must be >= 0')

    repr_color_code = 33  # yellow

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};48m{self.title} | {self.price} ₽\033[1;00;00m'


class Field:
    """Класс для обработки вложенных полей"""
    def __init__(self, d):
        for key, value in d.items():
            if isinstance(value, dict):
                self.__dict__[key] = Field(value)
            else:
                self.__dict__[key] = value


if __name__ == '__main__':
    adv_dict_1 = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    adv_dict_2 = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }
