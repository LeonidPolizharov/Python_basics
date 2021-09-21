from functools import wraps


def val_checker(x):
    def _val_checker(my_func):

        @wraps(my_func)
        def checker(arg):
            if arg <= 0:
                msg = 'Incorrect value: ' + str(arg)
                raise ValueError(msg)
            return my_func(arg)

        return checker

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
