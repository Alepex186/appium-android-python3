
from appium.webdriver.common.appiumby import AppiumBy
from pages.basePage import basePage
import time
class loginPage(basePage):
    def __init__(self,context,timeout):
        super().__init__(context, timeout)


    def verify_login_page_loaded(self):
        super().verify_text_in_element("Usuario","test-Usuario",AppiumBy.ACCESSIBILITY_ID)
        super().verify_text_in_element("Contraseña","test-Contraseña",AppiumBy.ACCESSIBILITY_ID)

    def verify_products_page_loaded(self):
        element = super().get_visibility_element('new UiSelector().text("PRODUCTOS")',AppiumBy.ANDROID_UIAUTOMATOR)
        assert element is not None, "No se encontro el elemento " + f'new UiSelector().text("PRODUCTOS")'


    def fill_username_input(self,text):
        super().fill_input(text,"test-Usuario",AppiumBy.ACCESSIBILITY_ID)

    def fill_password_input(self,text):
        super().fill_input(text,"test-Contraseña",AppiumBy.ACCESSIBILITY_ID)
        
    def send_formulary(self):
        super().get_clickable_element("test-LOGIN",AppiumBy.ACCESSIBILITY_ID).click()

    def verify_error_message(self,error_message):
        element = super().get_visibility_element(f'new UiSelector().text("{error_message}")',AppiumBy.ANDROID_UIAUTOMATOR)
        assert element is not None, "No se encontro el elemento " + f'new UiSelector().text("{error_message}")'

