# 强大的解析工具BeautifulSoup,借助网页的结构和属性等特性来解析网页

from bs4 import BeautifulSoup   
html = """
<head>
  <title>热映口碑榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//s0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//analytics.meituan.com" />
  <link rel="dns-prefetch" href="//report.meituan.com" />
  <link rel="dns-prefetch" href="//frep.meituan.com" />

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(soup.title.string) # 获取内容
print(soup.title.name)
print(soup.meta.attrs)  # 获取属性
print(soup.link)


# 关联选择

print(soup.head.contents)
print(soup.head.children)
for i, child in enumerate(soup.head.children):
    print(i,child)

print(soup.title.parent)   # 父节点, 祖先节点呢？（parents）

# 兄弟节点
# next_sibling
# previous_sibling

# 提取信息

# 方法选择器
# find_all(name, attrs, recursive, text, **kwargs)
for link in soup.find_all(name='link'):
    print(link)

print(soup.find_all(attrs={'rel': 'dns-prefetch'}))


# find :只返回第一个匹配的元素