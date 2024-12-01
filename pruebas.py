from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configuración del driver de Chrome usando webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL de WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Esperar a que WhatsApp Web cargue y escanear el código QR
print("Escanea el código QR en tu teléfono...")
time.sleep(15)  # Tiempo para escanear el QR

# Lista de contactos (nombre y número de teléfono en formato internacional)
contacts = [
    {'name': 'Contacto 1', 'phone': '+524492779268'},
]

# Ruta de la imagen que deseas enviar
image_path = r'C:\Users\hiram\OneDrive\Documents\BARATA\istockphoto-689364180-612x612.jpg'  # Ruta local de la imagen

# Mensaje de texto
text_message = "¡Hola! Este es un mensaje con texto y una imagen."

def send_message(contact, text_message, image_path):
    # Buscar el contacto por nombre
    search_box = driver.find_element(By.XPATH, '//div[@title="Buscar o empezar un chat"]')
    search_box.click()
    search_box.send_keys(contact['name'])
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    # Enviar mensaje de texto
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(text_message)
    message_box.send_keys(Keys.RETURN)

    time.sleep(1)

    # Enviar la imagen directamente en el cuadro de entrada de texto
    message_box.send_keys(image_path)  # Ruta completa de la imagen
    message_box.send_keys(Keys.RETURN)
    time.sleep(2)

    print(f'Mensaje enviado a {contact["name"]}')

# Enviar mensaje a cada contacto
for contact in contacts:
    send_message(contact, text_message, image_path)

# Cerrar el navegador
driver.quit()
