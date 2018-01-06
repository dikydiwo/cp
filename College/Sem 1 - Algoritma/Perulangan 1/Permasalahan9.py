x = int(input())
cond = False

while cond == False:
    if (x+4) % 4 == 0 or (x+4) % 400 == 0 and (x+4) % 100 != 0:
        x += 4
        cond = True
    else:
        x += 1

print(x)