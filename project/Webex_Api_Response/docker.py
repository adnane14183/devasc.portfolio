import json

with open('Webex_Api_Response/dockerdata.json','r') as json_file:
  docker_json_file = json.load(json_file)

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict = (docker_json_file)
print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])