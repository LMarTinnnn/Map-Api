import requests

from IP_Api.config import headers

key = 'Fcl0xHO4bNtdHGzR45K7iYga1T6pH6fT'
api_url = 'http://api.map.baidu.com/location/ip'


def get_country(ip):
    """
    ip to address
    只支持国内ip
    :param: ip address you wanna check
    :return: address
    """

    data = {
        'ip': ip,
        'ak': key,
    }

    json_res = requests.get(api_url, headers=headers, params=data).json()
    city = json_res['content']['address']
    return city


if __name__ == '__main__':
    print(get_country('47.88.188.254'))
