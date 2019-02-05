import sys
import io
from selenium import webdriver
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome(r"C:\section3\webdriver\chrome\chromedriver")
driver.set_window_size(1920,1280)

driver.get("https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F")
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element_by_name('log').send_keys('######')
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element_by_name('pwd').send_keys('######')
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
driver.implicitly_wait(5)
time.sleep(5)

driver.find_element_by_xpath('//*[@id="main-menu-item-29786"]/a/strong').click()
driver.implicitly_wait(5)
time.sleep(5)

driver.quit()
