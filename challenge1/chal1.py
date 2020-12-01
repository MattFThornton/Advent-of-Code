with open('chal1input') as f:
    data = f.readlines()
for x in range(0,len(data)):
    for n in range(1,len(data)):
        if int(data[x]) + int(data[n])) == 2020:
            print(int(data[x]) + int(data[n]))
            print(int(data[x])*int(data[n]))
