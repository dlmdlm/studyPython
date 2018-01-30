import time

from selenium import webdriver


driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")
driver.get('https://www.baidu.com')
print("网页头部： %s" % driver.title)
driver.find_element_by_id("kw").send_keys("狐妖小红娘")
print("等待3秒")
time.sleep(3)
driver.find_element_by_id("su").click()
print("等待10秒")
time.sleep(10)
driver.quit()
