timezone = input()
if timezone == '+14':
    print('Wednesday')
elif timezone in ['-11', '-12']:
    print('Monday')
else:
    print('Tuesday')