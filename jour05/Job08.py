#foction tri
def my_sort(list):
    count=0
    #on compare chaque élément de la liste au valeurs suivante 
    for i  in range (len(list)-1):
        for j in range (i+1 ,len(list)):
            if list[i]>list[j]:
                l=list[i]
                list[i]=list[j]
                list[j]=l
                count+=1
    return list , count


#initialisation de l liste L
L=[9 , 40 ,89 ,3,7 ,0 ,29]

#affichage de la fonction sort
print("Nombre totalde coups nécessaires pour trier la liste :", my_sort(L)[1])
print("Liste triée: ", my_sort(L)[0])