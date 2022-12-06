with open("start.py", "r") as f:
    content = f.read()

stop = 1
while stop==1:
    exec(content)