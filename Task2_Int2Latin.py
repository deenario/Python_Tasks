# List that Shows the Latin Representation of all the Integers.
LatinRep = [(1000000,'-M'),(900000,'-CM'),(500000,'-D'),(100000,'-C'),(90000,'-XC'),(50000,'-L'),(10000,'-X'),(9000,'-IX'),
            (5000,'-V'),(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')]


# A function that takes an integers and returns a string Representation in Latin.
def integerToLatin(_Number):
    Latin = ''
    # a while loop that checks if the number is greater than 0 as 0 cannot be represented in Latin.
    while _Number > 0:
        # for loop to take the two elements of the list and compare then with the given integer.
        for i, r in LatinRep:
            while _Number >= i:
                # adding latin symbols one by one.
                Latin += r
                _Number -= i

    # returns the latin representation
    return Latin


Number = 1
while Number > 0:
    # asks user to input the integer.
    Number = int(input("Enter Integer Between (1 - 999,999) which you want to convert or enter 0 to exit: "))
    # calls the function and shows the number.
    if Number < 1000000:
        print("The Latin representation of the Number ", Number, " is ", integerToLatin(Number))
        print()
    else:
        print("The Number is greater than 999999")
input("Program Finished Running")
