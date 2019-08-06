# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pyquery import PyQuery as pq
from time import sleep

#定义一个taobao类

class taobao_infos:

    #对象初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches', ['enable-automation']) # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 30) #超时时长为10s


    #延时操作,并可选择是否弹出窗口提示
    def sleep_and_alert(self,sec,message,is_alert):

        for second in range(sec):
            if(is_alert):
                alert = "alert(\"" + message + ":" + str(sec - second) + "秒\")"
                self.browser.execute_script(alert)
                al = self.browser.switch_to.alert
                sleep(1)
                al.accept()
            else:
                sleep(1)


    #登录淘宝
    def login(self):

        # 打开网页
        self.browser.get(self.url)

        # 自适应等待，点击密码登录选项
        self.browser.implicitly_wait(30) #智能等待，直到网页加载完毕，最长等待时间为30s
        self.browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click()

        # 自适应等待，点击微博登录宣传
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath('//*[@class="weibo-login"]').click()

        # 自适应等待，输入微博账号
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_name('username').send_keys(weibo_username)

        # 自适应等待，输入微博密码
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_name('password').send_keys(weibo_password)

        # 自适应等待，点击确认登录按钮
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
        # 输出淘宝昵称
        print(taobao_name.text)




    # 获取天猫商品总共的页数
    def search_total_page(self):

        # 等待本页面全部天猫商品数据加载完毕
        #good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#m-itemlist > div.item.J_MouserOnverReq.item-ad')))
        sleep(5)
        #获取天猫商品总共页数
        number_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-page.g-clearfix > div.wraper > div.inner.clearfix > div.total')))
        page_total = number_total.text.replace("共","").replace("页，到第页 确定","").replace("，","")

        return page_total

    def crawl_good_data(self, key):
        # 对天猫商品数据进行爬虫
        self.browser.get("https://s.taobao.com/search?q="+key)
        page_total = self.search_total_page()
        return page_total

if __name__ == "__main__":

    chromedriver_path = "" #改成你的chromedriver的完整路径地址
    weibo_username = "" #改成你的微博账号
    weibo_password = "" #改成你的微博密码

    a = taobao_infos()
    a.login() #登录
    with open("file.txt") as f:
        for line in f.readlines():
            sleep(5)
            pageNum = a.crawl_good_data(line) #爬取天猫商品数据
            print(line.strip()+': '+str(pageNum))
