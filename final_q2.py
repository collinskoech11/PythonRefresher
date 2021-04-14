# Noel Wafuko
# nww010 # 11308656
# For Instructor Jeff Long

def balance(weight, leftSide, rightSide):
    weight = []

    #Base case 
    if (leftSide > rightSide) :
        return False
        #Recursive case
        if (rightSide > leftSide) :
            return False
    #Recursive case 
    else :
        return True

    return balance()

#test case
weight =[1, 2, 3, 4, 5]


