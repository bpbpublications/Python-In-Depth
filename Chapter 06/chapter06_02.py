

def format(names):
    return " ".join(names)


def show_name_reversed(func):

    def wrapper(names):

        res = list(func(names))
        res.reverse()
        return "".join(res)

    return wrapper

decorated = show_name_reversed(format)
result = decorated(names=["John", "Doe"])
print(result)