# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import date, datetime, timedelta

def checker(usr, pwd):

    browser = webdriver.Firefox()
    browser.request('POST', 'https://hudson.reportingexchange.com/access/loginxhr?language=en', data={"password":"Jules@2013","username":"donpulpo@gmail.com"})

    #browser.get('https://www.reportingexchange.com/loginform', )
    elem_name = browser.find_element_by_css_selector('#username')  # Find the input box
    elem_name.send_keys(usr)
    elem_pwd = browser.find_element_by_css_selector('#password')  # Find the input box
    elem_pwd.send_keys(pwd + Keys.RETURN)
    time.sleep(2)
    browser.find_element_by_css_selector('#LOGINFORM > div.ecoformActions.layout-align-space-between-stretch.layout-row > button.md-raised.pinkBTN.no-right-marg.formSubmit.center.pinkBTN.md-button.md-button').click()

    browser.get('https://www.reportingexchange.com/reportingProvision/401')

    # elem = browser.find_element_by_xpath("//*")
    # source_code = elem.get_attribute("outerHTML")

# //*[@id="holdView"]/div[2]/section/div/md-card
    # encostr = unicode(search_string, encoding='utf-8')
    # list = []
    # if source_code.find(encostr) > 1:
    #     # if random.randint(1, 2) == 1:
    #     list.append(usr+','+pwd+',(C)\n')
    # else:
    #     list.append(usr+','+pwd+',(S)\n')

    return list

user='donpulpo@gmail.com'
pwd='Jules@2013'

list_data = checker(user, pwd)
print list_data



# use login donpulpo@gmail.com
# pwd is Jules@2013
# the pages to save have a standard structure https://www.reportingexchange.com/reportingProvision/401
