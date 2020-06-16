money = abs(int(input()))
if money >= 6769:
    print(money // 6769, 'sheep')
elif 3848 <= money < 6769:
    print(money // 3848, 'cows' if money // 3848 > 1 else 'cow')
elif 1296 <= money < 3848:
    print(money // 1296, 'pigs' if money // 1296 > 1 else 'pig')
elif 678 <= money < 1296:
    print(money // 678, 'goats' if money // 678 > 1 else 'goat')
elif 23 <= money < 678:
    print(money // 23, 'chickens' if money // 23 > 1 else 'chicken')
else:
    print('None')