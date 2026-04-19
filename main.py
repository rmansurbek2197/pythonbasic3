def juft_toq_ajratish(sonlar):
    juft_sonlar = []
    toq_sonlar = []
    for son in sonlar:
        if son % 2 == 0:
            juft_sonlar.append(son)
        else:
            toq_sonlar.append(son)
    return juft_sonlar, toq_sonlar

def asosiy_funktsiya():
    sonlar = [12, 34, 56, 78, 23, 45, 67, 89, 10, 20]
    juft, toq = juft_toq_ajratish(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

def boshqa_funktsiya():
    sonlar = [15, 25, 35, 45, 55, 65, 75, 85, 95]
    juft, toq = juft_toq_ajratish(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

def yana_bir_funktsiya():
    sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    juft, toq = juft_toq_ajratish(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

def qoshimcha_funktsiya():
    sonlar = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    juft, toq = juft_toq_ajratish(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

asosiy_funktsiya()
boshqa_funktsiya()
yana_bir_funktsiya()
qoshimcha_funktsiya()

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft, toq = juft_toq_ajratish(sonlar)
print("Juft sonlar:", juft)
print("Toq sonlar:", toq)

sonlar = [15, 25, 35, 45, 55, 65, 75, 85, 95]
juft, toq = juft_toq_ajratish(sonlar)
print("Juft sonlar:", juft)
print("Toq sonlar:", toq)

sonlar = [12, 34, 56, 78, 23, 45, 67, 89, 10, 20]
juft, toq = juft_toq_ajratish(sonlar)
print("Juft sonlar:", juft)
print("Toq sonlar:", toq)