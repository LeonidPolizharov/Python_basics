from functools import wraps


def type_logger(my_func):
    log_class = {}

    @wraps(my_func)
    def my_logger(*args):
        nonlocal log_class
        num = args
        for i in args:
            log_class[i] = type(i)
        return log_class

    return my_logger


@type_logger
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube.__name__, calc_cube(10, 15.5))
