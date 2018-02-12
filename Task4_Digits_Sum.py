# takes the digits and sum of digits from the user
digits = int(input("Enter the No of Digits "))
_sum = int(input("Enter The Sum of the Digits "))
num_string = ""
limit_string = ""

# method that creates the no of digits lower and upper limit
for x in range(digits):
    num_string = num_string + "1"
    limit_string = limit_string + "9"


# method that adds and prints out the numbers
def adding(para_num_string):
    # converting string into string
    _digits = [int(x) for x in str(para_num_string)]
    # Adding all the digits
    tempSum = sum(_digits)
    # checking if the sum of digits is equal to the total sum.
    if tempSum == _sum:
        # check the digits in ascending
        if isAscending(_digits):
            print(para_num_string)


# method to check the list is in ascending
def isAscending(para_list):
    previous = para_list[0]
    for number in para_list:
        if number < previous:
            return False
        previous = number
    return True


limit_int = int(limit_string)
num_int = int(num_string)
print()
# runs the loop until the limit is reached.
while num_int <= limit_int:
    num_string = str(num_int)
    adding(num_string)
    num_int += 1
input("Program Finished Running")