# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import date, datetime, timedelta
import requests
import json
import random
import unicodedata 

headers = {'content-type': 'application/json'}
sjson={'password':'Jules@2013','username':'donpulpo@gmail.com'}
r = requests.post('https://hudson.reportingexchange.com/access/loginxhr?language=en', data=json.dumps(sjson), headers=headers)
result=(r.text)
# print result.split('"')[3]



a=range(1000,30000,1)

headers = {"Authorization":"Bearer "+result.split('"')[3]}
res=[]
fw = open('ll_organization.txt', 'r+')

for seq in a:
	r = requests.get('https://hudson.reportingexchange.com/api/provisioningorganisation/'+str(seq)+'?language=en', headers=headers)
	#r = requests.get('https://hudson.reportingexchange.com/api/reportingprovisionpublic/'+str(seq)+'?language=en', headers=headers)
	print r.text
	fw.write((r.text).encode("utf-8")+'\n')

	# res.append(r.text)

fw.writelines(res)

# fw = open('ll_result.txt', 'r+')
# fw.write('user:password,status\n')
# res.append(list_data[0])

# fw.writelines(res)