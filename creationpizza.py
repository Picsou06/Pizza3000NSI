from main import money#Importation de money
from time import sleep#Importation de sleep


taille=0#Creation de la variable taille
pizza=[]#Creation de la variable pizza
base=0#Creation de la variable base
supplement=0#Creation de la variable supplement
fromage=0#Creation de la variable fromage

lp=open("ingredients PIZZA.txt", "r")#Creation d'une varible lp
Lines = lp.readlines()#Creation de la variable Lines
txtinput=[]#Creation de la variable txtinput

for line in Lines:#Repeter Lines fois
    txtinput.append(line)#Ajout dans la variable txtinput de la variable line

print("Quel taille souhaitez vous pour votre pizza?")#Affichage de "Quel taille souhaitez vous pour votre pizza?" 
while taille<1 or taille>3:#Tant que taille<1 ou taille>3
    taille=int(input(txtinput[0]))#Mise a jour de la variable taille
pizza.append(taille)#Ajout dans la variable pizza de la variable taille
print("Quel base souhaitez vous?")#Affichage de "Quel base souhaitez vous?"

while base<1 or base>4:#Tant que base<1 ou base>4
    base=int(input(txtinput[1]))#Mise a jour de la variable base
pizza.append(base)#Ajout dans la variable pizza de la variable base
print("Quel fromages souhaitez vous?")#Affichage de "Quel fromages souhaitez vous?"

while fromage<1 or fromage>11:#Tant que fromage<1 ou fromage>11
    fromage=int(input(txtinput[2]))#Mise a jour de la variable fromage
pizza.append(fromage)#Ajout dans la variable pizza de la variable fromage

nb=input("Combien de supplement souhaitez vous?")
print("Quel supplement souhaitez vous?")#Affichage de "Quel supplement souhaitez vous?"
for i in range(nb):
while supplement<1 or supplement>8:#Tant que supplement<1 ou s'il est >8
    supplement=int(input(txtinput[3]))#Mise a jour de la variable supplement
    supplementls.append(supplement)#Ajout dans la variable pizza de la variable supplement

Taille=['29cm', '33cm', '40cm']#Creation de la variable Taille
Base=['Sauce_Tomates', 'Creme_fraiche', "Huile_d'olives", 'Aucune']#Creation de la variable Base
Fromages=['Gruyere', 'Mozarella', 'Emmental', 'Cantal', 'Gorgonzola', 'Cheddar', 'Conte', 'Chevre', 'Roquefort', 'Roblechon', 'Aucun']#Creation de la variable Fromages
Supplement=['Steak_Hache', 'Saumon', 'Olives', 'Champignon', 'Basilic', 'Anchois', 'Frites']#Creation de la variable Supplements
for i in supplementls:
    supplement=Supplement(int(i)-1)+" "
print("Vous avez donc choisi une pizza de "+Taille[pizza[0]-1]+" avec une base "+Base[pizza[1]-1]+" et comme ingredients:"+Fromages[pizza[2]-1]+", "+supplement) #Affichage de "Vous avez donc choisi une pizza de "+taille[pizza[0]-1]+" avec une base "+base[pizza[1]-1]+" et comme ingredients:"+Fromages[pizza[2]-1]+", "+Supplement[pizza[3]-1]
addfav=input("Souhaitez vous l'ajouter a vos pizzas favoris?(1: Oui, autre: Non)")#Creation de la variable addfav

if addfav=="1":#Si addfav=1
    lpa=open("pizzafav.txt", "a")#Creation de la variable lpa
    lpr=open("pizzafav.txt", "r")#Creation de la variable lpr
    nom=input("Quel nom souhaitez vous donnez a cette pizza?")#Creation de la variable nom
    prix=input("Quel prix voulez vous donnez a cette pizza?")
    Lines = lpr.readlines()#Mise a jour de la variable Lines
    x=0#Creation de la variable x
    for line in Lines:#Repeter Lines fois
        x=x+1#Mise a jour de la variable x
    x=x/6#Mise a jour de la variable x
    x=int(x+1)#Mise a jour de la variable x
    lpa.write("\n"+str(x)+":"+"\n"+"\t"+"Nom="+nom+"\n"+"\t"+"Diametre="+Taille[pizza[0]-1]+"\n"+"\t"+"base="+Base[pizza[1]-1]+"\n"+"\t"+"ingredient=")#Ecriture dans le fichier pizzafav.txt
    lpa.write(Fromages[pizza[2]-1]+" et "+supplement+"\n"+"\t"+"Prix="+str(prix))#Ecriture dans le fichier pizzafav.txt
    print("Pizza ajoute a vos favoris!")#Affichage de "Pizza ajoute a vos favoris!"
    money=money+20#Mise a jour de la variable money
    lpa.close()#Fermeture de fichier pizzafav.txt
else:#Sinon
    print("Au revoir, merci de votre visite!")#Affichage de "Au revoir, merci de votre visite!"

sleep(2)#Attendre 2sec
