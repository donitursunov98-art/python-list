royxat = ['olma', 'anor', 'banan', 'uzum']

print('Royxat:', royxat)

indeks = int(input('Indeksni kiriting: '))
yangi_qiymat = input('Yangi qiymatni kiriting: ')

if 0 <= indeks < len(royxat):
    royxat[indeks] = yangi_qiymat
    print('Yangilangan royxat:', royxat)
else:
    print('Xato! Notogri indeks.')
