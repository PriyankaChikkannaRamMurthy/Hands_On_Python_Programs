'''Program 1: Rock-Paper-Scissors

Algorithm: • The program takes the input as the user’s choice of Rock paper scissors which are populated in the list. • random library is used from which the choice method is applied to the list and helps in the random selection of the choice as computer made that choice selection. • if user's choice and the computer's choice are the same, then there exists a tie else if compares it with the user’s choice of rock against scissors, wins and against paper, looses else if compares it with the user’s choice of paper against rock, wins and against scissors, looses else if compares it with the user’s choice of scissors against paper, wins and against rock, looses else the option is said to be incorrect asking the user to input the correct input choice • The rules for the logic is given as below: • Rock smashes scissors • Scissors cuts paper • Paper covers rock

Instructions: Select the cell and click "Run" from the upper tab options to execute the cell and input the user choice accordingly

Expected results: Enter your choice: ROCK Computer chooses rock User and computer tie! Enter your choice: Scissors Computer chooses rock I, the computer, win! Enter your choice: paper Computer chooses rock You, the user, win!

#importing the random module'''

#importing the random module
import random

#running the while loop until it hits the break
while True:
    #taking in the user's choice for rock or paper or scissors and converting to lower case
    user_input = input('Enter your choice: ').lower()
    # creating a list of choices
    choice_list = ['rock','paper','scissors']
    #selecting randomly from the choice_list using random module
    comp_choice = random.choice(choice_list)
    #printing the random choice selected
    print("Computer chooses ",comp_choice)
    
    #if condition loop for user_choice and computer_choice are same
    if (user_input == comp_choice):
        print("User and computer tie!")
    #for user_choice of 'rock' against computer's choice of 'scissors' and 'paper'
    elif (user_input == 'rock'):
        if(comp_choice == 'scissors'):
            print("You, the user, win!")
        else:
            print("I, the computer, win!")
    #for user_choice of 'paper' against computer's choice of 'scissors' and 'rock'
    elif (user_input == 'paper' ):
        if(comp_choice == 'rock'):
            print("You, the user, win!")
        else:
            print("I, the computer, win!")
    #for user_choice of 'scissors' against computer's choice of 'rock' and 'paper'
    elif (user_input == 'scissors' ):
        if(comp_choice == 'paper'):
            print("You, the user, win!")
        else:
            print("I, the computer, win!")
    #else condition loop for any other user_choice other than rock,paper and scissors it breaks and comes out of while loop
    else:
        print("Option is incorrect... Enter the correct choice")
        break