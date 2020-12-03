with open("input") as f:
    data = f.readlines()
valid = 0
for x in data:
    mi = int(x.split("-")[0])
    ma = int(x.split("-")[1].split(" ")[0])
    l = x.split(" ")[1][0]
    password = x.split(" ")[2][:-1]
    val = 0
    if password[mi-1] == l:
        val += 1
    if password[ma-1] == l:
        val +=1
    if val == 1:
        valid += 1
    #print("min: "+str(mi)+" max: "+str(ma)+" - "+l+" password: "+password)
print(valid)

