import json

with open('Webex_Api_Response/data.json','r') as json_file:
  resp = json.load(json_file)

print("Displaying partial information")
print("Name: " + resp['displayName'])
print("Created: " + resp['created'])
print("User Type: " + resp['type'])
print("User Status: " + resp['status'])
