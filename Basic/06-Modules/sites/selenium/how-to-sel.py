#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# 把chrome driver放在PATH下面
# 调用chrome浏览器
driver = webdriver.Chrome()

# 打开界面
driver.get('https://www.baidu.com')
driver.find_element_by_name('wd').send_keys('test' + Keys.RETURN)

# 保存当前的网页的快照
driver.save_screenshot(driver.title+".png")

# 定位element并点击
driver.find_element_by_link_text('test_百度翻译').click()

# 跳转到打开的新窗口
print driver.current_url
driver.switch_to.window(driver.window_handles[1])
print driver.current_url

# 在新窗口内点击
driver.find_element_by_xpath('//*[@id="main-outer"]/div/div/div/div[1]/div[1]/a[1]/span').click()

# 关闭新窗口
driver.close()

# 调回到原来的窗口
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.frame()

# 关闭整个driver
driver.quit()