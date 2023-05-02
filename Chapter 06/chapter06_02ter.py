
def show_name_reversed(case=""):
    def show_name_wrapper(func):

        def wrapper(names):

            res = list(func(names))
            res.reverse()
            res_str = "".join(res)
            if case == "upper":
                return res_str.upper()
            elif case == "lower":
                return res_str.lower()
            else:
                return res_str

        return wrapper
    return show_name_wrapper

@show_name_reversed(case="upper")
def format(names):
    """ Format the names of a person """
    return " ".join(names)


if __name__ == "__main__":
    result = format(names=["Jane", "Doe"])
    print(result)