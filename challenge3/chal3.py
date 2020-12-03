# 31x323
#284
right = 3
down = 1
with open("input") as f:
    temp = f.readlines()
    data = []
    for x in temp:
        temp2 = []
        for n in x:
            if n != "\n":
                temp2.append(n)
        data.append(temp2)

def slopecheck(right,down):        
    cright = 0
    cdown = 0
    tree = 0
    i = 0
    while cdown < 323:
        check = data[cdown][cright]
        if check == "#":
            tree += 1
        cright += right
        cdown += down
        i += 1
        if cright >= 31:
            cright = cright-31
    return tree
#challenge 1
#print(slopecheck(3,1))
#challenge 2
#print(slopecheck(1,1) * slopecheck(3,1) * slopecheck(5,1) * slopecheck(7,1) * slopecheck(1,2))
