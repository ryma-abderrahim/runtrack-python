#creation de la fonction length qui compte le nombre de valeur de la liste
def length(list):
    count=0
    for i in list:
        count+=1
    return count


#creation de la fonction tri 
def tri(list):
    len=length(list)
    #on compare chaque élément de la liste au valeurs suivante 
    for i  in range (len-1):
        for j in range (i+1 ,len):
            if list[i]>list[j]:
                l=list[i]
                list[i]=list[j]
                list[j]=l
    return list


#création de la fonction round qui arroundi les nombres
def round_number(number):
    integer=int(number)   #récupération de la partie entière de number
    decimal=number-integer  #récupération de la partie decimale de number

    #si la partie decimale est >5 on rajoute 1
    if decimal >= 0.5:
        number = integer + 1 
    #sinon on garde on retourne le number
    else: 
        number=integer
     
    return number


#fonction round list 
def round_list(list):
    for i in range(length(list)) :
        list[i]= round_number(list[i])
    
    return list 


#initialiation de la liste L
L=[22.4, 4.0, 16.22, 9.10, 11.00,12.22, 14.20, 5.20, 17.50]

print(L)

#aroundir la liste puis l'afficher dans l'ordre
liste_arrondi=(round_list(L))
print(liste_arrondi)
print(tri(liste_arrondi))
