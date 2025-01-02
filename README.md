# Control de LEDs y Visualización en LCD con Raspberry Pi Pico

Este código permite controlar LEDs y mostrar información en una pantalla LCD mediante botones y sensores conectados a una Raspberry Pi Pico. Además, incluye almacenamiento de datos de temperatura y ángulo leídos desde un potenciómetro.

---

## **Requisitos**

- Raspberry Pi Pico con microcontrolador RP2040.
- Sensor DHT11 para medir la temperatura.
- Potenciómetro conectado para medir ángulos.
- Módulo LCD I2C de 16x2 para visualización.
- LEDs conectados a los pines GPIO (rojo, amarillo y verde).
- Botones conectados para guardar y mostrar datos.

---

## **Instalación**

1. Asegúrate de tener MicroPython instalado en la Raspberry Pi Pico.
2. Instala las librerías necesarias en Thonny o tu entorno preferido:
    - `lcd_api.py` y `pico_i2c_lcd.py`.
3. Descarga y guarda el archivo con este código en formato `.py`.
4. Conecta todos los componentes según la configuración especificada.
5. Sube el archivo al microcontrolador y ejecútalo.

---

## **Uso**

### **Funciones Principales:**

- **Guardar Datos:**
  - Botón 1: Guarda la temperatura y el ángulo actuales en el conjunto de datos 1.
  - Botón 3: Guarda la temperatura y el ángulo actuales en el conjunto de datos 2.

- **Mostrar Datos:**
  - Botón 2: Muestra el último dato guardado en el conjunto 1.
  - Botón 4: Muestra el último dato guardado en el conjunto 2.

- **Visualización en LCD:**
  - Muestra temperatura y ángulo en tiempo real.
  - Cambia el color del LED según la temperatura:
    - Verde: Temperatura < 32°C.
    - Amarillo: Temperatura entre 32°C y 45°C.
    - Rojo: Temperatura > 45°C.

- **Alerta de PARE:**
  - Si ambas temperaturas son mayores o iguales a 50°C y el ángulo supera los 345°, muestra "PARE" en la pantalla y apaga los LEDs.

---

## **Notas**

- **Interrupciones:** Se utilizan interrupciones para responder de inmediato cuando se presiona un botón.
- **Lectura del Potenciómetro:** El valor analógico se escala para representar ángulos en grados.
- **Seguridad:** El sistema detecta condiciones críticas y muestra advertencias.
- **Datos Guardados:** Los datos almacenados pueden ser visualizados en cualquier momento pulsando los botones correspondientes.

---

## **Ejemplo de Configuración de Pines**

- **Botones:**
  - Botón 1: GPIO 14
  - Botón 2: GPIO 15
  - Botón 3: GPIO 11
  - Botón 4: GPIO 10

- **LEDs:**
  - Rojo: GPIO 18
  - Amarillo: GPIO 17
  - Verde: GPIO 16

- **LCD I2C:**
  - SDA: GPIO 12
  - SCL: GPIO 13

- **Sensor DHT11:**
  - Datos: GPIO 26

- **Potenciómetro:**
  - Entrada analógica: GPIO 27

## **Consideraciones Finales**

Este proyecto es ideal para aplicaciones de monitoreo y control en tiempo real. Permite capturar datos críticos y proporcionar alertas visuales inmediatas. Su estructura modular facilita la personalización y expansibilidad según las necesidades del usuario.

