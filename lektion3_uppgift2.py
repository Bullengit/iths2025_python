file = open("log.txt","r")

for line in file:
    line = line.strip()
    if "Failed login attempt" in line:
        print(line)
