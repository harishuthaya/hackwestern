import requests
import json
from rich import print
import webbrowser as wb

r = requests.post('http://localhost:5000/api/create/room')
print(r.text)
link = 'doctor.metered.live/' + r.text
print(link)
