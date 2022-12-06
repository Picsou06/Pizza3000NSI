lp=open("pizzafav.txt", "r")
print("Chargement de Pizza3000...")
print("Voici les pizzas disponibles:")
ch=lp.read()
print(ch)
print("Que souhaitez vous faire?")
print()
print("1: Selectionner une pizza")
print("")
print("2: Créer une pizza")
print("")
print("3: Quitter")
print("")
choix=input("Choix?")
if choix=="1":
    exec(open("./choixdepizza.py").read())
elif choix=="2":
    exec(open("./creationpizza.py").read())
elif choix=="3":
    x=0
    print("Au revoir!")
else:
    print("Ce choix n'est pas répertorié")