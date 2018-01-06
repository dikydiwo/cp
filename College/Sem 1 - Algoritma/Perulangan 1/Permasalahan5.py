x = int(input())
binary = str()
octal  = str()
hexa   = str()
num  = x
num1 = x
num2 = x

reverseBinary = str()
reverseOctal  = str()
reverseHexa   = str()

while num > 0:
    modBinary = num % 2
    num //= 2
    binary += str(modBinary)

while num1 > 0:
    modOctal = num1 % 8
    num1 //= 8
    octal += str(modOctal)

while num2 > 0:
    modHexa = num2 % 16

    if modHexa == 10:
        modHexa = "A"
    elif modHexa == 11:
        modHexa = "B"
    elif modHexa == 12:
        modHexa = "C"
    elif modHexa == 13:
        modHexa = "D"
    elif modHexa == 14:
        modHexa = "E"
    elif modHexa == 15:
        modHexa = "F"

    num2 //= 16

    hexa += str(modHexa)

for i in range(len(binary)-1,-1,-1):
    reverseBinary += binary[i]

for j in range(len(octal)-1,-1,-1):
    reverseOctal += octal[j]

for k in range(len(hexa)-1,-1,-1):
    reverseHexa += hexa[k]

print(reverseBinary, reverseOctal, reverseHexa)