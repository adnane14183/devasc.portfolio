import json

with open('Webex_Api_Response/dockerdata2.json','r') as json_file:
  docker_json_file2 = json.load(json_file)

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict2 = (docker_json_file2)
print(docker_dict2[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.dumps(docker_dict2)
print("Filtering from dict")
print(docker_dict2[0]["Name"])
print(docker_dict2[0]["Created"])
print(docker_dict2[0]["Containers"]["4e99a64e10dfcf6608a1d47f4349676c745bf234cebd52826d786db9a3be2811"]["IPv4Address"])