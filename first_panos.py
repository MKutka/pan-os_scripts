import requests
import json
import vars
from pprint import pprint

url = f"https://{vars.host}/restapi/v10.2/Objects/Addresses?location=shared"
payload={}


response = requests.request("GET", url, headers=vars.headers, data=payload, verify=False)

# Format the response to a JSON object
json_response = json.loads(response.text)

#Pretty Print the output of the JSON object
pprint(json_response)