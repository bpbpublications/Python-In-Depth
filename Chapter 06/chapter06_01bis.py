
def show_name():

    def concatenate(names):

        return " ".join(names)

    return concatenate

concat = show_name()
print(concat(names=["John", "Doe"]))