income = abs(int(input()))
percent = 0
if 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
elif income > 132406:
    percent = 28

print(f'The tax for {income} is {percent}%. That is {income * percent / 100:.0f} dollars!')