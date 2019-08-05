# 动态渲染页面爬取

# 声明浏览器对象
from selenium import webdriver

browser = webdriver.Chrome()

# 调用browser 对象, 执行各个动作模拟浏览器操作
browser.get('https://www.taobao.com/')
print(browser.page_source)

# 查找节点
# 找一下搜索框
# 三种方式
'''
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
'''

# 节点交互
# 输入文字: send_keys(), 清空文字: clear(), 点击按钮: click()
import time
input_first = browser.find_element_by_id('q')
input_first.send_keys('iPhone')
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()

# 动作链
# 执行JavaScript
# 获取节点信息
# 切换frame
# 延时等待
# 前进和后退
# 异常处理
