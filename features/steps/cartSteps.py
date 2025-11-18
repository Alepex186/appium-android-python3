from behave import Given, When, Then
from pages.cartPage import cartPage


@When("El usuario navega al carrito de compras")
def step_impl(context):
    cart_page:cartPage=context.cart_page
    cart_page.open_cart()


@Then("Debería visualizar un producto en el carrito")
def step_impl(context):
    cart_page:cartPage=context.cart_page
    cart_page.verify_added_product()


@When("El usuario elimina el producto del carrito")
def step_impl(context):
    cart_page:cartPage=context.cart_page
    cart_page.remove_first_product()

@Then("El carrito debería estar vacío")
def step_impl(context):
    cart_page:cartPage=context.cart_page
    cart_page.verify_removed_product()







