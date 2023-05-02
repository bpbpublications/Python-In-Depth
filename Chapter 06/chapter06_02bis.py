

def show_name_reversed(func):

    def wrapper(names):

        res = list(func(names))
        res.reverse()
        return "".join(res)

    return wrapper


@show_name_reversed
def format(names):
    return " ".join(names)


result = format(names=["John", "Doe"])
print(result)