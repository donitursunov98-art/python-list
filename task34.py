royxat1 = []
royxat2 = []

print('1-royxat uchun :')
for i in range(5):
    son = int(input(f'{i+1}-son: '))
    royxat1.append(son)

print('2-royxat uchun :')
for i in range(5):
    son = int(input(f'{i+1}-son: '))
    royxat2.append(son)

umumiy = []

for x in royxat1:
    if x in royxat2 and x not in umumiy:
        umumiy.append(x)

print('1-royxat:', royxat1)
print('2-royxat:', royxat2)
print('Umumiy elementlar:', umumiy)
