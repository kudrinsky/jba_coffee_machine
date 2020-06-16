chars = list(input())
result = ''
for char in chars:
    if char.isupper():
        result += '_' + char.lower()
    else:
        result += char
print(result)