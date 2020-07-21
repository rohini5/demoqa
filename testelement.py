from selenium import webdriver
from hamcrest import *
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time
import pdb


driver = none


@pytest.fixture(scope='function', autouse='true')
def openwebpage(request):
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    driver.get("http://demoqa.com/")
    driver.maximize_window()

    yield

        # if request.session.testsfailed != failed_before:
        #     test_name = request.node.name
        #     take_screenshot(driver, test_name)
    driver.close()


# def take_screenshot(driver, test_name):
#     screenshots_dir= "/Users/rohinisrivastava/Desktop/Hplaptopdocuments/desktop/chapter1/Test_cases/demoqa/screenshots_dir"
#     screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
#     driver.save_screenshot(screenshot_file_path)

@pytest.fixture()
def elementiconopen():
    global driver
    element_card = driver.find_elements_by_css_selector('.top-card')[0]
    element_card.click()
    # or
    # sendKeys(Keys.RETURN)
class TestElementIcon:

    # def test_leftpannel_menulist(self):
    #     global driver
    #     leftpannel_count_expected= 8
    #     # pdb.set_trace()
    #     leftpannel_count_actual = len(driver.find_elements_by_css_selector('.element-list.collapse.show>ul>li'))
    #     assert_that(leftpannel_count_expected, equal_to(leftpannel_count_actual))


    @pytest.mark.testbox
    def test_textbox_positive(self,elementiconopen):
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
        time.sleep(5)
        submit_button = driver.find_element_by_id('submit')
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        expected = 'Name:'+text_to_be_send_name+'\n'+'Email:'+text_to_be_send_email+'\n'+'Current Address :'+text_to_be_send_current_address+'\n'+'Permananet Address :'+text_to_be_send_permananentAddress
        actual= driver.find_element_by_id('output').text
        assert_that (expected,equal_to(actual))

    @pytest.mark.testbox
    def test_textbox_negative(self,elementiconopen):
        global driver
        textbox_icon = driver.find_element_by_id('item-0')
        textbox_icon.click()
        input_name = driver.find_element_by_id('userName')
        input_name.clear()
        text_to_be_send_name = 'ppppp'
        input_name.send_keys(text_to_be_send_name)
        input_emailid = driver.find_element_by_id('userEmail')
        input_emailid.clear()
        text_to_be_send_email = 'rdtdrtr@dbjqbdi.dwbd'
        input_emailid.send_keys(text_to_be_send_email)
        input_current_address = driver.find_element_by_id('currentAddress')
        input_current_address.clear()
        text_to_be_send_current_address = 'dytfuygudtstrfchjbgy'
        input_current_address.send_keys(text_to_be_send_current_address)
        input_permananentAddress = driver.find_element_by_id('permanentAddress')
        input_permananentAddress.clear()
        text_to_be_send_permananentAddress = 'dyfyddhgyutytfgfyj'
        input_permananentAddress.send_keys(text_to_be_send_permananentAddress)
        # pdb.set_trace()
        submit_button = driver.find_element_by_id('submit')
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        expected = ''
        actual = driver.find_element_by_id('output').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.testbox
    def test_textbox_blank(self,elementiconopen):
        global driver
        textbox_icon = driver.find_element_by_id('item-0')
        textbox_icon.click()
        input_name = driver.find_element_by_id('userName')
        input_name.clear()
        text_to_be_send_name = ''
        input_name.send_keys(text_to_be_send_name)
        input_emailid = driver.find_element_by_id('userEmail')
        input_emailid.clear()
        text_to_be_send_email = ''
        input_emailid.send_keys(text_to_be_send_email)
        input_current_address = driver.find_element_by_id('currentAddress')
        input_current_address.clear()
        text_to_be_send_current_address = ''
        input_current_address.send_keys(text_to_be_send_current_address)
        input_permananentAddress = driver.find_element_by_id('permanentAddress')
        input_permananentAddress.clear()
        text_to_be_send_permananentAddress = ''
        input_permananentAddress.send_keys(text_to_be_send_permananentAddress)
        # pdb.set_trace()
        submit_button = driver.find_element_by_id('submit')
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        expected = ''
        actual = driver.find_element_by_id('output').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.checkbox
    def test_checkboxhome(self,elementiconopen):
        global driver
        checkbox_icon = driver.find_element_by_id('item-1')
        checkbox_icon.click()
        home_checkbox = driver.find_element_by_css_selector('.rct-checkbox')
        home_checkbox.click()
        expected= 'You have selected :\nhome\ndesktop\nnotes\ncommands\ndocuments\nworkspace\nreact\nangular\nveu\noffice\npublic\nprivate\nclassified\ngeneral\ndownloads\nwordFile\nexcelFile'
        actual= driver.find_element_by_id('result').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.checkbox
    def test_checkbox_home(self,elementiconopen):
        global driver
        checkbox_icon = driver.find_element_by_id('item-1')
        checkbox_icon.click()
        expand_button=driver.find_element_by_css_selector('#tree-node>ol>li>span>button')
        expand_button.click()

        checkbox_desktop= driver.find_elements_by_css_selector('span.rct-title')
        for i in checkbox_desktop:
            if i.text == 'Desktop':
                i.click()
        time.sleep(2)
        expected='You have selected :\ndesktop\nnotes\ncommands'
        actual= driver.find_element_by_id('result').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.checkbox
    def test_checkbox_count(self,elementiconopen):
        global driver
        checkbox_icon = driver.find_element_by_id('item-1')
        checkbox_icon.click()

        click_on_expand= driver.find_element_by_css_selector('.rct-option.rct-option-expand-all')
        click_on_expand.click()
        expected =16

        actual = len(driver.find_elements_by_css_selector('#tree-node > ol > li'))
        assert_that(expected, equal_to(actual))

    @pytest.mark.checkbox
    def test_checkbox_uucheckdesktop_icon(self,elementiconopen):
        global driver
        checkbox_icon = driver.find_element_by_id('item-1')
        checkbox_icon.click()
        home_checkbox = driver.find_element_by_css_selector('.rct-checkbox')
        home_checkbox.click()
        expand_button = driver.find_element_by_css_selector('#tree-node > ol > li > span > button > svg')
        expand_button.click()
        time.sleep(5)
        uncheck_desktopicon = driver.find_element_by_css_selector('#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox')
        uncheck_desktopicon.click()

        expected= 'You have selected :\ndocuments\nworkspace\nreact\nangular\nveu\noffice\npublic\nprivate\nclassified\ngeneral\ndownloads\nwordFile\nexcelFile'
        actual= driver.find_element_by_id('result').text
        assert_that(expected,equal_to(actual))

    @pytest.mark.checkbox
    def test_checkbox_unchecked_multiple_icon(self,elementiconopen):
        global driver
        checkbox_icon = driver.find_element_by_id('item-1')
        checkbox_icon.click()
        home_checkbox = driver.find_element_by_css_selector('.rct-checkbox')
        home_checkbox.click()
        click_on_expand = driver.find_element_by_css_selector('.rct-option.rct-option-expand-all')
        click_on_expand.click()
        uncheck_desktopicon = driver.find_element_by_css_selector('#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox')
        uncheck_desktopicon.click()
        uncheck_documenticon = driver.find_element_by_css_selector('#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox')
        uncheck_documenticon.click()
        expected = 'You have selected :\ndownloads\nwordFile\nexcelFile'
        actual = driver.find_element_by_id('result').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.checkbox
    def test_checkbox_checked_multiple_icon(self,elementiconopen):
        global driver
        checkbox_icon = driver.find_element_by_id('item-1')
        checkbox_icon.click()
        click_on_expand = driver.find_element_by_css_selector('.rct-option.rct-option-expand-all')
        click_on_expand.click()
        check_desktopicon = driver.find_element_by_css_selector('#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox')
        check_desktopicon.click()
        check_documenticon = driver.find_element_by_css_selector('#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox')
        check_documenticon.click()
        expected = 'you have selected :\ndesktop\nnotes\ncommands\ndocuments\nworkspace\nreact\nangular\nveu\noffice\npublic\nprivate\nclassified\ngeneral'
        actual = driver.find_element_by_id('result').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.radiobutton
    def test_radiobox_selectyes(self,elementiconopen):
        global driver
        radiobox_icon= driver.find_element_by_id('item-2')
        radiobox_icon.click()
        clickon_yes_radiobutton = driver.find_element_by_css_selector('#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(1) > div:nth-child(2)')
        clickon_yes_radiobutton.click()
        expected = 'You have selected Yes'
        actual= driver.find_element_by_css_selector('#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(1) > p').text
        assert_that(expected, equal_to(actual))

    @pytest.mark.radiobutton
    def test_radiobox_selectimpressive(self,elementiconopen):
        global driver
        radiobox_icon = driver.find_element_by_id('item-2')
        radiobox_icon.click()
        clickon_impressive_radiobutton = driver.find_element_by_css_selector('#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(1) > div:nth-child(3)')
        clickon_impressive_radiobutton.click()
        expected= 'You have selected Impressive'
        actual = driver.find_element_by_css_selector('#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(1) > p').text
        assert_that(expected, equal_to(actual))

    def test_



