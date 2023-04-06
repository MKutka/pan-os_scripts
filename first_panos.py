import requests
import json
import vars
from pprint import pprint

# This scripts purpose is to pull all of the Address Objects from Panorama and save them as a CSV file.

url = f"https://{vars.host}/restapi/v10.2/Objects/Addresses?location=shared"
payload={}

response = requests.request("GET", url, headers=vars.headers, data=payload, verify=False)

# Format the response to a JSON object
json_response = json.loads(response.text)

stripped_json = json_response['result']['entry'][0:]

# # Pretty Print the output of the JSON object
# pprint(stripped_json)

# Save output as csv file on in local folder
with open('address.csv', 'w') as f:
    for item in stripped_json:
        # where sometimes decription and/or ip-netmask is not present
        if'description' and 'ip-netmask' not in item:
            item['ip-netmask'] = ' '
            item['description'] = ' '
            f.write("%s,%s,%s,%s\n" % (item['@name'], item['@location'], item['ip-netmask'], item['description']))
        elif 'ip-netmask' not in item:
            item['ip-netmask'] = ' '
            f.write("%s,%s,%s,%s\n" % (item['@name'], item['@location'], item['ip-netmask'], item['description']))
        elif 'description' not in item:
            item['description'] = ' '
            f.write("%s,%s,%s,%s\n" % (item['@name'], item['@location'], item['ip-netmask'], item['description']))

# Save output as json file on in local folder
with open('address.json', 'w') as f:
    json.dump(json_response, f, indent=4)
