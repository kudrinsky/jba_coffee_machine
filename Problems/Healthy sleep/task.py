a = abs(int(input()))
b = abs(int(input()))
h = abs(int(input()))
if a <= h <= b:
    print('Normal')
elif h < a:
    print('Deficiency')
else:
    print('Excess')