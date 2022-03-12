# Write you web scraping code here.

import time
from selenium import webdriver
from bs4 import BeautifulSoup


from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException        

print("hello")

dr = webdriver.Chrome(executable_path='C:/Users/paule/Chrome Driver/chromedriver.exe')
dr.get("https://isearch.asu.edu/asu-people/")

search_bar = dr.find_element_by_class_name("input-main-search")
search_bar.send_keys('professor or lecturer')
search_bar.send_keys(Keys.RETURN)

time.sleep(1)

def check_exists_by_id(id):
    try:
        dr.find_element_by_id(id)
    except NoSuchElementException:
        return False

def check_exists_by_class(className):
    try:
        dr.find_element_by_class_name(className)
    except NoSuchElementException:
        return False

for i in range(10):
    dr.find_element_by_xpath("//html").click()
    
    bs = BeautifulSoup(dr.page_source,"html5")

    listOfLinks = bs.find_all('a', {'class': 'displayName'})

    # listOfNames = []

    for e in listOfLinks:
        print(e.get_text())
    
    time.sleep(1)
    
    if(check_exists_by_class('fsrAbandonButton')):
        dr.find_element_by_class('fsrAbandonButton').click()
        dr.find_element_by_class('fsrDeclineButton').click()
        dr.find_element_by_xpath("//html").click()
        dr.find_element_by_class('fsrModalBackdrop').click()
        dr.find_element_by_class('fsrButton__inviteDecline').click()
        dr.find_element_by_id('fsrFullScreenContainer')
        time.sleep(1)

    next_button = dr.find_element_by_class_name("pager-next").click()




