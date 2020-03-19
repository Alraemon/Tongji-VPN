#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser=webdriver.Chrome(executable_path="/home/erwin/Telegram/TJVPN/chromedriver",chrome_options=chrome_options)
browser.get("https://vpn.tongji.cn")
username=browser.find_element_by_name("username")
passwd=browser.find_element_by_name("password")
realm=Select(browser.find_element_by_name("realm"))
submit=browser.find_element_by_name("btnSubmit")
username.send_keys("1550918")
passwd.send_keys("410789")
realm.select_by_value("统一身份认证用户")
submit.click()
cookies=browser.get_cookies()
if len(cookies)==3:
    btnCont=browser.find_element_by_name("btnContinue")
    btnCont.click()
    cookies=browser.get_cookies()
for cookie in cookies:
    if cookie['name']=='DSID':
        print(cookie['value'])
        break
#browser.close()
