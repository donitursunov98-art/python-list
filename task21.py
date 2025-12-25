royhat = [1, 22, 45, 67, 89, 93]

num = int(input('ochirilgan son: '))

if num in royhat:
    royhat.remove(num)
    print('yangilangan royxat: ', royhat)
else:
    print('bunday son yoq: ')    