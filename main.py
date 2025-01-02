from machine import Pin, I2C, ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime

# Configuración de los pines de los botones 
button_1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button_2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button_3 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
button_4 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)

# Configurar pines de LEDs
led_rojo = Pin(18, Pin.OUT)
led_amarillo = Pin(17, Pin.OUT)
led_verde = Pin(16, Pin.OUT)

# Configuración del pin de datos del sensor DHT11
dht_pin_1 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
sensor_1 = dht.DHT11(dht_pin_1)


# Configurar la dirección I2C del LCD y el objeto I2C
DEFAULT_I2C_ADDR = 0x27
I2C_ADDR = DEFAULT_I2C_ADDR
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
# Configuración del pin del potenciómetro 
pot_pin = ADC(27)  

flag = False
flag2 = False
data_to_save = []
data_to_save_2 = []

def guardar_datos(pin):
    global data_to_save
    if not pin.value() == 1:
        sensor_1.measure()
        temperatura_1 = sensor_1.temperature()
        pot_value = pot_pin.read_u16()
        angulo = (pot_value / 65535) * 376 - 5
        data_to_save.append((temperatura_1, angulo))
        lcd.clear()
        lcd.putstr(" DATO 1\n")
        lcd.putstr("GUARDADOS")
        utime.sleep(2)
        
# Configura la interrupción para que llame a la función cuando se presiona el botón       
button_1.irq(trigger=machine.Pin.IRQ_RISING, handler=guardar_datos)
    
def mostrar_datos(pin):
    global flag
    if not pin.value() == 1:
        flag=True
# Configura la interrupción para que llame a la función cuando se presiona el botón
button_2.irq(trigger=machine.Pin.IRQ_RISING, handler=mostrar_datos)

def guardar_datos_2(pin):
    global data_to_save_2
    if not pin.value() == 1:
        sensor_1.measure()
        temperatura_2 = sensor_1.temperature()
        pot_value = pot_pin.read_u16()
        angulo = (pot_value / 65535) * 376 - 5
        data_to_save_2.append((temperatura_2,angulo))
        lcd.clear()
        lcd.putstr(" DATO 2\n")
        lcd.putstr("GUARDADOS")
        utime.sleep(2)
        
# Configura la interrupción para que llame a la función cuando se presiona el botón       
button_3.irq(trigger=machine.Pin.IRQ_RISING, handler=guardar_datos_2)

def mostrar_datos_2(pin):
    global flag2
    if not pin.value() == 1:
        flag2=True
# Configura la interrupción para que llame a la función cuando se presiona el botón
button_4.irq(trigger=machine.Pin.IRQ_RISING, handler=mostrar_datos_2)

while True:
    try:
    
        if flag2 or flag == False:
            # Leer el valor del potenciómetro
            pot_value = pot_pin.read_u16()
            angulo = (pot_value / 65535) * 376 - 5
            ang = int(angulo)
            # Obtener temperatura en Celsius
            sensor_1.measure()
            temperatura_1 = sensor_1.temperature()
            temperatura_2 = sensor_1.temperature()
            
            # Determinar color del LED según la temperatura medida
            if temperatura_1 >= 50 and temperatura_2 >= 50 and ang >= 345:
                lcd.clear()
                lcd.putstr("------PARE------\n")
                lcd.putstr("------PARE------\n")
                led_verde.value(0)
                led_amarillo.value(0)
                led_rojo.value(0)
                utime.sleep(2)
                break # Salir del bucle después de mostrar "PARE"
            elif temperatura_1 < 32:
                led_verde.value(1)
                led_amarillo.value(0)
                led_rojo.value(0)
            elif 32 <= temperatura_1 <= 45:
                led_verde.value(0)
                led_amarillo.value(1)
                led_rojo.value(0)
            else:
                led_verde.value(0)
                led_amarillo.value(0)
                led_rojo.value(1)
            
            # Mostrar temperatura y ángulo del servo en LCD
            lcd.clear()
            lcd.putstr("T1:{:.0f} ".format(temperatura_1))
            lcd.putstr("t2:{:.0f} \n".format(temperatura_2))
            lcd.putstr("Ang:{:.0f} ".format(angulo))  # Convertir ciclo de trabajo a grados y redondear
            utime.sleep(0.1)
            
        if flag == True:
            lcd.clear()
            lcd.putstr("Mostrar dato 1\n")
            utime.sleep(3)
            if data_to_save:
                latest_data = data_to_save[-1]  # Obtiene el último conjunto de datos guardados
                lcd.clear()
                temperatura_1, angulo = latest_data
                lcd.putstr("T1:{:.0f}\n".format(temperatura_1))
                lcd.putstr("Ang:{:.0f}".format(angulo))
                utime.sleep(5)
            else:
                lcd.clear()
                lcd.putstr("No hay datos")
                utime.sleep(3)
            flag = False
            
        if flag2 == True:
            lcd.clear()
            lcd.putstr("Mostrar dato 2\n")
            utime.sleep(3)
            if data_to_save_2:
                latest_data_2 = data_to_save_2[-1]  # Obtiene el último conjunto de datos guardados
                lcd.clear()
                temperatura_2, angulo = latest_data_2
                lcd.putstr("t2:{:.0f}\n".format(temperatura_2))
                lcd.putstr("Ang:{:.0f}".format(angulo))
                utime.sleep(5)
            else:
                lcd.clear()
                lcd.putstr("No hay datos")
                utime.sleep(3)
            flag2 = False
            
    except Exception:
        pass