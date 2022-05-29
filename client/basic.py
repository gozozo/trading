import requests

enpoint  =  "http://127.0.0.1:8080/api/"

get_response = requests.get(enpoint, params={"adv":123}, json={"wuqry": "Hello"} )

print(get_response.json())
#print(get_response.status_code)

