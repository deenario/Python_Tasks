
height = int(input("Enter the height of the Diamond "))
stars = 1
spaces = height

for x in range(height):
    for y in range(spaces):
        print(" ",end="")
    for z in range(stars):
        print("*",end="")
    print("")
    spaces -=1
    stars +=2
for a in range(height+1):
    for c in range(spaces):
        print(" ", end="")
    for b in range(stars):
        print("*",end="")
    print("")
    spaces +=1
    stars -=2