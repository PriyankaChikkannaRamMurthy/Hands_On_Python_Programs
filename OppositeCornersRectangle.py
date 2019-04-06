'''
Problem 5:
 Below is the python program that takes as input two opposite corners of a rectangle: (x1,y1) and (x2,y2)
 which are of float or integer only. Finally, the user is prompted for the coordinates of a third point (x,y). The program should print Boolean value True or False based on whether the point (x,y) lies within the rectangle.
 At the end of each run, the user should be prompted to ask whether then want to continue.
 
Logic:
*function for taking the inputs from the user and determining the x,y co-ordinates to be inside the rectangle 
with name main_condition taking single argument to be 'y' or 'n'
*function for continuing with the program logic is written in the continue_condition with taking single 
argument from the previous function. With logic in if ..elif loop condition for 'y' with continuing the program 
or else 'n' to stop the [program with goodbye printed] or else to prompt the user with any other input nothing less than 'y' or 'n'
* the co-ordinates for x1,y1 and x2,y2 are prompted to entered from the user along with the x,y values for deciding it to be
lying in the rectangle
*if x1,x2 and y1,y2 are same then they form a point and not rectangle which is laso checked for in the program.
*if condition is written with the logic to be implemented for x,y to be lying inside the rectangle nothing but
lying within the range of x1,y1 and x2,y2 co-ordinates. 
* exception is handled with printing out 'enter valid format' to the user
*if true.. then the point lies within the rectangle or else false is printed to the user
'''

#function for continuing the loop with yes or no
def continue_condition(i_var):
    if(i_var == 'Y' or i_var == 'y'):
        main_condition('y')
    elif(i_var == 'N' or i_var == 'n'):
        print('Goodbye!')
    else:
        print('Enter Y or N')
        main_condition(input('Do you want to continue:'))

#function for taking the inputs from the user and determining the x,y co-ordinates to be inside the rectangle 
def main_condition(inp):
    print('Enter the co-ordinates for the first point...')
    x1_raw = input('Enter x1:')
    y1_raw = input('Enter y1:')
    print('Enter the co-ordinates for the second point...')
    x2_raw = input('Enter x2:')
    y2_raw = input('Enter y2:')
    print('Enter the co-ordinates for the x,y point to be checked for lying inside the rectangle...')
    x_raw = input('Enter x:')
    y_raw = input('Enter y:')

    try:
        #casting the input values float datatype accordingly
        x1 = float(x1_raw)
        y1 = float(y1_raw)
        x2 = float(x2_raw)
        y2 = float(y2_raw)
        x = float(x_raw)
        y = float(y_raw)
        
        #if condition loop for the values of x1, x2 and y1,y2 are same then they are the same single point
        if(x1 == x2 and y1 == y2):
            print('Since co-ordinates are same for x1,x2 and y1,y2 ....they form a point')
        #if condition loop to check for the x,y co-ordinate to fall inside the rectangle that will be within the range of the co-ordinates
        if(((x1<= x <=x2) or (x1>= x >=x2)) and ((y1<= y <=y2) or (y1>= y >=y2))):
            #printing true meaning the x,y are inside the rectangle
            print('True')
        else:
            #else condition for printing false meaning the x,y are not inside the rectangle
            print('False')
    
           
    except:
        print('Enter valid format for the input...')
    
    inp_var = input('Do you want to continue:')
    #calling the function to transfer the control flow for infinite looping based on the user input of 'y' or 'n'
    continue_condition(inp_var)
    
main_condition('y')        
