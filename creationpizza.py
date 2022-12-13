from time import sleep
lp=open("ingredients PIZZA.txt", "r")
Lines = lp.readlines()
txtinput=[]
for line in Lines:
    txtinput.append(line)
print("Quel taille souhaitez vous pour votre pizza?")
taille=0
pizza=[]
while taille<1 or taille>3:
    taille=int(input(txtinput[0]))
pizza.append(taille)
print("Quel base souhaitez vous?")
base=0
while base<1 or base>4:
    base=int(input(txtinput[1]))
pizza.append(base)
print("Quel fromages souhaitez vous?")
fromage=0
while fromage<1 or fromage>11:
    fromage=int(input(txtinput[2]))
pizza.append(fromage)
print("Quel supplement souhaitez vous?")
supplement=0
while supplement<1 or supplement>8:
    supplement=int(input(txtinput[3]))
print("Quel supplement souhaitez vous?")
huile=0
while huile<1 or huile>2:
    huile=int(input(txtinput[4]))
pizza.append(huile)
Taille=['29cm', '33cm', '40cm']
Base=['Sauce_Tomates', 'Creme_fraiche', "Huile_d'olives", 'Aucune']
Fromages=['Gruyere', 'Mozarella', 'Emmantal', 'Cantal', 'Gorgonzola', 'Cheddar', 'Conte', 'Chevre', 'Roquefort', 'Roblechon', 'Aucun']
Supplement=['Steak_Hache', 'Saumon', 'Olives', 'Champignon', 'Basilic', 'Anchois', 'Frittes', 'Aucun']
Huile=['Huile_Piquante', 'Aucun']
print("Vous avez donc choisi une pizza de "+taille[pizza[0]-1]+" avec une base "+base[pizza[1]-1]+" et comme ingredients:"+fromage[pizza[2]-1])
addfav=input("Souhaitez vous l'ajouter a vos pizzas favoris?")
if addfav=="1":
    lpa=open("pizzafav.txt", "a")
    lpr=open("pizzafav.txt", "r")
    nom=input("Quel nom souhaitez vous donnez a cette pizza?")
    Lines = lpr.readlines()
    x=0
    for line in Lines:
        x=x+1
    x=x/5
    x=int(x+1)
    lpa.write("\n"+str(x)+":"+"\n"+"\t"+"Nom="+nom+"\n"+"\t"+"Diametre="+taille[pizza[0]-1]+"\n"+"\t"+"base="+base[pizza[1]-1]+"\n"+"\t"+"ingredient="+fromage[pizza[2]-1])
    print("Pizza ajoute a vos favoris!")
else:
    print("Au revoir, merci de votre visite!")
lpa.close
sleep(3)