

def balance(weight, left, right):
    weight = []

    #Base case 
    if (left > right) :
        return False
        #Recursive case
        if (right > left) :
            return False
    #Recursive case 
    else :
        return True

    return balance()

#test case
weight =[1, 2, 3, 4, 5]


