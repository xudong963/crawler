# urllib: request, error, parse 三大模块


import urllib.request 
import urllib.parse

respond=urllib.request.urlopen('https://user.qzone.qq.com/784356697/infocenter')

print(respond.read().decode('utf-8'))

print(type(respond))
print(respond.status)
print(respond.getheaders())
print(respond.getheader('Server'))

data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
respond1=urllib.request.urlopen('https://user.qzone.qq.com/784356697/infocenter',data=data)
print(respond1.read().decode('utf8'))

request=urllib.request.Request('https://user.qzone.qq.com/784356697/infocenter')
respond2=urllib.request.urlopen(request)
print(respond2.read())
