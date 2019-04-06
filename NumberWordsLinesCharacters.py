'''Program 5: file contents

Algorithm: • The program takes the users input for the file name which is to be opened in read mode to count the characters, to count the words and number of lines count • for loop is written with reading the fhandle, all th elines from the text file with each_line counted with incrementor. For each_line again we split the spaces and count each word in it. for each word, we again count each characters and increment the character count value. We then calculate the average length of a word by dividing the total character count with total number of words. • If suppose the file is not found then we handle in the except block by printing the file is not found.

Instructions: Select the cell and click "Run" from the upper tab options to execute the cell and input the user choice accordingly

Expected results: What is the filename: RobertFrost.txt Number of lines: 4 Number of words: 27 Number of characters: 103 Average length of a word: 3.814814814814815

What is the filename: sdfghj.fgh File cannot be opened: sdfghj.fgh'''

#inputing the user value for the file name to be opened
user_inp = input('What is the filename: ')
try :
    #open method to open and read the filename entered
    fhand= open(user_inp)
    l_count = 0
    w_count = 0
    c_count = 0
    #for each_line in the fhand
    for line in fhand:
        #incrementing the line counter
        l_count = l_count + 1
        #incrementing the word counter
        w_count = w_count + len(line.split())
        #for each_word in each_line
        for each_word in line:
            #incrementing the character counter
            c_count = c_count + len(each_word.split())
        #computing the average length of each word
        avg_len = c_count / w_count
            
    print('Number of lines:',l_count)
    print('Number of words:',w_count)
    print('Number of characters:',c_count)
    print('Average length of a word:',avg_len)
except :
    #file cannot be opened when not found and handled in the except block
    print('File cannot be opened:',user_inp)
    quit()
    