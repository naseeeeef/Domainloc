import socket
import requests as req
import json


url = input("Enter domain name: ")
ip = socket.gethostbyname(url)
req = req.get(f'https://ipinfo.io/{ip}/json')
data = json.loads(req.text)
print (f'ip of {url} is {ip}\n\n')
print (f'location of the server is {data['loc']}')