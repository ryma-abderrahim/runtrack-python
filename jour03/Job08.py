#creation de la fonction
def function(type,saison):
    if (type == "fruits") and (saison == "hiver"):
        print("orange, mandarine et kiwi")
    
    elif (type == "fruits") and (saison == "ete"):
        print("poire, fraise, cassis")
    
    elif (type == "legume") and (saison == "hiver") :
        print("carotte, topinambour ,endive")
    
    elif (type == "legume") and (saison == "ete"):
        print("artichaut, aubergine, navet")

    else :
        print ("vegetal indesponible")


#appel de la fonction
function("fruits","hiver")
function("fruits","ete")
function("legume","hiver")
function("legume","ete")
function("vegetal","hiver")