from behave import Given, When, Then
from appium import webdriver
import time
from pages.loginPage import loginPage


@Given("El usuario está en la pantalla de inicio de sesión")
def step_impl(context):
    login_page:loginPage=context.login_page
    login_page.verify_login_page_loaded()


@When("El usuario ingresa un nombre de usuario {usuario}")
def step_impl(context,usuario):
    login_page:loginPage=context.login_page
    login_page.fill_username_input(usuario)

@When("El usuario ingresa una contraseña {contrasenia}")
def step_impl(context,contrasenia):
    login_page:loginPage=context.login_page
    login_page.fill_password_input(contrasenia)

@When("El usuario envia el formulario de inicio de sesión")
def step_impl(context):
    login_page:loginPage=context.login_page
    login_page.send_formulary()

@Then("El usuario deberia visualizar la pantalla principal de la aplicación")
def step_impl(context):
    login_page:loginPage=context.login_page
    login_page.verify_products_page_loaded()

@Then("El usuario deberia visualizar el mensaje {mensaje_error}")
def step_impl(context,mensaje_error):
    login_page:loginPage=context.login_page
    login_page.verify_error_message(mensaje_error)