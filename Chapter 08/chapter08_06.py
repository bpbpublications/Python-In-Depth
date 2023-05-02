
class Greeter:

    def __init__(self):
        self.closed = False
        self.allowed = 10

    def greet(self, name="", debug=False):
        if not self.closed:
            if self.allowed:
                print(f"++ Hello {name}")
                self.allowed -= 1
                if debug:
                    print(f"(Can still greet {self.allowed})")
            else:
                print("Sorry, no greeting left")
        else:
            print("Greeting machine is closed")


from contextlib import contextmanager

@contextmanager
def greeting_manager():
    greeter = Greeter()

    greeter.closed = False
    try:
        yield greeter
    finally:
        greeter.closed = True
        greeter.allowed = 10


if __name__ == "__main__":

    # First greeting
    with greeting_manager() as gm:
        gm.greet("Kamon", debug=True)
        gm.greet("Ahidjo", debug=True)

    print()

    # Second one
    with greeting_manager() as gm:
        gm.greet("John", debug=True)
        gm.greet("Sally", debug=True)

