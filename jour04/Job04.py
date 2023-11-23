#creation de la fonction List
def List(String):
    fruits=["pomme", "cerise", "orange", "Melon"]
    #La méthode list.insert(index,element) permet d'ajouter un élement a i  d'une liste en python 
    fruits.insert(2,String)
    return fruits



#appel de la fonction List
print(List("Mangue"))