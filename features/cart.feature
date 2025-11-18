@wip
Feature: Carro de compra
  Como usuario de la aplicación de e-commerce
  Quiero administrar el carro de compras
  Para manejar el carrito de forma correcta

Scenario: Agregar un producto al carrito
    Given El usuario está en la página de productos
    When El usuario agrega un producto al carrito
    And El usuario navega al carrito de compras
    Then Debería visualizar un producto en el carrito

Scenario: Eliminar un producto del carrito
    Given El usuario está en la página de productos
    When El usuario agrega un producto al carrito
    And El usuario navega al carrito de compras
    And El usuario elimina el producto del carrito
    Then El carrito debería estar vacío

