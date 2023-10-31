# Proyecto de página web para empresa propia

## Pasos para desplegar el proyecto:

1. Clonar el repositorio

2. Crear un entorno virtual:
   - Para Windows:
     ```
     python -m venv env
     ```
   - Para Linux:
     ```
     python3 -m venv env
     ```

3. Activar el entorno virtual:
   - Para Windows:
     ```
     env\Scripts\activate
     ```
   - Para Linux:
     ```
     source env/bin/activate
     ```

4. Instalar dependencias:
    - pip install > requirements.txt

5. Crear un archivo .env con las variables para el servidor SMTP y un Secret Key:
    - SECRET_KEY        
    - MAIL_SERVER      #Reemplazar por el Servidor SMTP
    - MAIL_PORT        #Puerto SMTP
    - MAIL_USERNAME    #Dirección de correo electrónico de Salida
    - MAIL_PASSWORD    #Contraseña de correo electrónico 


5. Iniciar la aplicación:
    - Para Windows:
    ```
    python app.py
    ```
    - Para Linux:
    ```
    python3 app.py
    ```

