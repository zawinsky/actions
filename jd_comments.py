import os
import re
import csv
import random
from datetime import datetime
import requests


#log = open('a.log', 'w')
url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98&productId={0}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'

filename = os.path.dirname(os.path.realpath(__file__))+'/useragents.csv'
user_agent_csv = open(filename, 'r')
reader = csv.reader(user_agent_csv)
user_agent_list = [row for row in reader]

def random_ua():
    return random.choice(user_agent_list)[0]

def fetch(sku):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'Referer': f'https://item.jd.com/{sku}.html',
        'User-Agent': random_ua()
    }
    r = requests.get(url.format(sku), headers=header).text
    a = re.match('.*"commentCount":(\d+).*', r)
    b = re.match('.*"defaultGoodCount":(\d+).*', r)
    c = re.match('.*"commentCount":(\d+).*', r)
    d = re.match('.*"goodCount":(\d+).*', r)
    e = re.match('.*"generalCount":(\d+).*', r)
    f = re.match('.*"poorCount":(\d+).*', r)
    g = re.match('.*"videoCount":(\d+).*', r)
    h = re.match('.*"afterCount":(\d+).*', r)
    if a and a.groups():
        print(sku,':',a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1])
    else:
        #log.write(f'{sku}:None\n')
        print(sku, r)
        #raise

def main():
    skus = []
    with open('list.txt', 'r') as f:
        for line in f:
            skus.append(line.replace('\n',''))

    #log.write(f'starts at: {datetime.now()}\n')
    print(f'starts at: {datetime.now()}')
    for s in skus:
        try:
            fetch(s)
        except:
            #log.write(f'error at: {datetime.now()}\n')
            print(f'error at: {datetime.now()}')
            return
    print(f'ends at: {datetime.now()}')
    #log.write(f'ends at: {datetime.now()}\n')

if __name__ == '__main__':
    main()
