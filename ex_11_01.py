import re
from bs4 import BeautifulSoup
import ssl
import urllib.request,urllib.parse,urllib.error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('enter url-')
html=urllib.request.urlopen(url,context=ctx) 

soup=BeautifulSoup(html,'html.parser')
tags=soup('span')

numberstrings=list()
for item in tags:
    y=re.findall('[0-9]+',item.decode())
    numberstrings.append(y)


intnumbers=list()
for list1 in numberstrings:
    for number in list1:
    
        number1=int(number)
        intnumbers.append(number1)
    
print(sum(intnumbers))    