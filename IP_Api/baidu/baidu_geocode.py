import requests

from IP_Api.config import headers

key = 'Fcl0xHO4bNtdHGzR45K7iYga1T6pH6fT'
api_url = 'http://api.map.baidu.com/geocoder/v2/'


def geocode(address):
    """
    Address to (latitude, longitude)

    :param address: address string
    :return: a tuple of string like (latitude, longitude)
    """
    data = {
        'ak': key,
        'output': 'json',
        'address': address
    }
    json_res = requests.get(api_url, params=data, headers=headers).json()
    lng = json_res['result']['location']['lng']
    lat = json_res['result']['location']['lat']
    return lat, lng


def reverse_geocode(location):
    """
    (latitude, longitude) to address

    :param location: (latitude, longitude)
    :return: address
    """
    data = {
        # 坐标是 (纬度，经度)
        'location': '%s, %s' % (location[0], location[1]),
        'coordtype': 'bd09ll',   # 默认值 百度经纬度坐标
        'output': 'json',
        'ak': key
    }
    json_res = requests.get(api_url, params=data, headers=headers).json()
    formatted_address = json_res['result']['formatted_address']
    semantic_description = json_res['result']['sematic_description']  # ....弱鸡api单词都能拼错
    return formatted_address, semantic_description

if __name__ == '__main__':
    print(geocode('北京'))




