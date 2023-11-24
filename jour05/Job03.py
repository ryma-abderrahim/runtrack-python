#creation de la fonction draw_triangle
def draw_triangle(height):
    for i in range(height-1):
      print(((height-1)-i) * " " +"/" + " " * (i *2)+ "\\")

    #la dernière ligne de triangle 
    print( "/" + "_" * ((2*height)-2) + "\\")


#initialisation de l'argument height
height=int(input("Entrez la hauteur de triangle : "))


#appel à la fonction draw_trinagle
draw_triangle(height)