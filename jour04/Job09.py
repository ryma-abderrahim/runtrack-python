#création de la fonction max
def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


#creation de la fonctio min
def min(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

#initialisation de la liste L
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

#affichage de la liste L
print(L)

#afficher le maximum de la liste L 
print("la valeur max est :", max(L))

#afficher le minimum de la liste L 
print("la valeur min est :", min(L))