#!/usr/bin/env python3
# envia correos por smtp con los argumentos que le des en bash,
# en el argumento 1 va el asunto y en el 2 el mensaje

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

data = {}
emails = {}

with open('pass.json') as f:
    data = json.load(f)

with open('lista_de_correos.json') as f:
    emails = json.load(f)

# se repite 5 veces porque en la lista hay 5 correos
for i in range(1,5):
    string_i = str(i)
    print("Enviando a: ", emails['e'+string_i])
    print("El asunto es: ", sys.argv[1])
    print("El cuerpo del correo es: ", sys.argv[2])
    msg = MIMEMultipart()
    message = sys.argv[2]

    msg['From'] = data['user']
    msg['To'] = emails['e'+string_i]
    msg['Subject'] = sys.argv[2]

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.office365.com:587')
    server.starttls()

    print(data['user'])
    server.login(data['user'], data['pass'])

    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("\n")
    server.quit()
