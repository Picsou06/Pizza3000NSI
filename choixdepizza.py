import re
lp=open("pizzafav.txt", "r")
ch=lp.read()
print(ch)
z=re.split(":")
print(z)
choix=input("Veuillez choisir une pizza:")
print("Merci de votre commande de:")
print(z[choix-1])
choix=input("Souhaitez vous commander autre chose? 0: Non, 1: Oui")
if choix==0:
    stop=0
    print("Au revoir!")
elif choix==1:
    exec(open("./start.py").read())
else:
    print("Erreur, choix innexistant")

