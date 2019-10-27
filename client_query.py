#!/usr/bin/python

#main varaiables to be anonymized later before upload to github:
organization = cred.organization
key = cred.key
email_server = cred.email_server

#imports
import requests
import json
import os
import time
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


#Import the CRED module from a separate directory
sys.path.insert(0,'../CRED')
import cred


me = cred.me

you1 = cred.you1

#Main URL for the Meraki Platform
dashboard = "https://api.meraki.com"
#api token and other data that needs to be uploaded in the header
headers = {'X-Cisco-Meraki-API-Key': (key), 'Content-Type': 'application/json'}

# open files for writing
avery_status = open("ub_status.csv", "w", 0)
error_status = open("ub_error_status.csv", "w", 0)

#pull back all of the networks for the organization
get_network_url = dashboard + '/api/v0/organizations/%s/networks' % organization

#request the network data
get_network_response = requests.get(get_network_url, headers=headers)

#puts the data into a json format
get_network_json = get_network_response.json()


for network in get_network_json:
    time.sleep(1)
    #use this one when pulling back the last 3 days worth of data
    get_client_url = dashboard + '/api/v0/networks/%s/clients?timespan=604800' % network["id"]
    get_client_response = requests.get(get_client_url, headers=headers)
    get_client_json = get_client_response.json()
    for client in get_client_json:
        time.sleep(1)
        try:
            if (client["manufacturer"]) == "Ubiquiti Networks":                
                avery_status.write(network["name"] + ", " + str(client["mac"] + "\n"))
        except TypeError:
            error_status.write(network["name"] + "\n")
            #pass


msg = MIMEMultipart()
msg['Subject'] = 'Listing of the Stores with Ubiquiti Devices'
msg['From'] = me
#used when sending email to groups vs a single user.
#msg['To'] = ', '.join(you1)
msg['To'] = you1

part = MIMEBase('application', "octet-stream")
part.set_payload(open("avery_status.csv", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="avery_status.csv"')

msg.attach(part)

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP(email_server)
s.sendmail(me, you1, msg.as_string())
s.quit()
avery_status.close
error_status.close
