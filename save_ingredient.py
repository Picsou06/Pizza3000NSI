lp=open("ingredients PIZZA.txt", "r")
vi=open("variableingredients.txt", "a")
Lines = lp.readlines()
txtinput=[]
nom=[]
autre=[]
ingredient=[]
for line in Lines:
    txtinput.append(line)
for i in txtinput:
    temp=i.split(" = ")
    nom.append(temp[0])
    autre.append(temp[1])
for i in ingredient:
    temp=i.split(" ")
    ingredient.append(temp)
for i in range(nom):
    vi.write(nom[i]+"="+ingredient[i])