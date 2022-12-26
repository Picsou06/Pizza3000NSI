from main import money
from time import sleep # importation de sleep
lp=open("pizzafav.txt", "r") #Creation d'une varible lp
p=lp.read() #Creation d'une varible p qui est egale
print(p)  #Affichage du contenu de la variable p
lp=open("pizzafav.txt", "r")#Mise a jour de la variable lp
Lines = lp.readlines()#Creation de la variable Lines
pizza=[]#Creation de la variabe pizza
x=0#Mise à jour de la varible x
for line in Lines:#Repeter Lines fois
    x=x+1#Mise a jour de la variable x
    pizza.append(line)#Ajout dans la variable pizza de la variable line
x=x/6#Mise a jour de la variable x
choix=0#Creation de la variabe choix
while choix>x or int(choix)<1:#Tant que choix > x ou choix < 1
    choix=int(input("Quel pizza souhaitez vous commander?"))#Mise a jour de la variable choix
#recupération du prix:
l=(choix-1)*6+5#Mise a jour de la variable l
prix=pizza[l]
prix=prix.split("=")
prix=int(prix[1])
if prix<money:
    money=money-prix
    print("Merci de votre commande de:")#Affichage de "Merci de votre commande de"
    l=(choix-1)*6#Mise a jour de la variable l
    for i in range(5):#Repeter 4 fois
        l=l+1#Mise a jour de la variable l
        print(pizza[l])#Afficher le 2eme element de la variable pizza
    sleep(3)#Attendre 3 secondes
else:
    print("Vous n'avez pas assez d'argent pour acheter cette pizza!")

