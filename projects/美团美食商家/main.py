
import os
import re
import time
import random
import pickle
import argparse
import requests
from utils import *
from urllib.parse import urlencode


# 程序初始化
def initialProgram(cityname):
	cur_path = os.path.abspath(os.path.dirname(__file__))
	citynamesfilepath = os.path.join(cur_path, 'data/cities.json')
	uafilepath = os.path.join(cur_path, 'data/useragents.data')
	uuidfilepath = os.path.join(cur_path, 'data/uuid.data')
	brfilepath = os.path.join(cur_path, 'data/br.json')
	savedatapath = os.path.join(cur_path, '%s_data.json' % cityname)
	# cities
	if not os.path.isfile(citynamesfilepath):
		downCitynamesfile(citynamesfilepath)
	# uuid
	url = 'https://{}.meituan.com/meishi/'.format(cityname2CODE(cityname, citynamesfilepath))
	headers = {'User-Agent': getRandomUA(uafilepath)}
	res = requests.get(url, headers=headers)
	with open(uuidfilepath, 'w') as f:
		uuid = re.findall(r'"uuid":"(.*?)"', res.text, re.S)[0]
		f.write(uuid)
	# return
	return citynamesfilepath, uafilepath, uuidfilepath, brfilepath, savedatapath


# 主函数
def MTSpider(cityname, maxpages=50):
	# data_pages = {}
	citynamesfilepath, uafilepath, uuidfilepath, brfilepath, savedatapath = initialProgram(cityname)
	base_url = 'https://{}.meituan.com/meishi/api/poi/getPoiList?'.format(cityname2CODE(cityname, citynamesfilepath))
	try:
		for page in range(1, maxpages+1):
			print('[INFO]: Getting the data of page<%s>...' % page)
			data_page = None
			while data_page is None:
			
				params = getGETPARAMS(cityname, page, citynamesfilepath, uuidfilepath, brfilepath)
				url = base_url + urlencode(params)
				headers = {
							'Accept': 'application/json',
							'Accept-Encoding': 'gzip, deflate, br',
							'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
							'User-Agent': getRandomUA(uafilepath),
							'Connection': 'keep-alive',
							'Host': 'bj.meituan.com',
							'Referer': 'https://{}.meituan.com/'.format(cityname2CODE(cityname, citynamesfilepath))
						}
				res = requests.get(url, headers=headers)
			    # data_page = parsePage(json.loads(res.text))
				for item in parsePage(json.loads(res.text)):
					print(item)
					with open('杭州.txt','a',encoding='utf-8') as f:
       					 f.write(json.dumps(item,ensure_ascii=False)+'\n')
			
					if item is None:
						time.sleep(random.random()+random.randint(3, 6))
						initialProgram(cityname)
				# data_pages.update(parsePage(json.loads(res.text)))
				if page != maxpages:
					time.sleep(random.random()+random.randint(3, 6))
				data_page = 1
	except:
		print('[Warning]: Something wrong...')
	#with open(savedatapath, 'wb') as f:
		#pickle.dump(data_pages, f)


# run
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Spider for gourmet shops in meituan.")
	parser.add_argument('-c', dest='cityname', help='The city you choose to crawl.', default='杭州')
	parser.add_argument('-p', dest='maxpages', help='Max pages to crawl.', default=50, type=int)
	args = parser.parse_args()
	cityname = args.cityname
	maxpages = args.maxpages
	MTSpider(cityname, maxpages)