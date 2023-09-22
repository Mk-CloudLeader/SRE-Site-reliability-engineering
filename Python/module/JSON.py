# JSON in Python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#example 2
get_secret_value_response = client.get_secret_value(SecretId='snowMK-pwd')
# parse get_secret_value_response :
secret = json.loads(get_secret_value_response['SecretString'])
# the result is a Python dictionary:
pwd = secret['snowMK-pwd']


