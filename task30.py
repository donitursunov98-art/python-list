text = []

for i in range(5):
    t = input(f'{i + 1} sozni kiriting: ')
    text.append(t)

palindrom = []

for i in text:
    if i == i[::-1]:
        palindrom.append(i)

print('kiritilgan soz: ', text)
print('palindrom soz: ', palindrom)
