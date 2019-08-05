import requests
r=requests.get('https://user.qzone.qq.com/784356697/infocenter')
print(r.text)
print(r.status_code)
print(type(r))
print(type(r.text))
print(r.cookies)



# request库的高级用法：
# 文件上传
# 获取和设置cookies

rc = requests.get("https://www.baidu.com")
print(rc.cookies)

for key, value in rc.cookies.items():
    print(key + "=" + value)


# 400 bad request   
headers = {
    'Cookie': '_zap=df14dd98-9767-430f-b85e-7b959a3cbb53; d_c0="ANAiXVkvxg6PTooxnPzBne2VWeUxHvJq0W8=|1546598135"; __gads=ID=93cb37fafda6d28d:T=1546602802:S=ALNI_MY_93dxGrUpn_aJWAN7s25FS2FSuw; __utmv=51854390.100-1|2=registration_date=20170720=1^3=entry_date=20170720=1; _xsrf=GsYuIXgnjuKGesBLtdGU7iTzVFErI95g; _ga=GA1.2.1436942581.1547313503; tshl=; capsion_ticket="2|1:0|10:1562169418|14:capsion_ticket|44:MDcxNjE3ZjQwN2JkNDI1MDlkMWY0OWM2MDcyNjM1YTQ=|c758a33604d484d6c705d9d4570dfa1b24164135f265d0d248be680343e15c13"; z_c0="2|1:0|10:1562169437|4:z_c0|92:Mi4xUHVsNkJRQUFBQUFBMENKZFdTX0dEaVlBQUFCZ0FsVk5YUjRLWGdEYVNrUmo0ZTlSXzlIMktxN09VZFFBS0NEMXZB|728c8e1d02656dca4d421e7db4ba3ed9bd1bb5a6167eac12803f2e99c733912e"; q_c1=53e80c330dad4f3b83190cc7314bed71|1562674184000|1546602151000; __utma=51854390.1436942581.1547313503.1560175255.1564105986.45; __utmz=51854390.1564105986.45.45.utmcsr=github.com|utmccn=(referral)|utmcmd=referral|utmcct=/greatghoul/remote-working; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; tst=r',

    'Host': 'https://www.zhihu.com/',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

r2 = requests.get('https://www.zhihu.com/', headers=headers)
print(r2.text)
