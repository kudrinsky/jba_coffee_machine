scores = input().split()
# put your python code here
correct = 0
incorrect = 0
for score in scores:
    if score == 'C':
        correct += 1
    elif score == 'I':
        incorrect += 1
        if incorrect == 3:
            break

print('Game over' if incorrect == 3 else 'You won')
print(correct)