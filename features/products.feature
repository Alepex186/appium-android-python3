Feature: Ver detalles de un producto
  Como usuario de la aplicación
  Quiero poder ver la información completa del producto al seleccionarlo
  Para tomar decisiones informadas sobre la compra

Scenario: Validar información de todos los productos
  Given El usuario está en la página de productos
  When El usuario selecciona cada producto en la lista
  Then Cada producto debería mostrar correctamente el nombre y precio

