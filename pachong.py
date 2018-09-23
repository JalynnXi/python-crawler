import requests
from lxml import etree
import json
import csv


fp = open('/Users/jalynnxi/Desktop/map.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('address', 'longitude','latitude'))


def get_user_url(url):
    url_part = 'https://www.qiushibaike.com'
    res = requests.get(url)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[@class = "article block untagged mb15 typs_hot"]')
    for url_info in url_infos:
        user_part_urls = url_info.xpath('div[1]/a[1]/@href')
        # print (user_part_urls)
        if len(user_part_urls)==1:
            user_part_url = user_part_urls[0]
            get_user_adress(url_part+user_part_url)
        else:
            pass


def get_user_adress(url):
    res = requests.get(url)
    selector = etree.HTML(res.text)
    if selector.xpath('/html/body/div[2]/div/div[3]/div[2]/ul/li[4]/text()'):
        address = selector.xpath('/html/body/div[2]/div/div[3]/div[2]/ul/li[4]/text()')
        # print (address)
        get_geo(address[0].split('.')[0])
    else:
        pass


def get_geo(address):
    par = {'address':address,'key':'cb649a25c1f81c1451adbeca73623251'}
    api = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(api,par)
    json_data = json.loads(res.text)
    # print (json_data)
    try:
        geo = json_data['geocodes'][0]['location']
        longitude = geo.split(',')[0]
        latitude = geo.split(',')[1]
        writer.writerow((address,latitude,latitude))
    except IndexError:
        pass


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    for url in urls:
        get_user_url(url)