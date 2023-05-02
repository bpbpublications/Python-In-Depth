
greeting = "hello world"
new_greeting_letters = list()

for i in greeting:
      if i == "l":
          i = "L"
      new_greeting_letters.append(i)
print(new_greeting_letters)
new_greeting = "".join(new_greeting_letters)
print(new_greeting)



