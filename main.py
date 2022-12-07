with open("start.py", "r") as f:
    print("Chargement de Pizza3000...")
    content = f.read()

stop = 1
while stop==1:
    exec(content)