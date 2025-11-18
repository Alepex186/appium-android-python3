from appium.webdriver.common.appiumby import AppiumBy
from pages.basePage import basePage


class cartPage(basePage):
    def __init__(self,context,timeout):
        super().__init__(context, timeout)


    def open_cart(self):
        cart_button=super().get_clickable_element('test-Carrito',AppiumBy.ACCESSIBILITY_ID)
        cart_button.click()
    
    def verify_added_product(self):
        try:
            super().get_visibility_element('new UiSelector().description("test-Item")',AppiumBy.ANDROID_UIAUTOMATOR,3)
            return True
        except Exception:
            raise AssertionError("No se agregó el elemento")


    def remove_first_product(self):
        product = super().get_visibility_element('new UiSelector().description("test-Item")',AppiumBy.ANDROID_UIAUTOMATOR,5)

        remove_button = product.find_element(AppiumBy.ACCESSIBILITY_ID, "test-REMOVER")
        remove_button.click()


    def verify_removed_product(self):
        try:
            super().get_visibility_element('new UiSelector().description("test-Item")',AppiumBy.ANDROID_UIAUTOMATOR,3)
            raise AssertionError("No se elimino el elemento")
        except Exception:
            return True
