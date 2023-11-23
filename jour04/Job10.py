#création de la fonction produit_list 
def  produit_list(list , v1 ,  v2):
    produit=1
    if v1 == v2:
        return 0
    else:
        for i in list :
            if (i < v2) and (i > v1):
                produit = produit * i
        return produit
    

#initialisation de la liste L
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

#affichage de la liste 
print (L)

#calcule le produit de toutes les valeurs de la liste comprises dans l’intervalle [25, 90]
print (produit_list(L, 25, 90))