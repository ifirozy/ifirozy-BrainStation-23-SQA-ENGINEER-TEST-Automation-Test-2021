from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://www.phptravels.net/home")
search_country = 'malaysia'
driver.find_element_by_class_name('tours').click()
driver.find_element_by_id("s2id_autogen19").click()
driver.find_element_by_class_name('select2-focused').send_keys('Malaysia')
driver.find_element_by_class_name('select2-result-sub').click()
driver.find_element_by_id("tourtype_chosen").click()

dropDowns = driver.find_element_by_class_name("chosen-results");

driver.find_element_by_xpath("//ul[@class='chosen-results']//li[6]").click()
driver.execute_script("document.getElementById('DateTours').value='09/07/2021'")
driver.find_element_by_class_name('bootstrap-touchspin-up').click()
driver.find_element_by_xpath("//button[@class='btn-primary']").click()


driver.find_element_by_xpath("//button[@class='btn-secondary']").click()
firstname = driver.find_element_by_name("firstname")
lastname = driver.find_element_by_name("lastname")
email = driver.find_element_by_name("email")
confirmemail = driver.find_element_by_name("confirmemail")
phone = driver.find_element_by_name("phone")
address = driver.find_element_by_name("address")

dropDowns = driver.find_element_by_class_name("chosen-single");
driver.find_element_by_xpath("//ul[@class='chosen-results']//li[6]").click()

                                   
driver.find_element_by_name("submit").click()


# driver.find_element_by_class_name('bootstrap-touchspin-up').click()


# driver.find_element_by_class_name("form-icon-left").click()

# driver.find_element_by_class_name('highlighted').click()

# dropEle.click()
# dropAttr = dropDowns.get_attribute("data-option-array-index")
# dropAttr = dropEle.get_attribute("data-option-array-index")
# print(dropAttr)



# find_element_by_xpath
# dropEle = driver.find_element_by_xpath("//ul[@class='chosen-results']//li")
# dropEle.

# dropDownsNext = dropDowns.get_attribute("data-option-array-index")==8
# print(dropDownsNext)
# dropDownsNext.click()


# el = driver.find_element_by_id('tourtype')
# for option in el.find_elements_by_tag_name('option'):
#     if option.text == 'Yact':
#         option.click()
# objSelect.selectByIndex(8);



# WebDriverWait(driver, 10).until(driver.find_element_by_class_name('select2-input').send_keys('Malaysia'))

# btn btn-white bootstrap-touchspin-up 