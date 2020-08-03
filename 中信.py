from bs4 import BeautifulSoup
import re
import requests
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
url_1 = 'https://buy.cthouse.com.tw/area/臺南市-city/page'
url_2 = '.html'
NameList=[]
AddressList=[]
pcShow=[]
price=[]
def end_page(): #找最後一頁
    page=[] 
    r = requests.get(url_1 + '1' + url_2)
    soup = BeautifulSoup(r.text, 'html.parser')
    for entry in soup.select('div.pageBar a'):
        page.append((entry.text))
    y=re.findall(r'\d+', page[-2]) #刪除最後一頁數字前的’...'
    y=eval(y[0])
    print(y)
    return y
r1=end_page()
i=1
while 1:
    if i==r1+1:
        break
    else:
        r = requests.get(url_1 + str(i) + url_2)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text)
            r.encoding = "utf8" 
            soup = BeautifulSoup(r.text, 'html.parser')
            stories = soup.find_all(attrs={'class':'intro__name'})
            stories2 = soup.find_all(attrs={'class':'intro__add'})
            stories3 = soup.find_all(attrs={'class':'pcShow'})
            stories4 = soup.find_all(attrs={'class':'item__price'})
            i = i + 1
            #print(stories,'\n','==================================================')
            # count=0
            for j in stories:
                #if i.text=='屋齡：':
                # tempStr=j.text
                # re.sub(r'\d','',tempStr)
                # tempStr.replace("地坪：.坪", "")
                # print(j.text)
                NameList.append(j.text)     
            for k in stories2:
                AddressList.append(k.text)
            for l in stories3:
                pcShow.append(l.text)
            for m in stories4:
                price.append(m.text)  
#將換行符號去除
pcShow2=[]
for i in pcShow:
    pcShow2.append(i.split()) 
price2=[]
for i in price:
    price2.append(i.split()) 
print(NameList,'\n\n',AddressList,'\n\n',pcShow2,'\n\n',price2)        
            