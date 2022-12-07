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
fromage=["Gruyere","Mozarella","Emmantal"]
print("Vous avez donc choisi une pizza de "+taille[pizza[0]-1]+" avec une base "+base[pizza[1]-1]+" et avec "+fromage[pizza[2]-1]+" comme fromage")
addfav=input("Souhaitez vous l'ajouter à vos pizzas favoris?")
if addfav=="1":
    lp2=open("pizzafav.txt", "a")
    nom=input("Quel nom souhaitez vous donnez à cette pizza?")
    Lines = lp.readlines()
    x=0
    for line in Lines:
        x=x+1
    lp2.write(str(int(x)/5)+":"+"/n"+"/t"+"Nom="+nom+"/n"+"/t"+"Diametre="+taille[pizza[0]-1]+"/n"+"/t"+"base="+base[pizza[1]-1]+"/t"+"ingredient="+fromage[pizza[2]-1])
else:
    print("Au revoir, merci de votre visite!")