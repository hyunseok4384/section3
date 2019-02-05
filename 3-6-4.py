import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome(r"C:\section3\webdriver\chrome\chromedriver")
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get("https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F")
time.sleep(7)
driver.implicitly_wait(3)

driver.find_element_by_name('log').send_keys('######')
driver.implicitly_wait(1)
time.sleep(2)
driver.find_element_by_name('pwd').send_keys('######')
driver.implicitly_wait(1)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
