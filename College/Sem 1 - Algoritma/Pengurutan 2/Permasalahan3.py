data = []
time = []

for i in range(10):
    ans = 0
    s = str(input())
    data += [s]
    char = s.split()
    for j in range(len(char)):
        if char[j] == "jam": ans += int(char[j-1]) * 3600
        elif char[j] == "menit": ans += int(char[j-1]) * 60
        elif char[j] == "detik": ans += int(char[j-1])
    time += [ans]

for i in range(10):
    for j in range(i+1,10):
        if time[j] < time[i]:
            time[i],time[j] = time[j],time[i]
            data[i],data[j] = data[j],data[i]

for i in range(3):
    print(data[i])