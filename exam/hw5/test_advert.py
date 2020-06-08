import pytest
import advertclass

def test_location():
    t = advertclass.Advert({"title": "iPhone X", "price": 100,
        "location": {"address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]}})
    assert t.location.address == "город Самара, улица Мориса Тореза, 50"

def test_nullprice():
    t = advertclass.Advert({"title": "iPhone X"})
    assert t.price == 0

def test_minusprice():
    with pytest.raises(ValueError):
        advertclass.Advert({"title": "iPhone X", "price": -100})

def test_notitle():
    with pytest.raises(ValueError):
        advertclass.Advert({"price": 100})
