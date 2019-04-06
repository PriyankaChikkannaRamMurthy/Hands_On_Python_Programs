'''
Problem 2:
 Below is the python program that accepts 3 integers or 4 integers from the user which determines whether its 
 3 or 4 integers respectively. Later based on the number of integers it computes the average and maximum of the integers.
 
Logic:
* It prompts the user for the total number of integers to be entered to be either 3 or 4. On entering other 
than 3 or 4 integers it handles the exception by printing "Enter a valid set of 3 or 4 integers & Program ended...". 
* It enters a condition loop expecting the number entered to be greater than 0 where on encountering 3 it enters
another if condition loop of prompting the user to enter all the 3 digits of int data type otherwise it handles the exception 
'Enter valid format for the integers'
* On proper format of the number it computes the average of the integers by the given formula in the program
 and also it computes the maximum of the integers by using the 'max' function and prints out the average and the maximum
 of the 3 or 4 integers 
* If they are not 3 or 4 integers then it enters the else loop and prints 'Enter a valid set of 3 or 4 integers & Program ended...'

'''

#Prompting the user to enter 3 or 4 integers
raw_inp = input('Enter set of 3 or 4 integers:')
try:
    #casting the input to 'int' format
    num_int = int(raw_inp)
except:
    #setting to some value less than 0 for catching the exception
    num_int = -1

#condition check greater than 0 enter the loop
if(num_int > 0):
    #if condition loop for number check to be 3 
    if (num_int == 3):
        try:
            #Prompting the user for first number
            first_int = int(input('Enter first number:'))
            #Prompting the user for second number
            sec_int = int(input('Enter second number:'))
            #Prompting the user for third number
            third_int = int(input('Enter third number:'))
            #computing the average value
            avg_num = (first_int + sec_int + third_int)/num_int
            #printing the average value
            print('The average of',first_int,',',sec_int,'and',third_int,'is:',avg_num)
            #computing the maximum number 
            max_num = max(first_int, sec_int, third_int)
            #printing the maximum number
            print('The maximum of the three numbers is:',max_num)
        except:
            print('Enter valid format for the integers')
    #if condition loop for number check to be 4
    elif (num_int == 4):
        try:
            #Prompting the user for first number
            first_int = int(input('Enter first number:'))
            #Prompting the user for second number
            sec_int = int(input('Enter second number:'))
            #Prompting the user for third number
            third_int = int(input('Enter third number:'))
            #Prompting the user for fourth number
            fourth_int = int(input('Enter fourth number:'))
            #computing the average value
            avg_num = (first_int + sec_int + third_int + fourth_int)/num_int
            #printing the average value
            print('The average of',first_int,',',sec_int,',',third_int,'and',fourth_int,'is:',avg_num)
            #computing the maximum number 
            max_num = max(first_int, sec_int, third_int, fourth_int)
            #printing the maximum number
            print('The maximum of the four numbers is:',max_num)
        except:
            print('Enter valid format for the integers')
    else: 
        print('Enter a valid set of 3 or 4 integers & Program ended...')
else:
    print('Enter a valid set of 3 or 4 integers & Program ended...')
