'''Program 4: String is Palindrome or not

Algorithm: • The program takes the users input for the line of text to be checked for string or not • function 'is_palindrome' is written which takes in the input parameter as the user input string to be checked as palindrome or not • the string is converted to lower case and the left index initialised to 0 and right to the last position of the string • if-elif condition written to evaluate the characters at the left and right index position of the string and incremented accordingly once both the characters are the same. • else it returns the value false telling that the string is not palindrome. • otherwise it returns the value true telling the string is palindrome

Instructions: Select the cell and click "Run" from the upper tab options to execute the cell and input the user choice accordingly

Expected results: Enter a string: mom " mom " is a palindrome

Enter a string: a nut f o r a JAR of TUNA " a nut f o r a JAR of TUNA " is a palindrome

Enter a string: asgh ashfa aidfja ;.fm " asgh ashfa aidfja ;.fm " is not a palindrome'''

#function definition with the parameters as string or text_line to be checked for palindrome or not
def is_palindrome(words):
    #converted to lower case
    words = words.lower()
    left = 0
    right = len(words) - 1
    
    #if-elif condition loop to compare each characters for palindrome or not
    if(not (words[left] >= 'a' and words[left] <= 'z')):
        left += 1
    elif(not (words[right] >= 'a' and words[right] <= 'z')):
        right -= 1
    #if both the characters from the las position of the string and the first position of the string matches then move to the next character for comparison 
    elif(words[left] == words[right]):
        left += 1
        right -=1
    else:
         #else returning the false value as the ouptut of the function
        return False
    #returning the true value as the ouptut of the function
    return True

#user input for the string to palindrome or not
user_inp = input('Enter a string: ')
#function call to check palindrome or not
output = is_palindrome(user_inp)
#the returned value of true or false passed to the if-else condition loopto decide palindrome or not
if(output == True):
    print('"',user_inp,'"','is a palindrome')
else:
    print('"',user_inp,'"','is not a palindrome')     
