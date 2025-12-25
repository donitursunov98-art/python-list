nums = []

for i in range(10):
    son = int(input(f'{i+1}-sonni kiriting: '))
    nums.append(son)

yangi = []

for i in nums:
    if nums.count(i) == 1:
        yangi.append(i)

print('Kiritilgan royxat:', nums)
print('Takrorlanmagan sonlar:', yangi)
