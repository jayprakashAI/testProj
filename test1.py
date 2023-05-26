def sqr(a):  # type: ignore
    if str(a).isnumeric():
        return a * a
    else:
        print("Cannot compute for non numeric values, please pass numbers")


def cub(b):
    if b.isalpha():
        return b + b + b
    else:
        print("This function cannot be passed non alphabet values")


def welcome():
    print("Welcome to Python classes")
