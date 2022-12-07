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
while fromage<1 or fromage>4:
    fromage=int(input(txtinput[2]))
pizza.append(fromage)
print(pizza)
taille=["29cm","33cm","40cm"]
base=["Sauce Tomates","Creme fraiche","Huile d'olives","Aucune"]
fromage=["Gruyere","Mozarella","Emmental","Cantal"]
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