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
x=x/5#Mise a jour de la variable x
choix=0#Creation de la variabe choix
while choix>x or int(choix)<1:#Tant que choix > x ou choix < 1
    choix=int(input("Quel pizza souhaitez vous commander?"))#Mise a jour de la variable choix
print("Merci de votre commande de:")#Affichage de "Merci de votre commande de"
l=0#Creation de la variabe l
l=(choix-1)*5#Mise a jour de la variable l
for i in range(4):#Repeter 4 fois
    l=l+1#Mise a jour de la variable l
    print(pizza[l])#Afficher le 2eme element de la variable pizza
sleep(3)#Attendre 3 secondes

