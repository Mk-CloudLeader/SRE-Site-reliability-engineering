"""
Also called Function
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""
# Demo01 ----------------------------------------------------------------------------------------------------------------------------

def sum_nums(n1, n2):
    print(n1 + n2)

sum_nums(2, 8)

sum_nums(3, 3)

#Demo02 ----------------------------------------------------------------------------------------------------------------------------
 
def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2                # The return statement is used to exit a function and return a value to the caller

sum1 = sum_nums(2, 8)

sum2 =  sum_nums(3, 3)

string_add = sum_nums('one', 2)
print(string_add)

print(sum1)
print("*************")

def isMetro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False

x = isMetro('boston')
print(x)

# #Demo03 (return) ----------------------------------------------------------------------------------------------------------------------------
def my_function():
  return 42
$my_function()    # output 42
def my_function(x):
  return x * x
$my_function(2)   # output 4 

# #Demo04 ----------------------------------------------------------------------------------------------------------------------------
"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

def sum_nums(n1, n2=4):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(4, n2=12)
print(sum1)

 #Demo05 ----------------------------------------------------------------------------------------------------------------------------
"""
Variable Scope
"""

a = 10

def test_method(a):
    print("Value of local 'a' is: " + str(a))
    a = 2
    print("New value of local 'a' is: " + str(a))

print("Value of global 'a' is: " + str(a))
test_method(a)
print("Did the value of global 'a' change? " + str(a))

##
a = 10

def test_method():
    global a
    print("Value of 'a' inside the method is: " + str(a))
    a = 2
    print("New value of 'a' inside the method is changed to: " + str(a))

print("Value of global a is: " + str(a))
test_method()
print("Did the value of global 'a' change? " + str(a))

 #Demo06  ----------------------------------------------------------------------------------------------------------------------------
"""
Some built-in functions
max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

abs(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument.
"""

def largest_num(*args):
    print(max(args))
    return(max(args))

largest_num(-20, -10, 0, 10, 100)

def smallest_num(*args):
    print(min(args))

smallest_num(-20, -10, 0, 10, 100)

def abs_function(a):
    print(abs(a))

abs_function(-20)
abs_function(20)

print("**********")

print(type(99))
print(type(99.9))
print(type("99.9"))
l = [1, 2, 3]
print(type(l))

#Demo7 ----------------------------------------------------------------------------------------------------------------------------
"""
Methods Exercise
Create a method, which takes the state and gross income as the arguments and returns the net income after deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don’t have to do for all the states, just take 3-4 to solve the purpose of the exercise.
"""

def calculateNetIncome(gross, state):
    """
    Calculate the net income after federal and state tax
    :param gross: Gross Income
    :param state: State Name
    :return: Net Income
    """
    state_tax = {'CA': 10, 'NY': 9, 'TX': 0, 'NJ': 6}

    # Calculate net income after federal tax
    net = gross - (gross * .10)

    # Calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all the heavy taxes is: " + str(net))
        return net
    else:
        print("State not in the list")
        return None


calculateNetIncome(100000, 'CA')


