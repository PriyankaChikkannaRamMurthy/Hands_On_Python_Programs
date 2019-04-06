'''Program 3: First character of a word returns the number of times the letter is the first character of a word

Algorithm: • The program takes the users input for the line of text along with a single character to be counted for its occurence in the text line. • if the user_input for single character is more than length of 1 then it prompts the user to enter only a single letter and comes out of the loop • else condition loop calls for the function 'first_char' which takes the input parameters like the text_line and the single_letter where it converts the text line & single letter to lower case. • for each_word from the text_line it checks for the first_letter of each_word to be single_letter. If it encounters it then it increments the counter and at the end of checking all the words for the letter it returns the total occurences of the single_letter in the text_line as the first character of the word

Instructions: Select the cell and click "Run" from the upper tab options to execute the cell and input the user choice accordingly

Expected results: Enter your line of text: The animal is an antelope Enter your letter to use: a Your letter a occurs as the first letter: 3 times

Enter your line of text: the asdhgf shdgjhdf Enter your letter to use: sdfghj Please enter a single letter for the letter to be used...'''

#function call for calculating the occurences of the single character in the text_line as the first character of each word
def first_char(line_text, single_letter):
    #converting to lower case
    lower_line = line_text.lower()
    #converting to lower case of the single_character
    lower_single = single_letter.lower()
    count = 0
    #for each of the word from the txt_line run the program logic
    for each_word in lower_line.split():
        #if condition loop for checking th efirst character of each word to be the single letter or not
        if(lower_single == each_word[0]):
            #incerementing the counter for number of occurences
            count = count + 1
            #returning the counter value as the outptut value of the function to the function call
    return count
#input for the text line from the user
line_text = input("Enter your line of text: ")
#input for the single_letter from the user
single_letter = input("Enter your letter to use: ")
#if the length of the single_letter is greater than 1 then return that its not a single letter as expected 
if(len(single_letter) != 1 ):
    print("Please enter a single letter for the letter to be used...")
#else condition loop for function call to check for the number of occurences of the single letter in the line_text
else:
    char_count = first_char(line_text, single_letter)
    #printing the number of occurences of the single letter as freturned from the function call
    print("Your letter",single_letter,"occurs as the first letter:",char_count,"times")

