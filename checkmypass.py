import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # First 5 symbols of SHA1 Hash string
    res = requests.get(url)
    if res.status != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def pwned_api_checl(password):
    #Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

#request_api_data('password123')