def logger_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} was called")
        return function(*args, **kwargs)

    return wrapper


@logger_decorator
def foo(number):
    print(f"number was {number}")


foo(2)
foo(3)
