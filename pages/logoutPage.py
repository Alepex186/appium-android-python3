from appium.webdriver.common.appiumby import AppiumBy
from pages.basePage import basePage


class logoutPage(basePage):
    def __init__(self,context,timeout):
        super().__init__(context, timeout)


    def logout(self):
        super().open_burger_menu()
        logout_button=super().get_clickable_element('new UiSelector().text("CERRAR SESION")',AppiumBy.ANDROID_UIAUTOMATOR)
        logout_button.click()