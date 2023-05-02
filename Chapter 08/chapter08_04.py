class GreetingCM:

    def __enter__(self):
        print("Start greeting!")
        print("++ Hello World")
        return self

    def __exit__(self, type, value, traceback):
        print("We are done with the greeting")
        return True


with GreetingCM() as cm:
    print("++ Hello You")



