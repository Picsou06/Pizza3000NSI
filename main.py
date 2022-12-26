print("Chargement de Pizza3000...") #Affichage de Chargement de Pizza3000... (déco)
money=50
nomdelamoney=" Euros"
print("Vous possedez actuellement "+str(money)+nomdelamoney)

stop = 1 #Creation d'une varible stop pour la boucle
while stop==1: #Tant que Stop est egal à 1 :
    if money>=0:
        x= open("start.py", "r") #Creation de la variable x pour lire le fichier start.py
        exec(x.read()) #Lecture de la variable x donc lecture du fichier start.py
    else:
        print("Vous devez travailler pour gagner de l'argent!")
        exec(open("./creationpizza.py").read())