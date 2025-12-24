kichik = []   
ortacha = []  
uzun = []

sozlar = input('soz: ')

for soz in sozlar:   
    if len(soz) <= 3:
        kichik.append(soz)
    elif 4 <= len(soz) <= 6:
        ortacha.append(soz)
    else:
        uzun.append(soz)   

print('<=3 harfli so\'zlar:', kichik)
print('4-6 harfli so\'zlar:', ortacha)
print('>6 harfli so\'zlar:', uzun)        