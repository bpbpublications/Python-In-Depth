
with open("./testing_files/sample1.txt") as f1, \
        open("./testing_files/sample2.txt") as f2:
    print("Sample 1 text:")
    print(f1.read())
    print()
    print("Sample 2 text:")
    print(f2.read())

