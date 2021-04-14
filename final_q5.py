#generate a random sales db based on a given seed for reproducability

import math as m
import random as r

#DO NOT CHANGE ANY OF THE FOLLOWING OR IT WILL BREAK THE AUTOMATED TESTING AND YOU WILL GET ZERO FOR THE QUESTION
cities = ['Vancouver', 'Vancouver', 'Vancouver', 'Calgary', 'Calgary', 'Edmonton', 'Saskatoon', 'Winnipeg', 'Toronto', 'Toronto', 'Toronto', 'Toronto']
sales_people = ['Bob', 'Doug', 'Samantha', 'Keri']
sales_range = [250000,500000]
stay_range = [1,5]
success_rate = 0.7
total_visits = 200
#DO NOT CHANGE ANY OF THE ABOVE OR IT WILL BREAK THE AUTOMATED TESTING AND YOU WILL GET ZERO FOR THE QUESTION


def generate_db(seed, c, e, s, st, sr, v):
    """
    Generates a random sales record based on a set of parameters and a random seed
    DO NOT CHANGE THIS FUNCTION AS IT WILL IMPACT AUTOMATED GRADING AND YOU WILL GET ZERO
    :param seed: random seed for the test generation
    :param c: list of cities
    :param e: list of employees
    :param s: range of sales amounts
    :param st: range of stay lengths
    :param sr: probability that a sale was successful
    :param v: total number of sales visits to generate
    :return: sales_db: a database (record or records) containing sales information. Index is the visit number in the range of 0 to v.
    """

    r.seed(seed) #initialize the random number generator with the seed
    sales_db = {} #make an empty dictionary

    for i in range(0,v):
        #populate a single record
        new_rec = {'city': r.sample(c, 1)[0], #draw a city
                   'employee' : r.sample(e, 1)[0], #draw a person
                   'sales' : round(r.triangular(s[0],s[1])), #draw a sale value
                   'stay' : round(r.uniform(st[0],st[1])) #how long did it take to close the deal
                   }
        if r.random() > sr: #deal fell through
            new_rec['sales'] = 0

        #add record to db
        sales_db[i] = new_rec

    return sales_db

def get_employee_totals(db, emp):
    """
    Returns to the total sales and stay length for a given employee
    :param db: a database as dictionary of sales records from generate_db
    :param emp: a string containing the name of the employee
    :return: a record containing the total sales and stay length for that employee
    """
    total_rec = {'employee' : REPLACE_THIS,
                 'sales' : REPLACE_THIS,
                 'stay' : REPLACE_THIS}

	#your code here
    return total_rec

def employee_totals(seed, emp):
    """
    a wrapper function to aid automated grading of this final exam question
    You should not change this function
    :param seed: a random seed
    :param emp: a string containing the name of the employee
    :return: total sales and stay length for that employee from get_employee_totals
    """

    db = generate_db(seed, cities, sales_people, sales_range, stay_range, success_rate, total_visits)
    rec = get_employee_totals(db, emp)
    return rec

