from .loginPage import loginPage
import os


class loginHelper():
    def __init__(self,login_page) -> None:
        self.login_page=login_page

    def full_login(self):

        username=os.environ.get("VALID_USERNAME")
        password=os.environ.get("VALID_PASSWORD")
        self.login_page.verify_login_page_loaded()
        self.login_page.fill_username_input(username)
        self.login_page.fill_password_input(password)
        self.login_page.send_formulary()   
        self.login_page.verify_products_page_loaded()