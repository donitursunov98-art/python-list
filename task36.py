sozlar = []

n = int(input('n: '))

for i in range(n):
    soz = input(f'{i+1}-sozni kiriting: ')
    sozlar.append(soz)

eng_uzun = sozlar[0]

for s in sozlar:
    if len(s) > len(eng_uzun):
        eng_uzun = s

print('Eng uzun soz:', eng_uzun)
