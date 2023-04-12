import requests
import json
import vars
from pprint import pprint

# Disable self-signed warning
requests.packages.urllib3.disable_warnings()

# The purpose of this script is to take end user input and create a new 
# network address/object for the Shared Template on PAN-OS

name = input("Enter the name of the network object: ")
ip_netmask = input("Enter the IP and Netmask of the network object: ")
description = name

location = {'location': 'shared', 'name': name}
url = f"https://{vars.host}/restapi/v10.2/Objects/Addresses"

payload = json.dumps({
  "entry": {
    "@name": name,
    "ip-netmask": ip_netmask,
    "description": description
  }
})

r = requests.post(url, params=location, verify=False, headers=vars.headers, data=payload)

if r.status_code == 200:
    print("Network object created successfully!")
else:
    print("Network object creation failed!")
    print(f"Failure Code: {r.status_code}")
    pprint(r.text)
