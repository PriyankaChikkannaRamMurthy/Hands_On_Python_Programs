'''Program 2: Number Guessing Game

Algorithm: • The program takes the users input for the number to be guessed and converts into integer • if the user_input is in the range of 0 and 100 inclusive enters the if condition with initializing the iteration variable to 0 and running the while loop for true condition until it encounters the break condition • the computer choice of selection is chosen between 1 and 100 inclusive with randint method of random module. • if condition loop whenever the user_input and the computer guessed number are same, then it prints the number of iterations and the guessed number and breaks the loop else it increments the counter variable and runs the next iteration. • else the option is said to be incorrect asking the user to input the correct input choice between 1 and 100

Instructions: Select the cell and click "Run" from the upper tab options to execute the cell and input the user choice accordingly

Expected results: Enter number to be guessed: 1 You guessed 1 ,and it took the program 99 iterations

Enter number to be guessed: 450 Enter valid input between 1 and 100 (inclusive)...exiting the program'''

from random import randint

raw_input = input("Enter number to be guessed: ")
try:
    user_inp = int(raw_input)
except:
    user_inp = -1

if(0 < user_inp < 101):
    iter_count = 0
    while True:
        comp_guess = randint(1,100)
        iter_count = iter_count + 1
        if(user_inp == comp_guess):
            print("You guessed",user_inp,",and it took the program",iter_count,"iterations")
            break
else:
    print("Enter valid input between 1 and 100 (inclusive)...exiting the program")
    
