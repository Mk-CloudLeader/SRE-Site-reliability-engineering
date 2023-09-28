"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

# List_demo ------------------------------------------------------------------------------------------------
"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

cars = [ "bmw", "honda", "audi"]
empty_list = []
print(empty_list)
print(cars)

print("*#"*20)

print(cars[1])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

more_cars = [ "bmw", "honda", "audi"]
print(more_cars[1])

more_cars[1] = "Benz"                    # will change because List is mutable but tuble is not 

print(more_cars[1])
print(more_cars)

#List_Method --------------------------------------------------------------------------------
"""
Built-in methods to help manipulating a list
"""

cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*#"*20)
print(cars)
cars.sort()

print(cars)

# dictdemo ----------------------------------------------------------------
"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1':'v1', 'k2':'v2'}
Not sequenced, no indexing -> Mapping
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)

d = {}

model = car['model']

print(car['make'])
print(model)

d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)

# Nested Dictionary -------------------------------------------------------------------------------------
"""
Nested Dictionary:
d = {'k1': {'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['benz']['model'])

#Dictionary Methods -------------------------------------------------------------------------
"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)

# Tuple -----------------------------------------------------------------
"""
Tuple
Like list but they are immutable
It means you can't change them
"""

my_list = [1, 2, 3]
print(my_list)

my_list[0] = 0
print(my_list)

my_tuple = (1, 2, 3, 2, 2, 3)
print(my_tuple)

print(my_tuple[0])

print(my_tuple[1:])

print(my_tuple.index(2))

print(my_tuple.count(3))
