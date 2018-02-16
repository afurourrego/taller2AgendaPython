# -*- coding:utf-8 -*-

"""
    GRUPO:5
    DAVID YEPES HERIBERTO
    NIETO GIL JOHN SEBASTIAN
    URREGO SALAZAR CRISTHIAN
"""


import sqlite3
import time
import os
import hashlib
import csv

def conecta():
    """Realiza la conexión a la base de datos agenda.db"""
    con = sqlite3.connect("agenda.db")
    return con

def conexion():

    con = conecta()
    cursor = con.cursor()
    # Comprueba si la tabla existe, en caso de no existir la crea
    #cursor.execute("""DROP TABLE datos""")
    #cursor.execute("""DROP TABLE pass_user""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS datos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, telefono TEXT, correo TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS pass_user (contrasena INTEGER, contrasena_encryptada TEXT)""")
    cursor.close()


def run():
    conexion()
    print("[BIENVENIDO A SU AGENDA]")

    if comprobar_si_contrasena() != 1:
        menu_contrasena()

    menu_inicio()


def encryptar_contrasena(cadena):
    encriptada = hashlib.sha1()
    encriptada.update(cadena.encode('utf-8'))
    return encriptada.hexdigest()


def comprobar_si_contrasena():
    con = conecta()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pass_user ")
    contrasena = cursor.fetchall()
    for contrasena_bolean in contrasena:
        contrasena = contrasena_bolean[0]
    cursor.close()
    return contrasena


def recuperar_contrasena_encryptada():
    con = conecta()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pass_user ")
    contrasena = cursor.fetchall()
    for contrasena_encryptada in contrasena:
        contrasena = contrasena_encryptada[1]
    cursor.close()
    return contrasena



def menu_contrasena():
    print("...")
    contrasena1 = input("Ingrese su nueva contraseña: ")
    contrasena2 = input("Repita su contraseña: ")

    if contrasena1 == contrasena2:

        con = conecta()
        cursor = con.cursor()

        contrasena = 1
        contrasena_encryptada = encryptar_contrasena(contrasena1)

        cursor.execute("insert into pass_user(contrasena, contrasena_encryptada) values ('%s','%s')"% (contrasena, contrasena_encryptada))

        con.commit()
        cursor.close()
        
    else:
        print("Error:[Las contraseñas deben ser iguales]")
        menu_contrasena()


def menu_inicio():
    opcionwhile = False

    while opcionwhile == False:
        os.system("clear")
        print("")
        print("-------------")
        print("[MENÚ AGENDA]")
        print("-------------")
        print("")
        print("[1] Ver Contactos")
        print("[2] Añadir.")
        print("[3] Editar.")
        print("[4] Eliminar.")
        print("[5] Buscar.")
        print("[6] Opciones.")
        print("[0] Salir.")
        print("")

        opcion = input("Eliga una Opción: ")

        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "0":
            print("")
            print("")
            print("[Opcion Incorrecta]")
            print("")
            time.sleep(2)

        elif opcion == "1":
            imprimir_encabezado("LISTA DE CONTACTOS")
            ver_contactos_opcion1()
            print("")
            input("Presione una tecla para continuar...")
        elif opcion == "2":
            anadir_contactos_opcion2()
        elif opcion == "3":
            editar_contactos_opcion3()
        elif opcion == "4":
            eliminar_contactos_opcion4()
        elif opcion == "5":
            buscar_contactos_opcion5()
            print("")
            input("Presione una tecla para continuar...")
        elif opcion == "6":
            opciones_opcion6()
        elif opcion == "0":
            salir_opcion0()

def isContact(identificador):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM datos WHERE id = {identificador}")
    cant = cursor.fetchall()
    cursor.close()
    return len(cant)


def obtener_contactos():
    """Obtener todos los contactos de la tabla"""
    con = conecta()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def ver_contactos_opcion1():
    """Muestra todos los contactos de la agenda"""
    resultado = obtener_contactos()
    for i in resultado:
        print("%s   %s   %s   %s   %s" % (i[0], i[1], i[2], i[3], i[4]))


def anadir_contactos_opcion2():
    """Agrega un nuevo contacto a la Agenda"""
    imprimir_encabezado("AGREGAR CONTACTO")

    con = conecta()
    cursor = con.cursor()

    nombre = input("Nombre: ")
    apellido = input("Apellidos: ")
    telefono = input("Telefono: ")
    correo = input("Email: ")

    cursor.execute("insert into datos (nombre, apellido, telefono, correo) values ('%s','%s','%s','%s')" % (
        nombre, apellido, telefono, correo))

    con.commit()
    cursor.close()

    print("")
    print("Los datos fueron agregados correctamente")


def editar_contactos_opcion3():
    imprimir_encabezado("EDITAR CONTACTOS")

    ver_contactos_opcion1()
    print("\n")
    identificador = input("Ingrese el id del contacto a editar: ")
    buscar = isContact(identificador)

    if buscar > 0:
        print("\n")
        contrasena = input("Ingrese su contraseña para editar: ")
        if encryptar_contrasena(contrasena) == recuperar_contrasena_encryptada():
            print("")
            print("")
            while True:
                print("")
                print("Campos a editar")
                print("")
                print("--------------------")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Telefono")
                print("4. Correo")
                print("0. Finaliza")
                print("--------------------")
                print("")
                opcion = input("Ingrese la opcion a editar: ")

                con = conecta()
                cursor = con.cursor()

                if opcion == '0':
                    break
                elif opcion == '1':
                    nuevoNombre = input("Ingrese el nuevo nombre: ")
                    cursor.execute("UPDATE datos SET nombre = '%s' WHERE id='%s'" % (nuevoNombre, identificador))
                elif opcion == '2':
                    apellido = input("Ingrese el nuevo apellido: ")
                    cursor.execute("UPDATE datos SET apellido = '%s' WHERE id='%s'" % (apellido, identificador))
                elif opcion == '3':
                    telefono = input("Ingrese el nuevo telefono: ")
                    cursor.execute("UPDATE datos SET telefono = '%s' WHERE id='%s'" % (telefono, identificador))
                elif opcion == '4':
                    correo = input("Ingrese el nuevo correo: ")
                    cursor.execute("UPDATE datos SET correo = '%s' WHERE id='%s'" % (correo, identificador))
                else:
                    print("\n")
                    print("Opción Incorrecta")
                con.commit()

            cursor.close()

            print("")
            print("Los datos fueron agregados correctamente")
        else:
            print("[ERROR DE CONTRASEÑA]")
    else:
        print("\n")
        print("El contacto no existe")

    print("")
    input("Presione una tecla para continuar...")


def eliminar_contactos_opcion4():
    """Elimina un contacto de la Agenda"""
    imprimir_encabezado("ELIMINAR CONTACTOS")

    ver_contactos_opcion1()

    identificador = input("Ingrese el id del contacto a eliminar: ")
    print("")
    print("")

    #recupera los nombres y apellidos de la base de datos y los compara, si hay exactitud continua de lo contrario no
    buscar = isContact(identificador)
    print("\n")

    #si existe el contacto a eliminar solicita la contraseña para eliminar
    if buscar > 0:
        contrasena = input("Ingrese su contraseña para eliminar: ")
        if encryptar_contrasena(contrasena) == recuperar_contrasena_encryptada():

            cursor.execute("DELETE FROM datos WHERE id='%s'" % (identificador))
            con.commit()
            cursor.close()

            print("Contacto eliminado correctamente...")
        else:
            print("[ERROR DE CONTRASEÑA]")
    else:
        print("[ERROR: NO SE HA ENCONTRADO CONTACTO]")

    input("Presione una tecla para continuar...")


def buscar_contactos_opcion5():
    """Busca un contacto en la agenda y lo lista"""
    imprimir_encabezado("BUSCAR CONTACTO")

    con = conecta()
    cursor = con.cursor()

    buscar = input("Buscar: ")

    cursor.execute("SELECT * FROM datos WHERE nombre LIKE ? OR apellido LIKE ? OR telefono LIKE ? OR correo LIKE ?", 
        ('%'+buscar+'%','%'+buscar+'%','%'+buscar+'%','%'+buscar+'%',))

    x = cursor.fetchall()

    print("")

    if len(x) > 0:
        for i in x:
            print("%s   %s   %s   %s   %s" % (i[0], i[1], i[2], i[3], i[4]))
    else:
        print("No se encontró ningún contacto")

    cursor.close()


def opciones_opcion6():
    opcionwhile = False

    while opcionwhile == False:
        opcionwhile = True
        imprimir_encabezado("MENU OPCIONES")
        print("[1] Exportar Contactos.")
        print("[2] Importar Contactos.")
        print("[0] Atras.")

        opcion = input("Eliga una Opción: ")

        if opcion != "1" and opcion != "2" and opcion != "0":
            print("")
            print("")
            print("[Opcion Incorrecta]")
            print("")

        elif opcion == "1":
            resultado = obtener_contactos()
            headers = ('id', 'nombre', 'apellido', 'telefono', 'correo')
            with open('export.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(resultado)
            # archivo = open("G:\\hello.txt", "w")
            # for i in resultado:
            #     archivo.write(str(i))
            # archivo.close() 

        elif opcion == "2":
            con = conecta()
            cursor = con.cursor()
            with open('export.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cursor.execute("insert into datos values ( NULL, '%s','%s','%s','%s')" % (
                    row['nombre'], row['apellido'], row['telefono'], row['correo']))
            con.commit()
            cursor.close()
        elif opcion == "0":
            break
            

    menu_inicio()


def salir_opcion0():
    print("")
    print("Saliendo de Agenda...")
    print("")
    print("")
    time.sleep(2)
    exit()

def imprimir_encabezado(titulo):
    print("")
    print("--------------------")
    print("[%s]" % (titulo))
    print("--------------------")
    print("")


if __name__ == '__main__':
    run()
