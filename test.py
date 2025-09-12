
from fastapi import requests


response = requests.get('http://localhost:8000/rt', stream=True)
for line in response.iter_lines():
    if line:
        print(line.decode())