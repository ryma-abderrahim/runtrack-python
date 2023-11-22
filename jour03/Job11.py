import math
#création de la fonctione time_to_texte
def time_to_texte (num):
    if num<0:
        return  print("erreur")

    if num<60  and num>=0:
        return print("0 heures et ",num,"minutes")
    else:
        #récupérer la partie entière de résultat de la dévision et le reste de la dévision 
        return  print(math.floor(num / 60)," heures et  ", num%60 ,"minutes")
    

#apple à la fonction time_to_texte
time_to_texte(60)
time_to_texte(150)
time_to_texte(50)
time_to_texte(-50)

