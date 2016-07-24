# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import sqlite3

# 数据库模型
conn = sqlite3.connect('zufang_messages.db')
cursor = conn.cursor()
# cursor.execute('create table houses ('
#                'house_id varchar(20) primary key, '
#                'house_title varchar(20), '
#                'house_link varchar(20), '
#                'house_region varchar(20), '
#                'house_zone varchar(20), '
#                'house_meters varchar(20), '
#                'house_direction varchar(20), '
#                'house_floor varchar(20), '
#                'house_build_time varchar(20), '
#                'house_price varchar(20), '
#                'house_message_time varchar(20))'
#                )


class Lianjia(object):
    def __init__(self, district):
        self.district = district
        self.table = district
        self.url_init = r'http://bj.lianjia.com/zufang/' + self.district + '/'
        self.house_id = 0

    def get_total_page(self):
        soup = BeautifulSoup(requests.get(self.url_init, timeout=5).content, 'html.parser')
        total_page = eval(soup.find('div', attrs={'class': 'page-box house-lst-page-box'})['page-data'])['totalPage']
        return total_page

    def get_message(self):
        try:
            for page in range(1, self.get_total_page(self.url_init) + 1):
                print u'正在请求第 %s 页' % page
                print '=' * 20
                asking_url = self.url_init + str(page) + '/'
                asking_soup = BeautifulSoup(requests.get(asking_url, timeout=5).content, 'html.parser')
                house_tags = asking_soup.find_all('div', attrs={'class': 'info-panel'})
                for house in house_tags:
                    house_id += 1
                    house_title = house.find('a', attrs={'target': '_blank'})['title']
                    house_link = house.find('a', attrs={'target': '_blank'})['href']
                    house_region = house.find('span', attrs={'class': 'region'}).text
                    house_zone = house.find('span', attrs={'class': 'zone'}).text
                    house_meters = house.find('span', attrs={'class': 'meters'}).text
                    house_direction = house.find('span', attrs={'class': 'meters'}).next_sibling.text
                    house_floor = house.find('div', attrs={'class': 'con'}).text.split('/')[1]
                    house_build_time = house.find('div', attrs={'class': 'con'}).text.split('/')[2]
                    house_price = house.find('span', attrs={'class': 'num'}).text
                    house_message_time = house.find('div', attrs={'class': 'price-pre'}).text

                    cursor.execute('insert into houses (house_id, house_title, house_link, house_region, house_zone, house_meters, house_direction, house_floor, house_build_time, house_price, house_message_time) '
                                   'values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (house_id, house_title, house_link, house_region, house_zone, house_meters, house_direction, house_floor, house_build_time, house_price, house_message_time)
                                   )
                time.sleep(0.1)
        finally:
            cursor.close()                          # 关闭Cursor:
            conn.commit()                           # 提交
            conn.close()                            # 关闭Connection


if __name__ == '__main__':
    dongcheng = Lianjia('dongcheng')
    print dongcheng.get_total_page()
    # dongcheng.get_message()


# print u'房屋名称：', house.find('a', attrs={'target': '_blank'})['title']
# print u'房屋链接：', house.find('a', attrs={'target': '_blank'})['href']
# print u'地理位置：', house.find('span', attrs={'class': 'region'}).text
# print u'房屋户型：', house.find('span', attrs={'class': 'zone'}).text
# print u'房屋面积：', house.find('span', attrs={'class': 'meters'}).text
# print u'房屋朝向：', house.find('span', attrs={'class': 'meters'}).next_sibling.text
# print u'房屋楼层：', house.find('div', attrs={'class': 'con'}).text.split('/')[1]
# print u'建设时间：', house.find('div', attrs={'class': 'con'}).text.split('/')[2]
# print u'房屋价格：', house.find('span', attrs={'class': 'num'}).text
# print u'交通方式：', house.find('span', attrs={'class': 'fang-subway-ex'}).text
# print u'看房时间：', house.find('span', attrs={'class': 'haskey-ex'}).text
# print u'取暖方式：', house.find('span', attrs={'class': 'heating-ex'}).text


# headers = {
#     'Host': 'bj.lianjia.com',
#     'Referer': 'http://bj.lianjia.com/zufang/haidian/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
# }

