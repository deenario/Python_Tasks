
num = int(input("How many tables do you want? "))
for x in range(num+1):
    print(x,"\t",end="")
print("")
for x in range(num):
    print("_____",end="")
print("")
for x in range(num):
    print(x+1," | ",end="")
    for y in range(num):
        _sum = (x+1)*(y+1)
        print(_sum, "\t",end="")
    print("")