import requests
import jwt

# Providing examples to help with interacting with the server
# For this to work you will need to run `python3 -m pip install requests pyjwt` to install the required modules
# Fill in any where you see angle brackets like <fill this in>

## Registering:
res = requests.post('<url>/api/register', data={'username': '<username here>'})
print(res.text)

## Logging in:
res = requests.post('<url>/api/login', data={'session': '<session token here>'})
print(res.text)
