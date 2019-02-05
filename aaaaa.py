import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class lolCafe:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\section3\webdriver\chrome\chromedriver")
        self.driver.implicitly_wait(30)
    def Login(self):
        self.driver.get("")
        self.driver.find_element_by_name('id').send_keys('######')
        self.driver.find_element_by_name('pw').send_keys('######')
        self.driver.find_element_by_xpath('').click()
