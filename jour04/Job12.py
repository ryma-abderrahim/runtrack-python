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


#creation de la list 
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

#afficher la liste 
print(L)


#trier la liste avec l afonctio tri et l'afficher
print(tri(L))

