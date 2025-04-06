import requests

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'     #First 5 symbols of SHA1 Hash string
res = requests.get(url)
print(res)