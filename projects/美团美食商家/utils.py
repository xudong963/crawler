import zlib
import time
import json
import base64
import random
import requests
from pyquery import PyQuery


# 城市名转城市拼音码
def cityname2CODE(cityname, citynamesfilepath):
	with open(citynamesfilepath, 'r', encoding='utf-8') as f:
		citynames_dict = json.load(f)
		code = citynames_dict[cityname]
	return code


# 读取保存的uuid
def readUUID(uuidfilepath):
	with open(uuidfilepath, 'r') as f:
		uuid = f.read().strip()
	return uuid


# 随机生成一个UA
def getRandomUA(uafilepath):
	with open(uafilepath, 'r') as f:
		ua = random.choice(f.readlines())
		ua = ua.strip('\n')
	return ua


# 城市名-拼音码爬取
def downCitynamesfile(citynamesfilepath):
	url = 'https://www.meituan.com/changecity/'
	doc = PyQuery(requests.get(url).text)
	cities_dict = dict()
	[cities_dict.update({city.text(): city.attr('href').replace('.', '/').split('/')[2]}) for city in doc('.cities a').items()]
	with open(citynamesfilepath, 'w', encoding='utf-8') as f:
		f.write(json.dumps(cities_dict, indent=2, ensure_ascii=False))


# 获取Get请求所需的参数
def getGETPARAMS(cityname, page, citynamesfilepath, uuidfilepath, brfilepath):
	uuid = readUUID(uuidfilepath)
	city_code = cityname2CODE(cityname, citynamesfilepath)
	data = {
			'cityName': cityname,
			'cateId': '0',
			'areaId': '0',
			'sort': '',
			'dinnerCountAttrId': '',
			'page': page, 
			'userId': '',
			'uuid': uuid,
			'platform': '1',
			'partner': '126',
			'originUrl': 'https://{}.meituan.com/meishi/'.format(city_code),
			'riskLevel': '1',
			'optimusCode': '1',
			'_token': getToken(brfilepath, city_code, uuid, page, cityname)
		}
	return data


# 获取SIGN
def getSIGN(cityname, page, uuid, city_code):
	url = 'https://{}.meituan.com/meishi/'.format(city_code)
	sign = 'areaId=0&cateId=0&cityName={}&dinnerCountAttrId=&optimusCode=1&originUrl={}&page={}&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid={}'
	sign = sign.format(cityname, url, page, uuid)
	return sign


# 获取_token参数
def getToken(brfilepath, city_code, uuid, page, cityname):
	ts = int(time.time() * 1000)
	with open(brfilepath, 'r') as f:
		brs_dict = json.load(f)
	key = random.choice(list(brs_dict.keys()))
	info = brs_dict[key]
	_token = {
				'rId': 100900,
				'ver': '1.0.6',
				'ts': ts,
				'cts': ts + random.randint(100, 120),
				'brVD': info.get('barVD'),
				'brR': [info.get('brR_one'), info.get('brR_two'), 24, 24],
				'bI': ['https://{}.meituan.com/meishi/'.format(city_code),''],
				'mT': [],
				'kT': [],
				'aT': [],
				'tT': [],
				'aM': '',
				'sign': getSIGN(cityname, page, uuid, city_code)
			}
	return base64.b64encode(zlib.compress(str(_token).encode())).decode()


# 解析一页数据
def parsePage(data_page):
	# data_parse = dict()
	infos = data_page.get('data')
	print(infos)
	if infos is None:
		return None
	else:
		infos = infos.get('poiInfos')
		
		for info in infos:
			# 店名: 地址, 评论数量, 平均得分, 平均价格, 电话
			# data_parse[info.get('title')] = [info.get('address'), info.get('allCommentNum'), info.get('avgScore'), info.get('avgPrice'), info.get('phone')]
			yield{
				'店名': info.get('title'),
				'地址': info.get('address'),
				'评论数量': info.get('allCommentNum'),
				'平均得分': info.get('avgScore'),
				'平均价格': info.get('avgPrice'),
				'电话': info.get('phone')
			}
