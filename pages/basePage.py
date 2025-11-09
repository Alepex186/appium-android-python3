from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class Waits:
    def __init__(self,driver,timeout):
        self.wait=WebDriverWait(driver,timeout)

    def wait_for_clickable(self,element):
        return self.wait.until(EC.element_to_be_clickable(element))

    def wait_for_visibility(self,element):
        return self.wait.until((EC.visibility_of_element_located(element)))





class basePage:
    def __init__(self,context,timeout=10):
        self.waits=Waits(context.driver,timeout)


    def verify_text_in_element(self,text,element_id,selector):
        assert text in self.waits.wait_for_visibility((selector,element_id)).text
        

    def fill_input(self,text,element_id,selector):
        input=self.waits.wait_for_visibility((selector,element_id))
        input.clear()
        input.send_keys(text)


    def get_clickable_element(self,element_id,selector):
        return self.waits.wait_for_clickable((selector,element_id))


    def get_visibility_element(self,element_id,selector):
        return self.waits.wait_for_visibility((selector,element_id))
