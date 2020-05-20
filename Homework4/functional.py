import doctest
import math
from typing import Iterable


## 1. Написать функцию получения размера генератора
def ilen(iterable: Iterable):
    """
    >>> ilen([1,2,3,4,'g'])
    5
    >>> ilen([])
    0
    """
    return sum(1 for i in iterable)


## 2. Написать функцию flatten, которая из многоуровневого массива сделает одноуровневый
def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    >>> list(flatten([2, [0, 6], [7, [8]]]))
    [2, 0, 6, 7, 8]
    """
    new = []
    for i in iterable:
        if isinstance(i, Iterable):
            new += flatten(i)
        else:
            new.append(i)
    return new


## 3. Написать функцию, которая удалит дубликаты, сохранив порядок
def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    >>> list(distinct([6, 5, 6, 6, 6, 5, 6, 6, 6]))
    [6, 5]
    """
    mylist = []
    for i in iterable:
        if i not in mylist:
            mylist.append(i)
    return mylist


## 4. Неупорядоченная последовательность из словарей, сгруппировать по ключу, на выходе словарь
def groupby(key, iterable: Iterable):
    """
    >>> users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    >>> groupby('gender', users)
    {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    """
    result = dict()
    for i in iterable:
        value = i[key]
        result.setdefault(value, []).append(i)
    return result


## 5. Написать функцию, которая разобьет последовательность на заданные куски
def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, )]
    """
    result = []
    part = math.ceil(len(iterable)/size)
    for i in range(part):
        result.append(tuple(iterable[size*i:size*i+size]))
    return result


## 6. Написать функцию получения первого элемента или None
def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
    try:
        return next(iter(iterable))
    except Exception:
        return None

    
## 7. Написать функцию получения последнего элемента или None
def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
    try:
        return list(iterable)[-1]
    except Exception:
        return None
