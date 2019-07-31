import requests,re,time,json

def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    respond=requests.get(url,headers=headers)
    if respond.status_code==200:
        return respond.text
    else:
        return None


def parse_one_page(html):
    pattern=re.compile(
        '<dd>.*?board-index.*?>(\\d+)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?<p.*?integer.*?>(.*?)</i><i.*?>(.*?)</i>',
        re.S
    )    # re.S的作用是:使.匹配包括换行符在内的所有字符
    items=re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'name':item[2].strip(),
            'score':item[3].strip()+item[4].strip()
        }

def write_to_file(content):
    with open('猫眼电影排名榜(前100).txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)   #延迟等待(针对反爬虫)


#排名：<dd>.*?board-index.*?>(.*?)</i>
#图片：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
#名字：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>
#评分：<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?<p.*?integer.*?>(.*?)</i><i.*?>(.*?)</i>
