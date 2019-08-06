import requests
import re
import os
import random
from bs4 import BeautifulSoup

def getRandomUA(uafilepath):
	with open(uafilepath, 'r') as f:
		ua = random.choice(f.readlines())
		ua = ua.strip('\n')
	return ua

poiId = 191784986

url = "https://www.meituan.com/meishi/"+ str(poiId);
print(url)
header = {
	'User-Agent': getRandomUA('data/useragents.data')
}
request = requests.get(url, headers = header)
print(request)
item = re.findall(r'"phone":(.*?),',str(request.text))
print(item)

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# 调用browser 对象, 执行各个动作模拟浏览器操作
browser.get(url)
