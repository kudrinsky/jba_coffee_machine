numbers = []
result = 0
while True:
    numbers.append(int(input()))
    if sum(numbers) == 0:
        for number in numbers:
            result += number ** 2
        print(result)
        break