#HGTV script
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, re

"""
INSTRUCTIONS:
1. Do the first entry into the sweepstakes manually for HGTV and DIY.
2. Fill out the variables below.
    a. input your email address
    b. input the URLs of the sweepstakes submission pages.   
"""


EMAIL = ''

HGTV_URL = 'https://www.hgtv.com/design/hgtv-urban-oasis/sweepstakes?nl=R-HGTV:UO2018_2018-10-07_EnterHGTV&bid=14676682&c32=29b2da5c1b73d6947e773da4fffb8f754d647aab&ssid=2017_HGTV_confirmation_API&sni_by=&sni_gn='
DIY_URL = 'https://www.diynetwork.com/hgtv-urban-oasis?nl=R-HGTV:UO2018_2018-10-07_EnterDIY&bid=14676682&c32=29b2da5c1b73d6947e773da4fffb8f754d647aab&ssid=2017_HGTV_confirmation_API&sni_by=&sni_gn='






"""
Do not edit anything below this line unless you know what you are doing.
"""
driver = webdriver.Chrome(r"chromedriver.exe")
##HGTV
driver.get(HGTV_URL)
get_HGTV_source = driver.page_source
HGTV_ngxFrame = re.findall("ngxFrame\d\w+",get_HGTV_source)[0]
time.sleep(20)
driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + HGTV_ngxFrame + """"]"""))
time.sleep(2)
driver.find_element_by_id("xReturningUserEmail").send_keys(EMAIL)
time.sleep(5)
driver.find_element_by_xpath("""//*[@id="xCheckUser"]/span""").click()
time.sleep(20)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + HGTV_ngxFrame + """"]"""))
driver.find_element_by_xpath("""//*[@id="multioptin_0_Secondary"]""").click()
driver.find_element_by_xpath("""//*[@id="multioptin_0_Secondary"]""").click()
action = ActionChains(driver)
action.send_keys(Keys.TAB)
action.send_keys(Keys.ENTER)
action.perform()
time.sleep(10)

##DIY
driver.get(DIY_URL)
get_DIY_source = driver.page_source
DIY_ngxFrame = re.findall("ngxFrame\d\w+",get_DIY_source)[0]
time.sleep(20)
driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + DIY_ngxFrame + """"]"""))       
driver.find_element_by_id("xReturningUserEmail").send_keys(EMAIL)
time.sleep(5)
driver.find_element_by_xpath("""//*[@id="xCheckUser"]/span""").click()
time.sleep(20)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + DIY_ngxFrame + """"]"""))
driver.find_element_by_xpath("""//*[@id="multioptin_06_0_Secondary"]""").click()
driver.find_element_by_xpath("""//*[@id="multioptin_06_0_Secondary"]""").click()
action = ActionChains(driver)
action.send_keys(Keys.TAB)
action.send_keys(Keys.ENTER)
action.perform()
time.sleep(10)

driver.quit()
