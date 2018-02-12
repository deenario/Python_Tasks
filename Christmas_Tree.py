
height = int(input("Enter the height of the Christmas Tree "))
for k in range(3):
    if k==0:
        stars = 1
        spaces = height
    else:
        stars = 3
        spaces = height-1
    for x in range(height):
            for y in range(spaces):
                print(" ",end="")
            for z in range(stars):
                print("*",end="")
            print("")
            spaces -=1
            stars +=2
for x in range(height):
    for x in range(height):
        print(" ",end="")
    print("**")