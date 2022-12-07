from time import sleep
lp=open("pizzafav.txt", "r")
p=lp.read()
print(p)
lp=open("pizzafav.txt", "r")
Lines = lp.readlines()
pizza=[]
x=0
for line in Lines:
    x=x+1
    pizza.append(line)
x=x/5
choix=0
while choix>x or int(choix)<1:
    choix=int(input("Quel pizza souhaitez vous commander?"))
print("Merci de votre commande de:")
l=0
l=(choix-1)*5
for i in range(4):
    l=l+1
    print(pizza[l])
sleep(3)

