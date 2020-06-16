# Make sure your output matches the assignment *exactly*
hours = abs(int(input()))
if hours < 2:
    print('That seems reasonable')
elif hours < 4:
    print('Do you have time for anything else?')
else:
    print('You need to get outside more!')