lp=open("ingredients PIZZA.txt", "r")
vi=open("variableingredients.txt", "w")
Lines = lp.readlines()
txtinput=[]
nom=[]
autre=[]
ingredient=[]
ingredientt=[]
for line in Lines:
    txtinput.append(line)
for i in txtinput:
    temp=i.split(" = ")
    nom.append(temp[0])
    autre.append(temp[1])
for i in autre:
    temp=i.split(" ")
    ingredientt.append(temp)
for i in ingredientt:
    temp=[]
    for j in range(len(i)):
        if j%2!=0:
            temp.append(i[j])
    ingredient.append(temp)
for i in range(len(nom)):
    ch=str(nom[i])+"="+str(ingredient[i])+"\n"
    ch.rstrip()
    ch.encode('utf-8')
    vi.write(ch)
vi.close()