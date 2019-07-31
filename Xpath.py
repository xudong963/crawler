# XPath 全程XML Path Language

from lxml import etree
text = '''
<div>
<ul>
<li>first</li>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result)

html1 = etree.parse('test.html', etree.HTMLParser())
result1 = etree.tostring(html1)
print(result1)

# 所有节点
result2 = html1.xpath('//*')
print(result2)


# 子节点
result3 = html1.xpath('//li/a')   # //li 用于选中所有的li节点，/a用于选中li节点的所有直接节点a
# 子孙节点
# or result3 = html.xpath('//li//a')
print(result3)

# 父节点
result4 = html1.xpath('//a[@href="link4.html"]/..')  # href属性为link4.html的a节点的父节点
print(result4)

# 文本获取：text()方法
result5 = html1.xpath('//li/a[@href="link4.html"]/text()')
print(result5)

# 属性多值匹配：需要使用contains()方法，第一个参数传入属性名称，第二个参数传入属性值

# 多属性匹配: 需要使用 and 连接
