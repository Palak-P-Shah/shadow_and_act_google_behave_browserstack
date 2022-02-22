from selenium import webdriver
from browserstack.local import Local
import os, json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/google_shadowandact_search.json'
# CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

bs_local = None

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']


def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)


def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()


def before_feature(context, feature):
    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
    # browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
    # browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

    desired_capabilities = {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'BStack-[Jenkins] behave sample Test using google search for shadowandact.com app testing',  # test name
        'build': build_name,  # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
        # 'browserstack.local': browserstack_local,
        # 'browserstack.localIdentifier': browserstack_local_identifier,
        'browserstack.user': username,
        'browserstack.key': access_key
    }

    # desired_capabilities = CONFIG['environments'][TASK_ID]
    #
    # for key in CONFIG["capabilities"]:
    #     if key not in desired_capabilities:
    #         desired_capabilities[key] = CONFIG["capabilities"][key]
    #
    # if "browserstack.local" in desired_capabilities and desired_capabilities["browserstack.local"]:
    #     start_local()

    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )


def after_feature(context, feature):
    if context.failed is True:
        context.browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At least 1 assertion failed"}}')
    if context.failed is not True:
        context.browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All assertions passed"}}')
    context.browser.quit()
    stop_local()
