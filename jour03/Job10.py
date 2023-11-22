#creation de la fonction
def Paire_Impaire(num):

    #verification de validité de paramètre ( entier et positive )
    if (type(num) != int)  or (num <=0) :
        return "Erreur"
    
    #calcul de la paire et de l'impair
    if num % 2 == 0:
        return "Paire"
    else :
        return "Impaire"
    
#Appel à la fonction Paire_impaire
print(Paire_Impaire(2))
print(Paire_Impaire(3))
print(Paire_Impaire(-3))
print(Paire_Impaire("a"))