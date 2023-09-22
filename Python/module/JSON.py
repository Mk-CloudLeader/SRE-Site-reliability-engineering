# JSON in Python
# Convert from JSON to Python: json.loads. # If you have a JSON string, you can parse it by using the json.loads() method.
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  json.loads
# the result is a Python dictionary:
print(y["age"])

#example 2
get_secret_value_response = client.get_secret_value(SecretId='snowMK-pwd')
# parse get_secret_value_response :
secret = json.loads(get_secret_value_response['SecretString'])
# the result is a Python dictionary:
pwd = secret['snowMK-pwd']



# Convert from Python to JSON: json.dumps
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)      # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  json.dumps

# the result is a JSON string:
print(y)

Example :
    request_parameter = {
    "records": [
        {
            "source": "aws:sns",
            "node": "ec2-windows-drivers",
            "type": "AWS Driver Notification For Latest Release",
            "resource": "sns-mktest",
            "severity": "4",
            "description": "AWS EC2 driver notification",
             
        }]
    }
# convert into JSON:
data=json.dumps(request_parameter, indent=2, default=str)

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

json.dumps(x, indent=4)

# Example :
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, 
# and a colon and a space to separate keys from values:

json.dumps(x, indent=4, separators=(". ", " = "))






