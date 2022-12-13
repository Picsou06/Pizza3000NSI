from time import sleep
lp=open("ingredients PIZZA.txt", "r")
Lines = lp.readlines()
txtinput=[]
pizza=[]
nom=[]
lignes=0
for line in Lines:
    txtinput.append(line)
for i in txtinput:
    temp=i.split(" = ")
    nom.append(temp[0])
for ingredient in nom:
    print("Quel "+ingredient+" souhaitez vous pour votre pizza?")
    pizza.append(input(txtinput[lignes]))
    lignes=lignes+1
for i in txtinput:
    temp=i.split(" = ")
    nom.append(temp[1])
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