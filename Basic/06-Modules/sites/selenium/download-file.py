# -*- coding:utf-8 -*-


from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# chrome设置
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,       # 禁止弹窗
    'download.default_directory': r'D:\test',            # 设置下载地址
    "profile.managed_default_content_settings.images": 2,  # 2 禁止加载图片 1 加载图片
    "profile.managed_default_content_settings.javascript": 2,  # 2 禁止加载JS 1 加载JS
}
options.add_experimental_option('prefs', prefs)

# 把chrome driver放在PATH下面
# 调用chrome浏览器
driver = webdriver.Chrome(chrome_options=options)
# 设置网页加载超时时间和脚本加载超时时间
driver.set_page_load_timeout(10)
driver.set_script_timeout(10)

# 打开界面
driver.get('http://192.168.1.51:9009/code_package_manager')
driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[6]/a').click()

# 更多chrome支持的参数
# 最大化启动
# options.add_argument('--start-maximized')
# 隐身模式
# options.add_argument('--incognito')
# 设置代理
# options.add_argument('--proxy-server=http://127.0.0.1:1080')
