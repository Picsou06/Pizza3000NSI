print("Que souhaitez vous faire?") #Affichage de "Que souhaitez vous faire?"
print("") #Saute une ligne
print("1: Commander une pizza du menu") #Affichage de "1: Commander une pizza au menu"
print("") #Saute une ligne
print("2: Creer une pizza") #Affichage de "2: Creer une pizza"
print("") #Saute une ligne
print("3: Quitter") #Affichage de "3: Quitter"
print("") #Saute une ligne
choix=input("Choix?") #Creation d'une varible choix ou la valeur est demande
if choix=="1": #Si la variable choix est egale a 1:
    exec(open("./choixdepizza.py").read())
elif choix=="2": #Sinon si variable choix est egal 2
    exec(open("./creationpizza.py").read())
elif choix=="3": #Sinon si la variable choix est egal a 3
    stop=0 #La variable stop est desormais egale a 0
    print("Au revoir!") #Affichage de "Au revoir!"
else: #Sinon
    print("Ce choix n'est pas repertorie") #Affichage de "Ce choix n'est pas repertorie"