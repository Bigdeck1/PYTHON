#nested loop

row = int(input("Enter row number: "))
colounms = int(input("Enter columns number: "))
symbol = input("Enter symbol: ")

for i in range(row):
    for j in range(colounms):
        print(symbol, end="")
    print()

haba = int(input("Enter haba: "))
lapad = int(input("Enter lapad: "))
signal = input("Enter signal: ")

for p in range(haba):
    for l in range(lapad):
        print(signal, end="")
    print()