

def winstreak(my_List):
    my_List = []
    
    #define streak counter 
    previous = None
    streak = 0
    previous_success = True

    #repetitive counter
    for i in my_list:
        if (i-1)==previous:

            if previous_success:
                streak+=1
            else:
                streak =1

        previous = i
    print(streak)

    return winstreak()