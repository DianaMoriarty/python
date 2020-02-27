import random
from random import randint
import time


def step1():
    print("Это утка-маляр -> 🦆")
    print("Утке пришло сообщение на телефон:\n")
    print("|---------------------------------------------|")
    print("|Друзья утки:")
    print("|", "      ", "\033[1m {} \033[0m".format("Ждем тебя в баре DrunkDuck!"))
    print("|---------------------------------------------|")
    print("Утка решает пойти выпить в бар. Разрешите ей провеяться?")
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_yes()
    return step2_no()


def step2_yes():
    weather = ["солнце", "облачно", "снег", "дождь", ]
    print("Перед выходом 🦆 решает проверить погоду через 📱")
    print("\033[3m {} \033[0m".format("Кря, гугл, какая сейчас погода?"))
    weather_now = random.choice(weather)
    print("\033[1m На улице {} \033[0m".format(weather_now))
    if weather_now in weather[2:]:
        print("Хочет ли утка взять зонт?")
        option = ''
        options = {'да': True, 'нет': False}
        while option not in options:
            print('Выберите: {}/{}'.format(*options))
            option = input()
        if options[option]:
            print("🦆 умный, он не промокнет")
        else:
            print("🦆 глупый, он промокнет")
    else:
        print("Хочет ли 🦆 надеть кепку?")
        option = ''
        options = {'да': True, 'нет': False}
        while option not in options:
            print('Выберите: {}/{}'.format(*options))
            option = input()
        if options[option]:
            print("Хороший выбор, ему идет!")
        else:
            print("🦆 и так хорошо")
    return step3()


def step2_no():
    print("Вы расстроили утку. Он останется дома в одиночестве 😢")


def step3():
    print("Чтобы пойти выпить 🍺, 🦆 нужны 💲💲💲")
    print("Только вчера 🦆 получил зарплату в 1000💲")
    print("Только незадача, его жена спрятала зарплату в сейфе, чтоб он ее не пропил")
    print("🦆 нужно отгадать число от 0 до 9, чтобы открыть сейф. У него есть только 5 попыток")
    code = randint(0, 9)
    # code = 5
    i = 0
    while i <= 4:
        try:
            num = int(input("Введите число: "))
            if num == code:
                print("🦆 отгадал код и теперь может пойти в бар!")
                return step4()
            else:
                print("Неправильный код")
            i = i + 1
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
    print("🦆 не угадал. Он останется дома в одиночестве и без денег 😢")


def step4():
    print("Сколько 💲 🦆 хочет взять с собой в бар? Введите число от 1 до 1000")
    while True:
        money = input("Введите число: ")
        if not money.isnumeric():
            print("Некорректный. Попробуйте снова: ")
        elif not 1 <= int(money) <= 1000:
            print("Число не в диапазоне. Попробуйте снова")
        else:
            print("🦆 берет ", money, "💲!")
            break
    return step5(int(money))


def step5(money):
    print("🦆 пошел с 💲💲💲 выпить с друзьями!")
    print("\033[1m {} \033[0m".format("A few moments later..."))
    time.sleep(5)
    if money <= 500:
        print("🦆 потратил все взятые деньги, но зато хорошо отдохнул! 😊")
    else:
        print("🦆 потратил большую часть зарплаты в баре, жена будет недовольна 😰. 🦆 расстроен 😞")


if __name__ == '__main__':
    step1()
