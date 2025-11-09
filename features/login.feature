Feature: Iniciar sesión en la aplicación
  Como usuario de la aplicación
  Quiero poder iniciar sesión con mis credenciales válidas
  Y recibir mensajes de error apropiados cuando las credenciales sean inválidas
  Para acceder a la pantalla principal o entender por qué no puedo acceder

  Scenario Outline: Iniciar sesión con credenciales válidas
    Given El usuario está en la pantalla de inicio de sesión
    When El usuario ingresa un nombre de usuario <usuario>
    And El usuario ingresa una contraseña <contrasenia>
    And El usuario envia el formulario de inicio de sesión
    Then El usuario deberia visualizar la pantalla principal de la aplicación

    Examples:
      | usuario        | contrasenia   |
      | standard_user  | secret_sauce  |


  Scenario Outline: Iniciar sesión con credenciales bloqueadas
    Given El usuario está en la pantalla de inicio de sesión
    When El usuario ingresa un nombre de usuario <usuario>
    And El usuario ingresa una contraseña <contrasenia>
    And El usuario envia el formulario de inicio de sesión
    Then El usuario deberia visualizar el mensaje <mensaje_error>


    Examples:
      | usuario          | contrasenia   |mensaje_error|
      | locked_out_user  | secret_sauce  |Lo sentimos, este usuario ha sido bloqueado.|


  Scenario Outline: Iniciar sesión con usuario invalido
    Given El usuario está en la pantalla de inicio de sesión
    When El usuario ingresa un nombre de usuario <usuario_invalido>
    And El usuario ingresa una contraseña <contrasenia>
    And El usuario envia el formulario de inicio de sesión
    Then El usuario deberia visualizar el mensaje <mensaje_error>

    Examples:
      | usuario_invalido| contrasenia     |mensaje_error|
      | invalid_user    | secret_sauce    |El usuario y contraseña no coinciden con ningun usuario en este servicio.|


  Scenario Outline: Iniciar sesión con contraseña invalida
    Given El usuario está en la pantalla de inicio de sesión
    When El usuario ingresa un nombre de usuario <usuario>
    And El usuario ingresa una contraseña <contrasenia_invalida>
    And El usuario envia el formulario de inicio de sesión
    Then El usuario deberia visualizar el mensaje <mensaje_error>

    Examples:
      | usuario       | contrasenia_invalida |mensaje_error|
      | standard_user | invalid_password     |El usuario y contraseña no coinciden con ningun usuario en este servicio.|