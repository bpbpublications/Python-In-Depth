
try:
    f = open("testing_files/sample.txt")
    print("No luck, an exception happens")

    number = int("abc")
finally:
    print("Finished with the file")
    print("We need to close the file...")
    f.close()
    print("Closed!")