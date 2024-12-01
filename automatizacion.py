import pandas as pd
import pywhatkit as kit
import time

# Cargar el archivo Excel
def cargar_datos(ruta_archivo):
    try:
        datos = pd.read_excel(ruta_archivo)
        return datos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

# Enviar mensajes a través de WhatsApp
def enviar_mensajes(datos):
    for index, fila in datos.iterrows():
        nombre = fila['Nombre']
        numero = fila['Número']
        mensaje = f"Hola {nombre}, este es un mensaje automatizado. ¡Saludos!"
        
        try:
            # Programar el envío (se abre en WhatsApp Web)
            kit.sendwhatmsg_instantly(
                phone_no=str(numero), 
                message=mensaje, 
                wait_time=10,  # Espera 10 segundos para procesar
                tab_close=True  # Cierra la pestaña de WhatsApp Web automáticamente
            )
            print(f"Mensaje enviado a {nombre} ({numero})")
            time.sleep(5)  # Pausa entre mensajes para evitar bloqueos
        except Exception as e:
            print(f"Error al enviar mensaje a {nombre} ({numero}): {e}")

if __name__ == "__main__":
    ruta = "destinatarios.xlsx"
    datos = cargar_datos(ruta)
    if datos is not None:
        enviar_mensajes(datos)
    else:
        print("No se pudo cargar el archivo de destinatarios.")
