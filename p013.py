file = open("p13_numbers.txt", "r")
sum = 0

while True:
    num = file.readline()
    if num == '':
        break
    sum += int(num)

print(str(sum)[:10])
