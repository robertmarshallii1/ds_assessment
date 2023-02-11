from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd

## Create webdriver object and grab VTEC page
s=Service('./chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://mesonet.agron.iastate.edu/vtec/')

## Placeholder data frame to store results
df = pd.DataFrame()

## Package search options into a dictionary
opts = {'wfo': 'KEKA', 'phenomena': 'FW', 'year': '2020'}

## Set select menus to appropriate values
for k,v in opts.items():
    sel = Select(browser.find_element(By.ID,k))
    sel.select_by_value(v)

## Set event number
en = browser.find_element(By.ID, 'etn')
en.clear()
en.send_keys('2')

## Click submit button
browser.find_element(By.ID, 'myform-submit').click()

## Pause to let results table load
sleep(1)

## Load results table rows
tbl = browser.find_elements(By.XPATH, '//table[@id="ugctable"]/tbody/tr')


for r in tbl:
    d = r.find_elements(By.TAG_NAME, 'td')
    for i in d:
        print(i.text)
