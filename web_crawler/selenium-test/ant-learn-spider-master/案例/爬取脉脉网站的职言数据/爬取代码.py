import requests
import json

url = "https://maimai.cn/sdk/web/content/get_list"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "cookie": "_buuid=5e83703b-23d6-47ae-af92-19bcba9cc049; Hm_lvt_125466a4193d3041720419bb940c71b9=1653288780,1653958040,1654051778; is_company_vip=0; has_admin=1; maimai_pc_login_show_tooltip=1; seid=s1654052124665; guid=GxgZBBsYGQQYHhwEGxocVhsbGRsaHBMaVhwZBB0ZHwVDWEtMS3kKGRwEHxoaHwQaBBgaGwVPR0VYQmkKA0VBSU9tCk9BQ0YKBmZnfmJhAgocGQQdGR8FXkNhSE99T0ZaWmsKAx4cUgoRHhxEQ30KERoEGhsKfmQKWV1FTkRDfQIKGgQfBUtGRkNQRWc=; u=1515483; u.sig=-zkSyCMo74aB-3I3ybshIIdWykE; access_token=1.f9da72d06fee39e13fcd77fe1ce9009f; access_token.sig=q1y6mB0aVa68tUUQ73UaVfQj7Ng; u=1515483; u.sig=-zkSyCMo74aB-3I3ybshIIdWykE; access_token=1.f9da72d06fee39e13fcd77fe1ce9009f; access_token.sig=q1y6mB0aVa68tUUQ73UaVfQj7Ng; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiJRZ2hNZ0RwNC1rLVg3UGVEWVg2UXBoSUciLCJ1IjoiMTUxNTQ4MyIsIl9leHBpcmUiOjE2NTQxMzg1NjUxNjIsIl9tYXhBZ2UiOjg2NDAwMDAwfQ==; session.sig=Ol3mcJmgNfaF_PC2fWMm9wMV1-M; csrftoken=9uslHOYd-9VY3qY-EOOwF2OsViiPRvjLitZU; Hm_lpvt_125466a4193d3041720419bb940c71b9=1654052174; _dd_s=logs=1&id=a218b5a9-d408-43ad-bc25-20db3e5a48ed&created=1654051777466&expire=1654053131843",
    "referer": "https://maimai.cn/gossip_list",
    "x-csrf-token": "9uslHOYd-9VY3qY-EOOwF2OsViiPRvjLitZU"
}


def craw_page(page_number):
    # ctrl alt l
    params = {
        "api": "gossip/v3/square",
        "u": "1515483",
        "page": page_number,
        "before_id": 0
    }

    resp = requests.get(url, params=params, headers=headers)
    # print(resp.status_code)
    data = json.loads(resp.text)
    datas = []
    for text in data["list"]:
        datas.append(text["text"])
    return datas


with open("脉脉结果.txt", "w", encoding="utf8") as f:
    for page in range(1, 10 + 1):
        print("craw page", page)
        datas = craw_page(page)
        f.write("\n".join(datas) + "\n")
