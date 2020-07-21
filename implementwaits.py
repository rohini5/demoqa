from selenium import webdriver
from hamcrest import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time
import pdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = none

@pytest.fixture(scope='function', autouse='true')
def openwebpage():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://demoqa.com/")
    driver.maximize_window()
    yield
    driver.quit()

@pytest.fixture()
def elementiconopen():
    global driver
    element_card = driver.find_elements_by_css_selector('.top-card')[0]
    element_card.click()

def test_textbox_positive(elementiconopen):
    global driver
    textbox_icon = driver.find_element_by_id('item-0')
    textbox_icon.click()
    input_name= driver.find_element_by_id('userName')
    text_to_be_send_name ='Rohini Srivastava'
    input_name.send_keys(text_to_be_send_name)
    input_emailid = driver.find_element_by_id('userEmail')
    text_to_be_send_email='rdtdrtr@gmail.com'
    input_emailid.send_keys(text_to_be_send_email)
    input_current_address = driver.find_element_by_id('currentAddress')
    text_to_be_send_current_address= 'dytfuygudtstrfchjbgy'
    input_current_address.send_keys(text_to_be_send_current_address)
    input_permananentAddress = driver.find_element_by_id('permanentAddress')
    text_to_be_send_permananentAddress= 'dyfyddhgyutytfgfyj'
    input_permananentAddress.send_keys(text_to_be_send_permananentAddress)

    submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'submit')))
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    submit_button.click()
    expected = 'Name:'+text_to_be_send_name+'\n'+'Email:'+text_to_be_send_email+'\n'+'Current Address :'+text_to_be_send_current_address+'\n'+'Permananet Address :'+text_to_be_send_permananentAddress
    actual= driver.find_element_by_id('output').text
    assert_that (expected,equal_to(actual))
