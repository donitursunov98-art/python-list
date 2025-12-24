ism_royxat = []

while True:
    ism = input('Ism kiriting (chiqish uchun stop deb yozing): ')
    if ism.lower() == 'stop':  
        break
    ism_royxat.append(ism)  

print('Ro\'yxatdagi ism soni:', len(ism_royxat))
