
class Greeter:

    def __init__(self):
        self.closed = False
        self.allowed = 10

    def greet(self, debug=False):
        if not self.closed:
            if self.allowed:
                print("++ Hello my friend")
                self.allowed -= 1
                if debug:
                    print(f"(Can still greet {self.allowed})")
            else:
                print("Sorry, no greeting left")
        else:
            print("Greeting machine is closed")


greeter = Greeter()


class GreetingCM:

    def __enter__(self):
        print("Start greeting!")
        greeter.closed = False
        greeter.greet(debug=True)
        return self

    def __exit__(self, type, value, traceback):
        print("We are done with the greeting")
        # Do the resource management stuff
        greeter.closed = True
        greeter.allowed = 10
        return True


if __name__ == "__main__":

    # First use
    with GreetingCM() as cm:
        print("++ Hello You")

    print("Is greeter closed?", greeter.closed)
    print()

    # Second use
    with GreetingCM() as cm:
        print("++ Hello")

    print("Is greeter closed?", greeter.closed)
    print()
