best_cafe = ''
cats = 0
while True:
    cafe = input()
    if cafe == 'MEOW':
        break
    if int(cafe.split()[1]) > cats:
        best_cafe = cafe.split()[0]
        cats = int(cafe.split()[1])
print(best_cafe)