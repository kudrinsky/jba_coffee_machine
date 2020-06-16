number = abs(int(input()))
limit = int(number ** 0.5)
flag = True
if number == 1:
    flag = False
else:
    for i in range(2, limit + 1):
        if number % i == 0:
            flag = False
print('This number is prime' if flag else 'This number is not prime')