# 📱 Automatización de Pruebas Mobile  
**Python + Appium + Behave**

---

## 📋 Descripción del Proyecto

Este proyecto de automatización de pruebas está orientado a validar la funcionalidad de una aplicación **Android (SauceLabs)** utilizando pruebas basadas en comportamiento (**BDD**) y el patrón de diseño **Page Object Model (POM)**.

El framework utiliza **Appium** para la automatización mobile y **Behave** para la definición de escenarios en lenguaje **Gherkin**, permitiendo pruebas legibles, mantenibles y alineadas con flujos reales de usuario.

---

## 🛠 Tecnologías Utilizadas

- **Python**
- **Appium**
- **Behave (BDD)**
- **Android Emulator / Dispositivo físico**
- **HTML Reports**

---

## 🚀 ¿Cómo ejecutar las pruebas?

### ✅ Prerrequisitos

- Python 3.8 o superior  
- [Node.js](https://nodejs.org/)
- [Android Studio](https://developer.android.com/studio) (necesario para disponer de **ADB**, requisito clave para la comunicación con dispositivos Android)  
- Emulador Android Studio o dispositivo físico  

---

## ⚙️ Configuración del Entorno

### 📦 Instalación de Appium y controlador

```bash
npm install -g appium
appium driver install uiautomator2
```

## 🧪 Comandos de ejecución de Pruebas

### 1️⃣ Preparar el dispositivo

- Conectar un **dispositivo físico Android (9 o menor)** con la **depuración USB** habilitada desde las opciones de desarrollador,  
  **o**
- Ejecutar un **emulador** desde Android Studio.

Verificar que el dispositivo sea reconocido por ADB: 

```bash
adb devices
```

### 2️⃣ Iniciar Appium Server

En una nueva terminal ejecutar:
```bash
appium
```

### 3️⃣ Ejecutar pruebas

#### ▶️ Ejecución Básica
```bash
behave
```
#### 📊 Ejecución con Reporte HTML
```bash
behave -v --no-capture -f behave_html_formatter:HTMLFormatter -o reports/report.html
```

