print("Que souhaitez vous faire?") #Affichage de "Que souhaitez vous faire?"
print("") #Saute une ligne
print("1: Commander une pizza du menu") #Affichage de "1: Commander une pizza au menu"
print("") #Saute une ligne
print("2: Creer une pizza") #Affichage de "2: Creer une pizza"
print("") #Saute une ligne
print("3: Quitter") #Affichage de "3: Quitter"
print("") #Saute une ligne
choix=input("Choix?") #Creation d'une varible choix
if choix=="1": #Si la variable 
    exec(open("./choixdepizza.py").read())
elif choix=="2":
    exec(open("./creationpizza.py").read())
elif choix=="3":
    stop=0
    print("Au revoir!") #Affichage de "Au revoir!"
else:
    print("Ce choix n'est pas repertorie") #Affichage de "Ce choix n'est pas repertorie"