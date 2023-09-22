
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


# def : In Python a function is defined using the def keyword:


# Example :
def my_function():
  print("Hello from a function")

my_function()                              # To call a function, use the function name followed by parenthesis:


# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. # Ex: def my_function(fname):

#The following example has a function with one argument (fname). When the function is called, we pass along a first name, 
# which is used inside the function to print the full name:
# Outcome - : call with first name and function will print with full name calling 'fname '

def my_function(fname):
  print(fname + " kumar")

my_function("Email")   # Email kumar
my_function("Tobias") # Tobias kumar
my_function("Linus")  # Linus  kumar


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

#From a function's perspective:

#A parameter is the variable listed inside the parentheses in the function definition.

#An argument is the value that is sent to the function when it is called. 


# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, 
# you have to call the function with 2 arguments, not more, and not less.

# Exampple :This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Mukesh", "kumar")

# If you try to call the function with 1 or 3 arguments, you will get an error:
# Example : This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Mukesh")     # will see error 

# Arbitrary Arguments, *args

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example :If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Mike", "Tina", "MK")       # output MK ; if change kids[0] then output Mike 
