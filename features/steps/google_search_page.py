
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

import time


# BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
# BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
# desired_cap = {
#    'os_version': '10',
#    'resolution': '1920x1080',
#    'browser': 'Chrome',
#    'browser_version': '94.0',
#    'os': 'Windows',
#    'name': 'BStack-[Python] Smoke Test for shadowandact.com google search for shadow & act on desktop',
#    'build': 'BStack Build Number'
# }
#
# desired_cap["chromeOptions"] = {}
# desired_cap["chromeOptions"]["args"] = ["--disable-notifications"]
# driver = webdriver.Remote(
#     command_executor='https://'+BROWSERSTACK_USERNAME+':'+BROWSERSTACK_ACCESS_KEY+'@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)


def navigate_to_google_page(driver):
    driver.maximize_window()
    driver.get("https://google.com")
    time.sleep(1)
    print(driver.title)
    # try:
    #     # time.sleep(2)
    #     WebDriverWait(driver, 5).until((ec.frame_to_be_available_and_switch_to_it(0)))
    #     # driver.switch_to.frame(0)
    # except NoSuchFrameException:
    #     print("No frame popup exists")
    try:
        # tmp = driver.find_element(By.ID, "introAgreeButton")
        # tmp.click()
        driver.find_element(By.ID, "L2AGLb").click()
        # driver.find_element_by_id("introAgreeButton").click()
        # driver.switch_to.default_content()
    except NoSuchElementException:
        print("No Such Element as no frame exists")
    # except NoSuchFrameException:
    #     print("No pop-up from Google")
    # try:
    #     WebDriverWait(driver, 40).until(ec.frame_to_be_available_and_switch_to_it(0))
    #     driver.switch_to.frame(0)
    #     driver.find_element(By.ID, "introAgreeButton").click()
    #     # driver.find_element_by_id("introAgreeButton").click()
    #     driver.switch_to.default_content()
    #     print("clicked on google pop-up")
    # except NoSuchElementException:
    #     print("No pop-up from Google")


def navigate_to_google_page_on_mobile(driver):
    driver.get("https://google.com")
    time.sleep(2)
    print(driver.title)


def search_keyword(driver, website_name):
    print("function called search_keyword ")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.XPATH, "//input[@name='q']")))
    search_text_box = driver.find_element(By.XPATH, "//input[@name='q']")
    search_text_box.send_keys(website_name)
    search_text_box.send_keys(Keys.RETURN)
    time.sleep(2)


def launch_app(driver):
    print("function called launch_app")
    result = driver.find_element(By.XPATH, "//a[@href='https://shadowandact.com/']")
    result.click()
    time.sleep(5)


def post_page_load_pop_up(driver):
    try:
        event_promo_pop_up = driver.find_element_by_xpath(
          "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
        driver.execute_script("arguments[0].click();", event_promo_pop_up)
    except NoSuchElementException:
        print("event promo pop-up does not exist")
    # try:
    #     driver.switch_to.frame("sp_message_iframe_565136")
    #     pop_up_text = driver.find_element(By.XPATH, "//p[normalize-space()='We value your privacy']")
    #     if pop_up_text.is_displayed():
    #         accept_button = driver.find_element(By.XPATH, "//button[@title='Accept']")
    #         accept_button.click()
    #     driver.switch_to.parent_frame()
    # except NoSuchElementException:
    #     print("blavity news privacy pop-up does not exist")
    footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
    driver.execute_script("arguments[0].click();", footer_xpath)
    assert driver.title == "SHADOW & ACT", "title does not match"


def verify_footer_presence(driver):
    time.sleep(3)
    footer_sanda_page = driver.find_element(
      By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    assert footer_sanda_page.is_displayed(), "Footer section for SHADOWANDACT is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(footer_sanda_page).perform()
    if footer_sanda_page.is_displayed():
        print("footer section is displayed on shadowandact page")
