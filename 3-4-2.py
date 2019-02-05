import sys
import io
import requests
from bs4 import BeautifulSoup
import urllib.parse as rep
import os
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'log':'######',
    'pwd':'######',
    'user-submit':rep.quote_plus('로그인'),
    'user-cookie':1
}

with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F', data = LOGIN_INFO)
    #print('login_req',login_req.text)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://www.inflearn.com/members/cjswocl/course/')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text,'html.parser')
        badges = soup.select("div.badges > ul > li > a > img")
        for i,z in enumerate(badges,1):
            fullFileName = os.path.join("c:/",str(i)+".jpg")
            req.urlretrieve(z['src'],fullFileName)
