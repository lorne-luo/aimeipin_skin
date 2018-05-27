import requests


def get_location(ip):
    base_url = 'http://ip.taobao.com//service/getIpInfo.php?ip='
    url = '%s%s' % (base_url, ip)
    r = requests.get(url)

    if r.status_code == 200:
        json = r.json()
        code = json['code']
        if code == 0:
            data = json['data']
            if data['country'] == '中国':
                return '%s %s' % (data['region'], data['city'])
            else:
                return '%s %s %s' % (data['country'], data['region'], data['city'])

    return None
