
def show_name(names):

    def concatenate():

        return " ".join(names)

    return concatenate

concat = show_name(names=["John", "Doe"])
print(concat())