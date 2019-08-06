#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
初始网页：https://www.meituan.com/

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome(chrome_options=option)
wait = WebDriverWait(browser, 10)


def get_browser(keyword):
    try:
        browser.get('https://www.meituan.com/')
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.header-search-input'))
        )  # 获得输入框
        submit_click = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.header-search-btn'))
        )  # 获得提交按钮
        element.send_keys(keyword)  # 给予条件
        submit_click.click()  # 点击提交，页面跳转
        get_products()
    except TimeoutError:
        print("链接超时")


def to_next_page(must_page):
    next_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-item.next-btn.active'))
    )  # 获得下一页按钮
    next_button.click()
    now_page = int(wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-item.select.num-item'))
    ).text)
    if now_page == must_page:
        get_products()
        print(must_page)


def main(keyword):
    total = get_browser(keyword)
    for i in range(2, 10):     # 放开注释，可以执行翻页动作。
        time.sleep(3)
        to_next_page(i)


def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.common-list-main'))
    )
    html = browser.page_source
    doc = pq(html)
    items = doc('.common-list-main .default-list-item.clearfix').items()
    for i in items:
        a_url = i.find('.link.list-item-pic.backup-color').attr('href')  # 得到下级url
        name = i.find('.list-item-desc .list-item-desc-top .link.item-title').text()  # 得到名称
        # 打开新页签，访问URL
        browser.switch_to.window(browser.window_handles[0])
        browser.execute_script('window.open()')
        browser.switch_to.window(browser.window_handles[1])
        browser.get("https:" + a_url)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.details.clear'))
        )
        dep_page = browser.page_source
        dep_doc = pq(dep_page)
        address = dep_doc('.address p').items()
        data = "名称：%s ," % name
        for i in address:
            data = " " + data + i.text() + ","
        data = data + " 原始地址：%s" % a_url
        print(data)
        save_data(data)
        browser.close()


def save_data(data):
    with open('result.txt', 'a', encoding='utf8') as w:  # 文本追加模式
        w.write(data + '\n')
    w.close()


if __name__ == '__main__':
    main('美食')