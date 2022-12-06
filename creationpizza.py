lp=open("pizzafav.txt", "w")
print("Quel taille souhaitez vous pour votre pizza?")
txtinput=lp.readline(1)
taille=0
pizza=[]
while taille>=1 and taille<=3:
    taille=input(txtinput)
pizza.append(taille)
print("Quel base souhaitez vous?")
txtinput=lp.readline(3)
base=0
while base>=1 and base<=4:
    base=input(txtinput)
pizza.append(base)
print("Quel fromages souhaitez vous?")
txtinput=lp.readline(5)
fromage=0
while fromage>=1 and fromage<=4:
    fromage=input(txtinput)
pizza.append(fromage)
print(pizza)
taille={"29cm","33cm","40cm"}
base={"Sauce Tomates","Creme fraiche","Huile d'olives","Aucune"}
fromage={"Gruyere","Mozarella","Emmantal"}
print("Vous avez donc choisi une pizza de "+taille[base[0]-1]+" avec une base "+taille[base[1]-1]+" et avec "+taille[base[2]-1]+" comme fromage")