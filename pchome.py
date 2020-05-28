import requests
import prettytable
import json
import os
# s = p.PrettyTable(['商品','價錢'],encoding='utf-8')

os.system("cls")

x = input("請輸入要搜尋的商品:")
r =requests.get(
    "https://ecshweb.pchome.com.tw/search/v3.3/all/results",

    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    },
    params={
        "q": x
    },
)

while True:
    os.system("cls")
    r = json.loads(r.text)
    for a in r["prods"]:
        print(a['name'],  a['price'])

    # for i in range(len(city)):
    #     s.add_row([city[i],tem[i]])
    # print(s)

    r =requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results",

        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        },
        params={
            "q": x,
            "page":input("請輸入頁碼: "),
        }
    )

    os.system("cls")

    r = json.loads(r.text)




