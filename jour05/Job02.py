#creation de la fonction draw_rectangle
def draw_rectangle(width,height):
    print ("|"  + "-" * (width-2) +"|")
    for i in range(height-2):
        print("|" + " " * (width-2) + "|")
    print ("|"  + "-" * (width-2) +"|")
        
#initialisation des input width et height
width=int(input("Entrez la largeur de rectangle: "))
height=int(input("Entrze la longeur de rectangle:"))

#appele à la fonction draw_rectangle
draw_rectangle(width,height)