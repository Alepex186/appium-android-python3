Feature: Cerrar sesión
  Como usuario de la aplicación de e-commerce
  Quiero cerrar sesión
  Para mantener segura mi información personal y mis datos de pago


Scenario: Validar cerrar sesión correctamente
    Given El usuario ha iniciado sesión en el sistema
    When El usuario cierra sesión
    Then El usuario debería ser redirigido a la pantalla de inicio de sesión