nums = []

n = int(input('n: '))

for i in range(n):
    son = int(input(f'{i+1}-sonni kiriting: '))
    nums.append(son)

max_elem = nums[0]
max_count = nums.count(nums[0])

for i in nums:
    if nums.count(i) > max_count:
        max_count = nums.count(i)
        max_elem = i

print(max_elem)
