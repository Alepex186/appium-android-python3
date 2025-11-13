from appium.webdriver.common.appiumby import AppiumBy
from pages.basePage import basePage
import time
from selenium.webdriver.support.wait import WebDriverWait

class productsPage(basePage):
    def __init__(self, context, timeout=5):
        super().__init__(context, timeout)
        self.context = context


    def get_all_products(self):
        driver = self.context.driver
        all_elements = []
        seen_elements = []

        self.wait=WebDriverWait(driver,5)


        while True:
            # Recolectar productos visibles
            try:
                elements = super().get_visibility_elements('new UiSelector().description("test-Articulo")',AppiumBy.ANDROID_UIAUTOMATOR)
                new_elements = [el for el in elements if el.id not in seen_elements]

                if not new_elements:
                    # No hay más elementos nuevos, final de la lista
                    break
                for el in new_elements:
                    count=0
                    while(True):
                        time.sleep(1)
                        try:
                            all_elements.append({
                                    "name": el.find_element(AppiumBy.ACCESSIBILITY_ID,"test-Titulo de articulo").text,
                                    "price": el.find_element(AppiumBy.ACCESSIBILITY_ID,"test-Precio").text
                            })
                            seen_elements.append(el.id)
                            break
                        except:
                            count +=1 
                            pass
                        if(count == 1):
                            break
            except:
                print("No se encontraron mas productos")
                break
                
            
                    
            # Hacer scroll para cargar más elementos
            super().swipe_up(driver,300)

        return all_elements


    def verify_products(self,products_list):
        for product in products_list:
            el=super().get_clickable_element(f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{product["name"]}"))',AppiumBy.ANDROID_UIAUTOMATOR)
            el.click()

            assert super().get_visibility_element(f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{product["name"]}"))',AppiumBy.ANDROID_UIAUTOMATOR) is not None 
            assert super().get_visibility_element(f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{product["price"]}"))',AppiumBy.ANDROID_UIAUTOMATOR) is not None

            self.context.driver.back()