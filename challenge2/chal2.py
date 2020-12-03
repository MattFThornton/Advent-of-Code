with open("input") as f:
    data = f.readlines()
valid = 0
for x in data:
    mi = int(x.split("-")[0])
    ma = int(x.split("-")[1].split(" ")[0])
    l = x.split(" ")[1][0]
    password = x.split(" ")[2][:-1]
    i = 0
    for n in password:
        if n == l:
            i+=1
    tempval = 0
    if i >= mi and i <= ma:
        valid += 1
        tempval = 1
    print("min: "+str(mi)+" max: "+str(ma)+" - "+l+" password: "+password + " valid?: "+ str(tempval) )
print(valid)

