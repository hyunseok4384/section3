import sys
import io
import requests, json

#Rest : POST, GET, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

param = {'keywords':'서버'}
r = requests.get('http://api.saramin.co.kr/job-search', data=param)

#print(r.json())
print(r.encoding)
print(type(r))
print(r.text)

"""
for line in r.iter_lines(decode_unicode=True):
    b = json.loads(line)
    for e in b.keys():
        print('key : ', e, 'value : ', b[e])
"""
