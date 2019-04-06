'''
Program 1:
Below is the python program that requests three strings from the user that concatenates the first two strings 
in the reverse order and will compare the concatenated string with the third string of the user.
On comparison, if they are equal then it prints “They are equal”, otherwise it prints “They are not equal”.

Logic:
use '+' operator for the second and then the first string
g to concatenate them and check the condition for 
the concatenated string to be equal to the third string entered by the user with th "if...else" loop '==' operator
wherein it prints "They are equal" on both being the same strings else prints 'They are not equal'. 

'''
#input string 1 entered by user
inp1_str = input('Enter string 1:')
#input string 2 entered by user
inp2_str = input('Enter second string:')
#input string 3 entered by user
inp3_str = input('Enter third string:')

#new string with concatenated output of string 2 and string 1 of the user
str_cat = inp2_str + inp1_str

#condition checking for the concatenated string and the third string to be equal or not
if(str_cat == inp3_str):
    print('They are equal') 
else:
    print('They are not equal')
