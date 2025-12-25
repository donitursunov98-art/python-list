royxat1 = []
royxat2 = []

n = int(input('n: '))

print('1-royxatni kiriting:')
for i in range(n):
    son = int(input(f'{i+1}-element: '))
    royxat1.append(son)

print('2-royxatni kiriting:')
for i in range(n):
    son = int(input(f'{i+1}-element: '))
    royxat2.append(son)

for i in range(n):
    vaqtinchalik = royxat1[i]
    royxat1[i] = royxat2[i]
    royxat2[i] = vaqtinchalik

print('Almashtirilgandan keyin:')
print('1-royxat:', royxat1)
print('2-royxat:', royxat2)
