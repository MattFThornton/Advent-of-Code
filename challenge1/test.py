with open('chal1input') as f:
    data = f.readlines()
for x in data:
    for n in data:
        for u in data:
            if int(x) + int(n) + int(u) == 2020:
                print(int(x)*int(n) * int(u))
