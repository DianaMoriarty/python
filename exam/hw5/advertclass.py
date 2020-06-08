import json


def jsondata(data):
    """Функция для обработки json"""
    if isinstance(data, str):
        return json.loads(data)
    else:
        return data


class Advert:
    """Класс для объявлений"""
    def __init__(self, ad):
        self.price = 0
        data = jsondata(ad)
        self.__dict__.update(data)

        for key, value in self.__dict__.items():
            if isinstance(value, dict):
                setattr(self, key, Field(value))

        if not self.__dict__.get('title'):
            raise ValueError("advert must have title")
        if self.price < 0:
            raise ValueError("price must be >= 0")

    repr_color_code = 33  # color - yellow

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};48m{self.title} | {self.price} ₽\033[1;00;00m'


class Field:
    """Класс для обработки вложенных полей"""
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, Field(value))
            else:
                setattr(self, key, value)


if __name__ == '__main__':
    advertIphone = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    advertDog = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }

    advert = Advert(advertIphone)
    print(advert.__dict__)
    print(advert.price)
    print(advert.location.address)
