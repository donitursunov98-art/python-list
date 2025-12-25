sozlar = []

n = int(input('n:'))

for i in range(n):
    soz = input(f'{i+1}-sozni kiriting: ')
    sozlar.append(soz)

uzun_sozlar = []

for soz in sozlar:
    if len(soz) > 5:
        uzun_sozlar.append(soz)

print('Kiritilgan sozlar:', sozlar)
print('Uzunligi 5 dan katta sozlar:', uzun_sozlar)
