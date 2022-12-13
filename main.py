print("Chargement de Pizza3000...") #Affichage de Chargement de Pizza3000... (déco)

stop = 1 #Creation d'une varible stop pour la boucle
while stop==1: #Tant que Stop est egal à 1 :
    x= open("start.py", "r") #Creation de la variable x pour lire le fichier start.py
    exec(x.read()) #Lecture de la variable x donc lecture du fichier start.py