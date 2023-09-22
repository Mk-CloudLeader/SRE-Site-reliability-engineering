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
y = json.dumps(x)

# the result is a JSON string:
print(y)

