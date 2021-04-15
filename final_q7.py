

def sum_digits(int1):
    #define initial sum as 0
    sum = 0
    #read int1 as a string of integers 
    for digit in str(int1): 
        #sum the digits in the integer 
        sum += int(digit)       
    return sum
    
#sample integer for the test run
int1 = 323
print(sum_digits(int1))