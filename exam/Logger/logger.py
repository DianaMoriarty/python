import logging


def timeit(prefix=''):
    def _timeit(func):
        def wrapper(*args, **kwargs):
            if not prefix:
                name = func.__name__
            else:
                name = prefix
            log = logging.getLogger(name)
            log.setLevel(logging.DEBUG)  # уровень логирования
            file = logging.FileHandler("mylogshere.log")  # файл для логов
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # форматирование
            formatter = logging.Formatter(fmt)
            file.setFormatter(formatter)
            log.addHandler(file)
            log.info("Вызов функции: %s" % name)
            result = func(*args, **kwargs)
            log.info("Результат: %s" % result)
            return func(*args, **kwargs)
        return wrapper
    return _timeit


@timeit()
def incr():
    #print("Hello")
    return 1


if __name__ == "__main__":
    incr()

