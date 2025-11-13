from behave import *

from pages.loginHelper import loginHelper
from pages.productsPage import productsPage

@Given("El usuario está en la página de productos")
def step_impl(context):
    login_helper:loginHelper=context.login_helper
    login_helper.full_login()


@When("El usuario selecciona cada producto en la lista")
def step_impl(context):
    products_page:productsPage=context.products_page

    productos=products_page.get_all_products()
    context.productos_list=productos

@Then("Cada producto debería mostrar correctamente el nombre y precio")
def step_impl(context):
    products_page:productsPage=context.products_page

    products_page.verify_products(context.productos_list)