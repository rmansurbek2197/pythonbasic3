def hisobla(x):
    kvadrat = x ** 2
    kub = x ** 3
    return kvadrat, kub

son = int(input("Son kiriting: "))
kvadrat, kub = hisobla(son)
print(f"Sonning kvadrati: {kvadrat}, kubi: {kub}")