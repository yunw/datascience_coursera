import requests

body = {'Name': 'Eric', 'Age': '26'}

# Make the POST request here, passing body as the data:
response = requests.post("http://codecademy.com/learn-http/", data=body)

print response