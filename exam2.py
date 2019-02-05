import sys
import io
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse as rep
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

LOGIN_INFO = {
    'log':'######',
    'pwd':'######',
    'user-submit':rep.quote_plus('로그인'),
    'user-cookie':1
}

SavePath = "C:/20190121/"

with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F', data=LOGIN_INFO)
    if login_req.status_code == 200 and login_req.ok:
        study_info = s.get("https://www.inflearn.com/members/cjswocl/course/")
        study_info.raise_for_status()
        #print(study_info.text)
        soup = BeautifulSoup(study_info.text,"html.parser")
        #print(soup.prettify)
        study_list = soup.select("div.course.mycourse > ul#course-list > li")
        print(study_list)

        for z,i in enumerate(study_list,1):
            img = i.select_one("div.col-md-4.col-sm-4 > a > img")
            fullFileName = os.path.join(SavePath,str(z)+".jpg")
            req.urlretrieve(img['src'],fullFileName)
            i.select_one("div.col-md-8.col-sm-8 > div.item-desc > p")
            with open(SavePath+str(z)+".txt", "wt") as fp:
                fp.write(i.string)
