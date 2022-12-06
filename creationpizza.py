lp=open("pizzafav.txt", "w")
print("Quel taille souhaitez vous pour votre pizza?")
txtinput=fic.readline(1)
taille=0
pizza=[]
while taille>=1 and taille<=3:
    taille=input(txtinput)
pizza.append(taille)
print("Quel base souhaitez vous?")
txtinput=fic.readline(3)
base=0
while base>=1 and base<=4:
    base=input(txtinput)
pizza.append(base)
print("Quel fromages souhaitez vous?")
txtinput=fic.readline(5)
fromage=0
while fromage>=1 and fromage<=4:
    fromage=input(txtinput)
pizza.append(fromage)
print(pizza)