from ftplib import FTP
import os


def save(con: FTP, file):
    with open(f'C:/Codes/py/TXT/{file}.txt', 'wb') as fp:
        con.retrbinary(f'RETR {file}', fp.write)


def comparacion(con:FTP, cosa, verif):
    if verif == 0:
        try:
            con.cwd(file)
        except :
            print(f'{file} no es un directorio')
    else:
        verif = 0
        con.nlst()
        if cosa.endswith('.txt') == True:
            print("Es un txt")
            save(con, cosa)
            verif = 1
        elif cosa.endswith('.msg') == True:
            print("Es un .msg")
            save(con, cosa)
            verif = 1
        elif cosa.startswith('README') == True:
            print("Es un README")
            save(con, cosa)
            verif = 1
    return verif


verif = 0

os.mkdir('TXT')
# conexion a servidor FTP
sesion = FTP('ftp.us.debian.org')
sesion.login()
sesion.cwd('debian')

contenido = sesion.nlst()
for file in contenido:
    comparacion(sesion, file, verif)
