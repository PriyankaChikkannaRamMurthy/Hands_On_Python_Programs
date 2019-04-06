'''
Program 3:
Below is the python program that verifies a positive integer from the user to be  a prime, 
composite or neither prime or composite and prints the message accordingly.

Logic:
* Have written a function "primenum" which takes in one argument which is the number to be tested to be a
prime or composite number. For loop is incorporated with numbers ranging from 2 to that number entered by user.
* We assume from 2 as 0 and 1 are considered to be neither Prime nor Composite. 
* Later we check for the factors of the number by dividing and checking the remainder to be 0  for a composite number where the if loop returns
False telling it to be a Composite number. In the else loop we return True meaning it is a Prime number
without any factors other than 1 and itself. 
* The user is prompted for the number and is casted for int datatype. 
* If condition loop is written for the number to be greater than or equal to 0 with first if loop condition 
checking for 0 or 1 where it prints it to be "Neither prime nor composite" on entering the loop
* In the elif loop the number is greater than 1 ,it enters the loop where it gives the control flow to the 
primenum function and expects the output to be True or False.
* If false then it prints "It is composite" and true then it prints "It is Prime"
* Else prints "Error: You did not enter a positive integer"

'''
#function for prime number check with one argument as input
def primenum(x):
    #checking for the factors of the number 
    for n in range(2,x):
        #checking with if loop for remainder to be 0 on dividing the number with numbers starting from 2 till it.
        if (x % n) == 0:
            #if factors found return false claiming it to be composite number
            return False
            break
    else:
        #if not found return true claiming it to be a prime number
        return True

#prompting the user for th input
raw_inp = input('Enter positive integer:')
try:
    #casting the numer to an int datatype
    pos_num = int(raw_inp)
except:
    pos_num = -1

#if condition loop for checking the number to be greater than or equal to 0
if(pos_num >= 0):  
#if condition loop for checking the number to be equal to 0 or 1
    if(pos_num == 0 or pos_num == 1):
        print('It is neither prime nor composite')
#if condition loop for checking the number to be greater than 1
    elif(pos_num > 1):
        #assigning the return value of function primenum by passing the input number as argument
        output = primenum(pos_num)
#if condition loop for checking the output to be false
        if(output == False):
        #then the number is composite
            print('It is a composite')
            #if condition loop for checking the output to be true
        elif(output == True):
            #then the number is prime
            print('It is a prime')
        else:
            print('none of the above')
    else:
        print('Error: You did not enter a positive integer')
else:
    #else condition loop for number other than integer datatype and lesser than 0
    print('Error: You did not enter a positive integer')
    
