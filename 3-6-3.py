import sys
import io
from selenium import webdriver
from selenium.Firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless")

drivers = webdriver.Firefox(firefox_options=firefox_options,executable_path=r"C:\section3\webdriver\firefox\geckodriver")

driver.get("https://google.com")

driver.save_screenshot("c:/website_fr1.png")

driver.get("https://www.daum.com")

driver.save_screenshot("c:/website_fr2.png")

drivers.quit()
print("스크린샷 완료!")
