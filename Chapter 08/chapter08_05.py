
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

while greeter.allowed > 0:
    greeter.greet(debug=True)
    print()
