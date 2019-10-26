by Joseph Jenkins

This script allows you to pull information from all of the devices in the organization. It iterates through the networks looking for clients with specific information and then dumps them into csv files as you go. The script can be customized based on any of the following information:

{
  "usage": {
    "sent": 138.0,
    "recv": 61.0
  },
  "id": "k74272e",
  "description": "Miles's phone",
  "mac": "00:11:22:33:44:55",
  "ip": "1.2.3.4",
  "user": "milesmeraki",
  "vlan": 255,
  "switchport": null,
  "ip6": "",
  "firstSeen": 1518365681,
  "lastSeen": 1526087474,
  "manufacturer": "Apple",
  "os": "iOS"
}

So when searching the network for specific things this makes it easy to iterate through and find all of the information.