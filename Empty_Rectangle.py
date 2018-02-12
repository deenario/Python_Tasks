
height = int(input("Enter the Height of the Rectangle "))
width = int(input("Enter the Width of the Rectangle "))
for x in range(height):
    for y in range(width):
        if x==0 or x==height-1:
            print("*",end="")
        elif x>0 or x<height:
            if y==0 or y==width-1:
                print("*",end="")
            else:
                print(" ",end="")
    print("")