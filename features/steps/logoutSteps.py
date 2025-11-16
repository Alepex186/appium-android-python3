from behave import *

from pages.logoutPage import logoutPage
from pages.loginHelper import loginHelper
from pages.loginPage import loginPage

@Given("El usuario ha iniciado sesión en el sistema")
def step_impl(context):
    login_helper:loginHelper=context.login_helper
    login_helper.full_login()

@When("El usuario cierra sesión")
def step_impl(context):
    logout_page:logoutPage=context.logout_page
    logout_page.logout()

@Then("El usuario debería ser redirigido a la pantalla de inicio de sesión")
def step_impl(context):
    login_page:loginPage=context.login_page
    login_page.verify_login_page_loaded()