import requests
from selenium import webdriver
import time

driver = webdriver.Chrome()



#driver.get('https://cmsweb.fresnostate.edu/psc/CFRPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL')
#Or
driver.get('https://portal.cms.fresnostate.edu/x/_class_search')

#need to figure out how to get past sign in
#doesnt ask sometimes, does other times


time.sleep(10)



#Have to activate the actual search first before I can click on a button

try:
    button = driver.find_element_by_id('win0divSSR_CLS_DTL_WRK_CLASS_NBR')
    button.click()

except:
    print("nope")


data = driver.find_element_by_id('win0divSSR_CLS_DTL_WRK_ENRL_TOT')

print(data.text)

driver.quit()