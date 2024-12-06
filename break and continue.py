#break and continue

while True:
    name = input("Enter your name: ")
    if name != "":
        print("Hellow "+name)
    age = input(f"How old are you {name}?: ")
    if age != "":
        print(f"wow {name} your already {age} years old")
    break

phone_number = "090-232-344"
for i in phone_number:
    if i == "-":
        continue
    print (i, end="")

    
for i in range (1,21):
    if i == 13:
        pass
    else:
        print()
