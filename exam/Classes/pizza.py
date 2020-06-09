import pytest


class Pizza:
    """Класс для рецептов пицц"""
    def __init__(self, ingredients):
        self.__dict__.update(ingredients)

        if not self.__dict__.get('dough'):
            raise ValueError("Pizza must have dough")
        if not self.__dict__.get('tomato paste'):
            raise ValueError("Pizza must have tomato paste")

        for key, value in self.__dict__.items():
            if key == 'name':
                pass
            else:
                if value <= 0:
                    raise ValueError("Ingredients must be > 0")

    def dict(self):
        return self.__dict__


    def __repr__(self):
        s = ''
        for key, value in self.__dict__.items():
            if key == 'name':
                s = s + value + ": "
            else:
                s = s + key + " " + str(value) + ", "
        return s[:-2]


def test_no_dough():
    with pytest.raises(ValueError):
        Pizza({"tomato paste": 50})


def test_minus_ingredients():
    with pytest.raises(ValueError):
        Pizza({'dough': 0, "tomato paste": -50})


def test_dict():
    t = Pizza({'dough': 100, "tomato paste": 50})
    assert t.dict() == {'dough': 100, "tomato paste": 50}


if __name__ == '__main__':
    receipt_for_peperoni = {'name': 'Peperoni', 'dough': 100, "tomato paste": 50,
                            "sausage": 40, "mozzarella": 10}
    receipt_for_cheese_pizza = {'name': 'Cheese pizza', 'dough': 90,
                                "tomato paste": 60, "cheese": 20, }
    receipt_for_mexican_pizza = {'name': 'Mexican Pizza', 'dough': 200, "tomato paste": 80,
                                 "chicken": 30, "pepper": 25, "jalapenos": 10, "salsa sauce": 25}
    peperoni = Pizza(receipt_for_peperoni)
    cheese = Pizza(receipt_for_cheese_pizza)
    mexican = Pizza(receipt_for_mexican_pizza)
    print(mexican.dict())
    print(str(mexican))
