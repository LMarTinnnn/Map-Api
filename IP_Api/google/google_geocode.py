import requests

from IP_Api.config import headers, proxies

key = 'AIzaSyCC_GUx0kM6ZlDJUoFZHu6CUrsh-AKC2_Y'
api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

data = {
    'address': 'Santa Monica, LA, California, USA',
    'key': key
}

# ???? 读不出来
# response = requests.get(api_url, params=data, headers=headers, timeout=3)
while True:
    try:
        response = requests.get(api_url, params=data, headers=headers, proxies=proxies, timeout=3)
        res = response.text
        print(res)
        break
    except:
        print('重试')


