
height = int(input("Enter the height of the triangle "))
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