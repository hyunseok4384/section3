import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options() #인스턴스 생성
chrome_options.add_argument("--headless") #CLI

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\section3\webdriver\chrome\chromedriver')
#driver = webdriver.Chrome(r'C:\section3\webdriver\chrome\chromedriver') GUI
#driver.set_window_size(1920,1280)
#driver.implicitly_wait(5) 암묵적으로 5초정도 기다린다(리소스가 다 로딩되면 5초보다 빨리 끝날수도 있음)

driver.get('https://google.com')
#time.sleep(5)
driver.save_screenshot("c:/website1_ch.png")

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot("c:/website2_ch.png")

driver.quit()
print("스크린샷 완료")
