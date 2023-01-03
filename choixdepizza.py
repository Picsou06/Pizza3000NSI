from main import money # importation de money
from time import sleep # importation de sleep


lp=open("pizzafav.txt", "r") #Creation d'une variable lp
p=lp.read() #Creation d'une varible p qui est egale
print(p)  #Affichage du contenu de la variable p

lp=open("pizzafav.txt", "r")#Mise a jour de la variable lp
Lines = lp.readlines()#Creation de la variable Lines
pizza=[]#Creation de la variabe pizza
x=0#Mise à jour de la variable x

for line in Lines:#Repeter Lines fois
    x=x+1#Mise a jour de la variable x
    pizza.append(line)#Ajout dans la variable pizza de la variable line
x=x/6#Mise a jour de la variable x
choix=0#Creation de la variabe choix

while choix>x or int(choix)<1:#Tant que choix > x ou choix < 1
    choix=int(input("Quel pizza souhaitez vous commander? "))#Mise a jour de la variable choix
    
#recupération du prix:
l=(choix-1)*6+5#Mise a jour de la variable l
prix=pizza[l]#Mise à jour de la variable prix
prix=prix.split("=")#Mise à jour de la varible prix
prix=int(prix[1])#Mise à jour de la varible prix


if prix<money:#Si prix<money
    money=money-prix#Mise à jour de la variable 
    print("Merci de votre commande de:")#Affichage de "Merci de votre commande de"
    l=(choix-1)*6#Mise a jour de la variable l
    for i in range(5):#Repeter 4 fois
        l=l+1#Mise a jour de la variable l
        print(pizza[l])#Afficher le 2eme element de la variable pizza
    sleep(2)#Attendre 2 secondes
else:#Sinon
    print("Vous n'avez pas assez d'argent pour acheter cette pizza!")#Affichage de "Vous n'avez pas assez d'argent pour acheter cette pizza!"

