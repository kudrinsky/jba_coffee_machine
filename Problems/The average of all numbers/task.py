a = int(input())
b = int(input())
summa = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        summa += i
        count += 1
print(summa / count)