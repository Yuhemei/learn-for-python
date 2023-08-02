import requests

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}


def get_random_ip():
    r = requests.get("http://api.ip.data5u.com/dynamic/get.html?order=9af38a40fb9e40bd1a9e6bc3d74d349e&random=1&sep=3")
    return str(r.text).strip()


proxy_ip = get_random_ip()
print(proxy_ip)
r = requests.get("https://www.zhipin.com/c101010100-p100109/?page=1&ka=page-1",
                 proxies={"http": 'http://' + proxy_ip, "https": 'https://' + proxy_ip},
                 verify=False, timeout=10,
                 headers=headers)

print(r.status_code)
print(r.text)
