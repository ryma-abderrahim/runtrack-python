#création de la foction arrondie_note
def arrondie_note(list):
    for i in range(len(list)):

        #si l'étudiant à réussi le teste et que ça note rempli le critère
        if (list[i]>=40)  and ((list[i]%5)>= 3):
            list[i]+=1
    return list

#initialisatin de la liste des notes
notes=[30,48,49,50,62,65,69,82,83,95,98]

#affichage de la liste 
print(notes)

#affichage de la liste arrondie
print(arrondie_note(notes))


    