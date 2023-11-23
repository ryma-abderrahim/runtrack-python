#creation de la fonction List
def List(String):
    fruits=["pomme", "cerise", "orange"]
    #La méthode append permet d'ajouter un élement à la fin  d'une liste en python 
    fruits.append(String)
    return fruits



#appel de la fonction List
print(List("Melon"))