# Python Requests Module :Make a request to a web page, and print the response text:
# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

# SYNTAX : requests.methodname(params)
# Methods
{{{ 
|Method	                 |Description                               |
|delete(url, args)	     |Sends a DELETE request to the specified url|
|get(url, params, args)	 |Sends a GET request to the specified url|
|head(url, args)	       |Sends a HEAD request to the specified url|
|patch(url, data, args)	| Sends a PATCH request to the specified url|
|post(url, data, json, args)	|Sends a POST request to the specified url|
|put(url, data, args)	|Sends a PUT request to the specified url|
|request(method, url, args)	| Sends a request of the specified method to the specified url |
}}}

# ----------------------------------------------
# Example :get

import requests

x = requests.get('https:/example.com/python/demopage.htm')

print(x.text)

# example :post

import requests

url = 'https://example.com/python/demopage.php'
myobj = {'name': 'MKS'}

x = requests.post(url, json = myobj)
print(x.text)

# Download and Install the Requests Module
$pip install requests
