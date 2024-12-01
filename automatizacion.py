import pandas as pd
import pyautogui as pg
import time
import webbrowser  # Para manejar el navegador

# Validar y corregir el número de teléfono
def validar_numero(numero):
    if pd.isna(numero):  # Verificar si el número es NaN
        return None
    
    numero = str(numero).strip()  # Convertir a string y eliminar espacios
    if len(numero) == 12 and numero.startswith("52"):
        return f"+{numero}"  # Número ya válido con 12 dígitos y prefijo 52
    elif len(numero) == 10 and numero.isdigit():
        return f"+52{numero}"  # Agregar prefijo 52 si tiene 10 dígitos
    else:
        return None  # Número inválido

# Cargar el archivo Excel
def cargar_datos(ruta_archivo):
    try:
        datos = pd.read_excel(ruta_archivo)
        return datos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

# Enviar mensajes usando una sola pestaña de WhatsApp Web
def enviar_mensajes(datos):
    print("Abriendo WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(14)  # Tiempo para que cargue WhatsApp Web (ajusta según tu conexión)

    for index, fila in datos.iterrows():
        nombre = fila['Nombre']
        numero = validar_numero(fila['Número'])  # Validar y corregir el número
        if not numero:
            print(f"Número inválido para {nombre or 'Sin nombre'}. Debe tener 10 o 12 dígitos y comenzar con '52' si tiene 12.")
            continue  # Saltar este contacto si el número es inválido

        mensaje = f"Hola {nombre}, este es un mensaje automatizado. ¡Saludos!"
        
        try:
            # Usar JavaScript para cambiar al contacto y mensaje dentro de la misma pestaña
            url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje}"
            pg.hotkey('ctrl', 'l')  # Seleccionar la barra de direcciones
            pg.typewrite(url)  # Escribir la URL
            pg.press('enter')  # Ir a la URL

            print(f"Enviando mensaje a {nombre} ({numero})")
            time.sleep(10)  # Esperar a que cargue el chat en WhatsApp Web
            pg.press('enter')  # Simular la tecla "Enter" para enviar el mensaje
            
            time.sleep(5)  # Pausa entre mensajes para evitar bloqueos
        except Exception as e:
            print(f"Error al enviar mensaje a {nombre} ({numero}): {e}")

if __name__ == "__main__":
    ruta = "destinatarios.xlsx"
    datos = cargar_datos(ruta)
    if datos is not None:
        print("Mantén la ventana de WhatsApp abierta durante todo el proceso.")
        enviar_mensajes(datos)
    else:
        print("No se pudo cargar el archivo de destinatarios.")
