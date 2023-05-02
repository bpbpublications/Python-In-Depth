

def show_name(firstname, lastname):

    def concatenate(names):

        return " ".join(names)

    return concatenate(names=[firstname, lastname])

print(show_name(firstname="John", lastname="Doe"))