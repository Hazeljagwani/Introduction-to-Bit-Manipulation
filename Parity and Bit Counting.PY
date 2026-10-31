input("Parity - Last bit = 0 even, last bit = 1 odd. Press ENTER ")
for n in [2, 3, 4, 5, 8, 9]:
    if n & 1:
        print("  ", n, "-> odd")
    else:
        print("  ", n, "-> even")

n = int(input("Enter a number( try 13 or 7): "))
input("Count the 1s - watch bits drop off. Press ENTER ")
temp = 0
while temp > 0:
    print(" binaryy: ", bin(temp)[2:], "last bit:", temp & 1)
    temp >>= 1
print(" total 1s in", n, "=", bin(n).count('1'))