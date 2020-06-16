col = abs(int(input()))
row = abs(int(input()))
if col in [1, 8] and row in [1, 8]:
    print(3)
elif col in [1, 8] or row in [1, 8]:
    print(5)
else:
    print(8)