from bs4 import BeautifulSoup
import requests
import jieba
import re

url = 'https://mp.weixin.qq.com/misc/appmsgcomment?action=list_comment&begin=0&count=20&comment_id=1257369624522489856&filtertype=0&day=0&type=2&max_id=0&token=756531224&lang=zh_CN&f=json&ajax=1'

requests.packages.urllib3.disable_warnings()
cookie = '''pgv_pvid=8639390853; ua_id=hx74FuoqlX3L7PEiAAAAAIwuYr7Qir9hmkj246LBtkU=; pgv_pvi=7127276544; UM_distinctid=16e638f17d84e2-072829bd8d9e75-34584c70-1fa400-16e638f17d9504; mm_lang=zh_CN; RK=f9Itm8e5vP; ptcz=af49d739c6e45616533936c0d0b542518dd1c414904e98188176a0c86fcad68b; pac_uid=0_8a53a03411b68; noticeLoginFlag=1; remember_acct=549628782%40qq.com; openid2ticket_olkf1wxEcIQe_HjyoQJosqkyaojs=g9js94GOzUubW6yCRn1EJDUErCtuqtXX+Z2AzI3OIaE=; openid2ticket_oMWOb1B6MYx2qUvAcFWa5NZAXpNY=khOjSN6e6Wo80+67GDCrbSXfEyTjeZr2G0EnWNS+2js=; openid2ticket_okLr95x34HobQzeOqCQKq0bdwUNs=Q4CU0lt9jTTtewlVPhxvanEcsWcUhVujOPywPIgwyNo=; CNZZDATA1272960370=2134580348-1573624790-https%253A%252F%252Fwww.sogou.com%252F%7C1584512248; CNZZDATA1272425418=1484688940-1573625319-https%253A%252F%252Fwww.sogou.com%252F%7C1584515871; pgv_info=ssid=s2456805422; pgv_si=s8781056000; uuid=ad723eca8cff70d734b5593a62fca1d2; ticket=5013af454e25c5aa338997025ce577055aa15c6a; ticket_id=gh_97e7327fff45; cert=aIfUbcpAHAoMw1lCfnPR0rFMPxy3yiFR; rand_info=CAESIHxLCJbDs7xaz1cZ+qfoWCqSW7Kzv8fLPU4zXPFsvKkS; slave_bizuin=3227266170; data_bizuin=3008866823; bizuin=3227266170; data_ticket=+c16RmmFiN0Kaz6pqWssGg5kkElvx/CD8R4h2B/X/GS4LMDkVAuhxxr/ni08FGKo; slave_sid=YmVxdk5pa0JWU2FZVDA3bXBic2lKZWxudTMzcmV5clo5YjNDU0h4RG1JN0xCam1jVlI1ZEZRQ2lGTlI5b0JqZW8zN1RSZ21VcVRxSThiQTJ2N3M0eFNSU2ViNUNLbk1KUGxuSUo1Ynh3VmtienlZSmVJdVVHbmNiUTc0MHZSZk9LN0dqNlVRRTY4c3FTMUVp; slave_user=gh_97e7327fff45; xid=8dd562d03105e1e9c1fa7fe4111028e0; openid2ticket_oB6pXsz_akEkil7C5UQyvkunubtE=YPfPAhKULIf1xEoB7WpHMm6xetuvQ630U7bRBARj5cE=; qpsvr_localtk=1584583235521'''

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400',
'Connection': 'keep-alive',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie': cookie}

response = requests.get(url, headers = headers, verify=False)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)

line = soup.readline()
res = re.findall(r'content\\\":\\\"(.*?)\\\"', string=line)

stopwords = [line.strip() for line in open("CS.txt", encoding="utf-8").readlines()]
words = jieba.lcut(res)

counts = {}
for word in words:
    # 不在停用词表中
    if word not in stopwords:

        # 不统计字数为一的词

        if len(word) == 1:

            continue

        else:

            counts[word] = counts.get(word, 0) + 1

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)

for i in range(30):
    word, count = items[i]

    print("{:<10}{:>7}".format(word, count))