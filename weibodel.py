#encoding=utf-8
import requests
import re
from selenium import webdriver
import sys
import time
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8')  
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde


driver = webdriver.Firefox()
url = 'http://weibo.com/login.php'
driver.get(url)

enable=0
while enable==0:
    c=driver.title
    if c=='我的首页 微博-随时随地发现新鲜事':
        enable=1
cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
cookiestr = ';'.join(item for item in cookie)
page = driver.page_source
t=re.findall("'domain'\]='(.*?)'",page,re.S)[0]
driver.quit()    
headers={'Referer':'http://weibo.com/'+str(t),'Cookie':cookiestr,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
while 1==1:
    try:
        t=requests.get('http://weibo.com/'+str(t),headers=headers,verify=False).text
        idx=re.findall('<a name=(.*?) ',t,re.S)
        for x in idx:
            print x
            datax={'mid':x}
            html=requests.post('http://weibo.com/aj/mblog/del?ajwvr=6',data=datax,headers=headers,verify=False).text
            print html
            time.sleep(1) #请适当调整延迟！速度过快可能会导致10054错误！
    except Exception as err:
        print err
