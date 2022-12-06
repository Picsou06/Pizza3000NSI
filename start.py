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
    ch=lp.read()
    print(ch)
    choix=input("Veuillez choisir une pizza:")
elif choix=="2":
    print("Hey2")
elif choix=="3":
    print("Hey3")
else:
    print("Ce choix n'est pas répertorié")