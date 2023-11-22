#creation de la fonction 
def Inverse ( string):
    #crear une chaine de caractère vide 
    inverse_String=""

    #ajouter les caractère de la chaine string dans la chian vide invers_string en comançant de la fin
    for i in range(len(string)-1 ,-1 ,-1):
        inverse_String+=(string[i])

    return inverse_String


#appel à la fonction Inverse
print(Inverse("ABCDEFG"))