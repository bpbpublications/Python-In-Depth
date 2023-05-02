
f = None

with open("testing_files/sample.txt") as f:
    print("File object within the 'with' block:", f, sep="\n")

print("File object after the 'with' block:", f, sep="\n")
print("Is the file closed?")
if f.closed:
    print("Yes")
else:
    print("No")