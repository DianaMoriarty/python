import pytest


def number_input():
    while True:
        num = input("Введите номер элемента последовательности Фибоначчи: ")
        if not num.isnumeric():
            print("Некоректный ввод, попробуйте снова")
        else:
            return int(num)


def fibonacci_iter(n):
    """Функция, возвращающая список"""
    num1 = num2 = 1
    l = []
    for i in range(n):
        l.append(num1)
        num1, num2 = num2, num1 + num2
    return l


def fibonacci(n: int):
    """Функция, возвращающая n-ый элемент последовательности"""
    f = fibonacci_iter(n)
    return f[len(f)-1]


def test_seq():
    assert fibonacci_iter(3) == [1, 1, 2]


def test_num():
    assert fibonacci(6) == 8


if __name__ == '__main__':
    n = number_input()
    print(fibonacci(n))
    test_num()
    test_seq()
