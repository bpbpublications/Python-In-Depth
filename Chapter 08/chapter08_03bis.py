
f = None

try:
    with open("testing_files/sample.txt") as f:
        print("File object in the 'with' block:",
              f,
              sep="\n")

        print("Expect the file to be closed...")
        print("... even when an exception occurs")
        number = int("abc")

    # Cannot actually see the next 2 print() results...
    print("File object after the 'with' block...")
    print("... but within a try/except:", f, sep="\n")
except ValueError:
    pass

print()

print("File object after the 'with' block:",
      f,
      sep="\n")
print("Is the file closed?")
if f.closed:
    print("Yes")
else:
    print("No")