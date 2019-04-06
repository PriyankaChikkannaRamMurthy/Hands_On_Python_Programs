'''
Program 4:
Below is the Python function SimpleInterest() that takes in 3 arguments: principle amount (float) ,
Interest Rate (0 to 100% as a float), Year (integer) which returns the interest amount.
The formula for a simple interest is given by the program and is implemented.

Logic:
* Function SimpleInterest is written which takes in 3 arguments principle amount, interest rate and year which
calculates the simple interest for the input values. On wrong input of the values the program handles it by 
printing the error message in the program. 
* If the principle amount, Interest and years are greater than 0 value then it enters an if loop condition for 
computing the simple interest value based on the formula given in the program. 
* If values are lesser than 0 or not in the proper format then it jumps to else loop and prints out the 
error message. 
* Program is run by the function call along with the input values of the principle, interest rate, years and are tested and computed for the simple interest values.

'''

#function call for simple_interest calculation
def SimpleInterest(princ_amt,rate_int,year):
    try:        
        #casting values for float and integer datatype accordingly
        principle = float(princ_amt)
        rate_interest = float(rate_int)
        years = int(year)    
        
    except:
        #values set to determine the format other than specified in the program
        principle = -1
        rate_interest = 0 
        years = 0
    
    #if condition loop for checking the numbers to greater than 0
    if(principle>= 0 and rate_interest>= 0 and years>=0):
        #formula for simple interest to be computed
        sim_interest = (principle*rate_interest*years)/100
        #printing the computed value to the user
        print('The interest amount is:', sim_interest)
    else:
        #else condition loop for numbers lesser than certain value and not being in the proper format
        print('Error: Please input in the correct format')
