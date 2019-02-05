import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class AmebaWriteAtt:
    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\section3\webdriver\chrome\chromedriver")
        self.driver = webdriver.Chrome(r"C:\section3\webdriver\chrome\chromedriver")
        self.driver.implicitly_wait(30)
    def login(self):
        self.driver.get("https://dauth.user.ameba.jp/accounts/login")
        time.sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("accountId").send_keys("######")
        time.sleep(3)
        self.driver.find_element_by_name("password").send_keys("######")
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/form/div[3]/input').click()
        self.driver.implicitly_wait(30)
    def myList(self):
        self.driver.get("https://blog.ameba.jp/ucs/iine/list.html")
        self.driver.implicitly_wait(30)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        print(soup.select('#iineHistoryEntryFrame > tr'))

"""
        return soup.select("div#iineHistoryEntryFrame > tr.iineEntryCnt.skinAnchorColor")
    def printMyList(self,list):
        with open(r"C:\PrintMyList.txt","wt") as f:
            for i in list:
                f.write(i.select_one("div.entryTitle").string)
                print(i.select_one("div.entryTitle").string)
#iineHistoryEntryFrame > table > tbody > td:nth-child(1) > div > div
#iineHistoryEntryFrame > table > tbody > tr:nth-child(2)

"""
if __name__ == '__main__':
    p = AmebaWriteAtt()
    p.login()
    p.myList()
