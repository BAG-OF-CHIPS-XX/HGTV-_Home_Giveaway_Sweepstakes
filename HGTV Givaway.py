#HGTV script
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time, re

"""
INSTRUCTIONS:
1. Do the first entry into the sweepstakes manually for HGTV and DIY.
2. Fill out the variables below.
    a. input your email address
    b. input the URLs of the sweepstakes submission pages.   
"""


EMAIL = ''

HGTV_URL = 'https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes/'
DIY_URL = 'https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-smart-home-sweepstakes'







"""
Do not edit anything below this line unless you know what you are doing.
"""
try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Chrome(ChromeDriverManager().install())
# ##HGTV
driver.get(HGTV_URL)
get_HGTV_source = driver.page_source
HGTV_ngxFrame = re.findall("ngxFrame\d\w+",get_HGTV_source)[0]
print (HGTV_ngxFrame)
time.sleep(20)
driver.switch_to.frame(driver.find_element_by_id(HGTV_ngxFrame))
time.sleep(2)
driver.find_element_by_id("xReturningUserEmail").send_keys(EMAIL)
time.sleep(5)
driver.find_element_by_xpath("""//*[@id="xCheckUser"]/span""").click()
time.sleep(20)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id(HGTV_ngxFrame))
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
# driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + DIY_ngxFrame + """"]"""))     
driver.switch_to.frame(driver.find_element_by_id(DIY_ngxFrame))   
driver.find_element_by_id("xReturningUserEmail").send_keys(EMAIL)
time.sleep(5)
driver.find_element_by_xpath("""//*[@id="xCheckUser"]/span""").click()
time.sleep(20)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id(DIY_ngxFrame))
submit_button_form = driver.find_element_by_id("xSecondaryForm")
submit_button_form.find_element_by_id("""xSubmitContainer""").click()
action = ActionChains(driver)
action.send_keys(Keys.TAB)
action.send_keys(Keys.ENTER)
action.perform()
time.sleep(10)

driver.quit()
