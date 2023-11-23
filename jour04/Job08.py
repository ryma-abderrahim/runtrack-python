#création de la fonction sum_paire 
def sum_pair(list):
    somme = 0
    for i in list:
        if i % 2 == 0 :
            somme += i
    return somme

#initialisation de la list L
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

#afficher la liste 
print( L)

#afficher la somme des nombres pairs de la list L
print("la somme des nombres paire de la liste L est : ",sum_pair(L))

