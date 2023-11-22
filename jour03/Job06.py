#création de la fonction
def Positive_Negative(num):
    if num > 0:
        return "Positif"
    elif num < 0:
        return "Négatif"
    else:
        return "Zéro"
    

#utilisation de la fonction
print(Positive_Negative(-2))
print(Positive_Negative(8))
print(Positive_Negative(0))