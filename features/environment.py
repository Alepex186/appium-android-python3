from dotenv import load_dotenv
import os
from appium.options.android import UiAutomator2Options
from appium import webdriver

from pages.loginPage import loginPage
from pages.loginHelper import loginHelper
from pages.productsPage import productsPage

load_dotenv()


APK_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
    )
)



CAPABILITIES = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": APK_PATH,
    "appPackage": "com.swaglabsmobileapp",
    "appActivity": "com.swaglabsmobileapp.MainActivity",
    "automationName": "UiAutomator2",
    "adbExecTimeout": 120000,
    "uiautomator2ServerInstallTimeout": 120000,
    "newCommandTimeout": 300,
    "noReset": False,
    "fullReset": False
}

APPIUM_SERVER_URL = "http://localhost:4723"


def before_all(context):
    options = UiAutomator2Options().load_capabilities(CAPABILITIES)
    context.driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    context.driver.implicitly_wait(10)


def before_scenario(context, scenario):
    context.driver.execute_script("mobile: terminateApp", {"appId": "com.swaglabsmobileapp"})
    context.driver.execute_script("mobile: activateApp", {"appId": "com.swaglabsmobileapp"})
    context.login_page = loginPage(context, 10)
    context.login_helper = loginHelper(context.login_page)
    context.products_page = productsPage(context, 10)


def after_all(context):
    context.driver.quit()