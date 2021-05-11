# 导入所有所需包
import time  # 获取当前时间，实现定时抢票
from bs4 import BeautifulSoup  # 从HTML中提取数据
from selenium import webdriver  # 驱动浏览器

browser = webdriver.Chrome()  # 打开Chrome浏览器
# 【将链接替换为对应剧场门票链接】
browser.get('https://shop.48.cn/tickets/item/4030')  # 跳转页面

# 【手动登陆账号】

html_k = browser.execute_script('return document.documentElement.outerHTML')  # 获取当前页面的HTML
bs_k = BeautifulSoup(html_k, 'html.parser') 

click_time = 0

# seattype2：VIP座票；seattype3：普通座票；seattype4：普通站票
# 【根据所需座位类型，配置】（也可手动勾选调整）
determine = browser.find_element_by_xpath('//em[@id="seattype4"]')  # 勾选座位类型
browser.execute_script('arguments[0].click();', determine)

while True:  # 无限循环
    if click_time > 0:  # 直到点击一次购票
        break
    if time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) == '2021-05-11 20:00:00':  # 设置抢票时间
        determine = browser.find_element_by_xpath('//a[@class="blue_nb_2 ma_r10"]')  # 点击购买
        browser.execute_script('arguments[0].click();', determine)
        click_time += 1  # 退出程序