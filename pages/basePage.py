from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
import time

class Waits:
    def __init__(self,driver,timeout):
        self.wait=WebDriverWait(driver,timeout)

    def wait_for_clickable(self,element):
        return self.wait.until(EC.element_to_be_clickable(element))

    def wait_for_visibility(self,element):
        return self.wait.until((EC.visibility_of_element_located(element)))

    def wait_for_visibility_of_all_elements(self,element):
        return self.wait.until((EC.visibility_of_all_elements_located(element)))



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

    def get_visibility_element(self,element_id,selector,timeout=10):
        return self.waits.wait_for_visibility((selector,element_id))

    def get_visibility_elements(self,element_id,selector):
        return self.waits.wait_for_visibility_of_all_elements((selector,element_id))


    def swipe_up(self, driver, duration=500):
        driver = self.context.driver
        size = driver.get_window_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        start_y = int(height * 0.8)  # 80% de la pantalla
        end_x = width // 2
        end_y = int(height * 0.2)    # 20% de la pantalla

        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionBuilder(driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()

        time.sleep(duration / 1000)