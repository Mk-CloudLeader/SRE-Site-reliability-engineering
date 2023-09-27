# Strings in Python are enclosed in either single or double quotes
# https://www.w3schools.com/python/python_strings.asp

print("Hello")
print('Hello')

my_name = "John Doe"
my_address = "123 Main Street, Anytown, CA 12345"
my_phone_number = "(555) 555-5555"

first = 'nyc'[0]
print(first)
city ='sfo'
ft = city[0]
print(ft)               # output will s

"""
len()
lower()
upper()
str()

"""
stri = "This Is Mixed Case"
print(stri.lower())
print(stri.upper())
print(stri.__len__())

print(stri + str(2))    # Output : This Is Mixed Case2

# Str() : The str() function converts the specified value into a string.
x = int("12") # Convert a string into an integer:
x = str(3.5)  # Convert the number 3.5 into an string:


a = "This is a string"
print(a[:])
print(a[:1])
print(a[:6])    # output is : This i
print(a[:-1])

#step
print(a[::])
print(a[::2])

print(a[::-1])
print(a[1])

# Strings Formatting ------
"""
Example to show how string formatting works in python
"""
city = "nyc"
event = "show"
print("Welcome to " + city + "  and enjoy the  " + event)

#Or, better way

print("welcome to %s and enjoy the show %s" %(city, event))
print("welcome to %s"  %(city))

