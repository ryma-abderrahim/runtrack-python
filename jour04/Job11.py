#dcreation de la fonction augmente de 1
def augmente (list):
    for i in range(len(list)):
        list[i] = list[i] + 1
    return list

#initialisation de la liste L
L = [7, 11, 42, 39, 2]

#affichage de la liste L
print(L)

#appel à la fonction augmente 
print ( augmente(L))
