from numpy import array 

def long_ch(ch):
    # Fonction pour calculer la longueur d'une chaîne
    count = 0
    for _ in ch:
        count += 1
    return count

def saisir():
    n = int(input('Donner le nombre de personnes = '))
    return n

def chercher(x, T, n):
    trouve = False
    i = -1
    while (trouve == False) and (i != n):
        i = i + 1
        if T[i] == x:
            trouve = True
    return trouve

def remplir(T, n):
    # Saisie du premier ID (avec contrôle format)
    ok = False
    while ok == False:
        print('Donner ID n°0 :')
        T[0] = input()
        ok = (long_ch(T[0]) == 8) and T[0].isdecimal()
    # Saisie des IDs suivants (avec contrôle format ET unicité)
    for i in range(1, n):
        ok = False
        while ok == False:
            print('Donner ID n°', i, ':')
            T[i] = input()
            ok = (long_ch(T[i]) == 8) and T[i].isdecimal() and (chercher(T[i], T, i - 1) == False)

# Programme principal
n = saisir()
T = array([str] * n)
remplir(T, n)
```