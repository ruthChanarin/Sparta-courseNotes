import requests
import json

headers = {'Content-Type': 'application/json'}
json_data = json.dumps({'postcodes':["PR3 0SG", "M45 6GN", "EX165BL"]})

post_codes_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_data)

print(post_codes_req)

print(post_codes_req.json())

print(type(post_codes_req))

print(post_codes_req.json()['result'][0]['result']['parish'])
