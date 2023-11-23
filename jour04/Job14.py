#création de  la fonction length 
def length(list):
    count=0
    for i in list:
        count+=1
    return count

#création de la fonction my_long_word
def my_long_word(n , String): 
    word=""  #variable qui va récupérer les mots
    new_String=""  #variable qui va prendre  le résultat de la fonction 

    for char in String :
        #si le char n'est ni un espace ni un point vergule en stocke le char dans word
        if (char != " ") and (char != ","):
            word += char
        
        #sinon on récupère word et on le stocke dans new_string si il es plus long que 3 et on  réinisialise la variable word
        else:
            if length(word) > n :
                new_String += word
                new_String+=' '
                word=""
            
            #si le word es plus petit que 3 on le réinisialise
            else:
                word=""
            
    return new_String
        



word="La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à"
print(word)

#Test de la fonction my_long_word
print(my_long_word(3,word))


