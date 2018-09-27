import requests
import re
import time
f = open('/Users/jalynnxi/Desktop/doupo.txt','a+')
def get_info(url):
    res = requests.get(url)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
        else:
            pass
if __name__ =='__main__':
    urls = ['http://m.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(1,1624)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()