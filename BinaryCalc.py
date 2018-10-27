# program to calculate binary number from integer
# prompt user to enter integer 
number = int(input("Enter number: "))
reverse_code = ""
# calculate binary number or give warning if incorrect number type entered
if number > 0:
    while number != 0:
        if number % 2 == 0:
            code = "0"
        else:
            code = "1"
        new_number = number //2
        number = new_number
        reverse_code = code + reverse_code
        print (reverse_code)
else:
    print ("Invalid Input. System will now self-destruct.")
