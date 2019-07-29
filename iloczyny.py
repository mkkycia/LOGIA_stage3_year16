def liczby(lista):
    wynik = []
    pom = []
    for i in lista:
        for j in range(1, i//2):
            if i % j == 0:
                pom = []
                pom.append(j)
                pom.append(i//j)
        if pom[0] > pom[1]:
            wynik.append([pom[1], pom[0]])
        else:
            wynik.append(pom)
    return wynik

print(liczby([13,44,42]))
        
            
