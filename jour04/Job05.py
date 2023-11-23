#creation de la liste
L=[1 , 2 , 3 , 4 , 5]

#afficher la deuxième valeur de la liste L et la liste entière
print(L)
print(L[1])

#Creation d el afonction Somme_voisin 
def Somme_voisin(list , index):

    #la première case : on remplace la case voulue par la case qui la suit
    if index == 0 :
       list[index] = list[index + 1]
       return list
    
    #le dernière case : on remplace la case voulue par la cacse qui la précède
    elif index == len(list) - 1 :
        list[index] = list[index-1]
        return list

    #au milieu de la liste : on remplace la case voulue par la somme de la case qui la suit et la case qui la précède
    else:
        list[index]= (list[index+1]) + (list[index-1])
        return list


#appel à la fonction Somme_voisin
print(Somme_voisin(L, 3))

#afficher la dernière valeur de la list L
print (L[(len(L))-1])
