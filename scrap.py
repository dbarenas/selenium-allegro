# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import date, datetime, timedelta
import requests
import json

headers = {'content-type': 'application/json'}
sjson={'password':'Jules@2013','username':'donpulpo@gmail.com'}
r = requests.post('https://hudson.reportingexchange.com/access/loginxhr?language=en', data=json.dumps(sjson), headers=headers)
result=(r.text)
print result.split('"')[3]


headers = {"Authorization":"Bearer "+result.split('"')[3]}
r = requests.get('https://hudson.reportingexchange.com/api/reportingprovisionpublic/401?language=en', headers=headers)

print r.text

# browser = webdriver.Firefox()

# browser.get('https://www.reportingexchange.com/reportingProvision/401')


# selenium.addCustomRequestHeader( "Authorization","Bearer "+result.split('"')[3] );
