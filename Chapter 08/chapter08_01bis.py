
print("Version with error")
try:
    print("Hello World")
    # No luck, an exception
    number = int("abc")
finally:
    print("==> Let's start our journey to the moon!")

print("TO THE MOON...")