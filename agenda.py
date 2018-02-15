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

# Conexion con Base de Datos Sqlite3
con = sqlite3.connect("agenda.db")
cursor = con.cursor()
# Comprueba si la tabla existe, en caso de no existir la crea
cursor.execute("""CREATE TABLE IF NOT EXISTS datos (nombre TEXT, apellido TEXT, telefono TEXT, correo TEXT)""")
cursor.close()

con = sqlite3.connect("pass.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS pass_user (contrasena INTEGER, contrasena_encryptada TEXT)""")
cursor.close()


def run():
    print("[BIENVENIDO A SU AGENDA]")

    if comprobar_si_contrasena() != 1:
        menu_contrasena()

    menu_inicio()


def encryptar_contrasena(cadena):
    encriptada = hashlib.sha1()
    encriptada.update(cadena.encode('utf-8'))
    return encriptada.hexdigest()


def comprobar_si_contrasena():

    con = sqlite3.connect("pass.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM pass_user ")

    contrasena = cursor.fetchall()

    for contrasena_bolean in contrasena:
        contrasena = contrasena_bolean[0]

    cursor.close()
    return contrasena


def recuperar_contrasena_encryptada():

    con = sqlite3.connect("pass.db")
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

        con = sqlite3.connect("pass.db")
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
        opcionwhile = True
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
            opcionwhile = False

        elif opcion == "1":
            print("")
            print("--------------------")
            print("[LISTA DE CONTACTOS]")
            print("--------------------")
            print("")

            ver_contactos_opcion1()

            print("")
            input("Presione una tecla para continuar...")
            menu_inicio()
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


def ver_contactos_opcion1():
    """Devuelve todos los contactos de la agenda"""

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()

    for i in resultado:
        print("%s %s %s %s" % (i[0], i[1], i[2], i[3]))

    cursor.close()



def anadir_contactos_opcion2():
    """Agrega un nuevo contacto a la Agenda"""
    print("")
    print("------------------")
    print("[AGREGAR CONTACTO]")
    print("------------------")
    print("")

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    nombre = input("Nombre: ")
    apellido = input("Apellidos: ")
    telefono = input("Telefono: ")
    correo = input("Email: ")

    cursor.execute("insert into datos (nombre, apellido, telefono, correo) values ('%s','%s','%s','%s')" % (
        nombre, apellido, telefono, correo))

    con.commit()

    print("")
    print("Los datos fueron agregados correctamente")

    cursor.close()
    time.sleep(2)
    menu_inicio()


def editar_contactos_opcion3():
    x = buscar_contactos_opcion5()
    nombre = x[0][0]

    while True:
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

        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()

        if opcion == '1':
            nuevoNombre = input("Ingrese el nuevo nombre: ")
            cursor.execute("UPDATE datos SET nombre = '%s' WHERE nombre='%s'" % (nuevoNombre, nombre))
            con.commit()
            nombre = nuevoNombre
        elif opcion == '2':
            apellido = input("Ingrese el nuevo apellido: ")
            cursor.execute("UPDATE datos SET apellido = '%s' WHERE nombre='%s'" % (apellido, nombre))
            con.commit()
        elif opcion == '3':
            telefono = input("Ingrese el nuevo telefono: ")
            cursor.execute("UPDATE datos SET telefono = '%s' WHERE nombre='%s'" % (telefono, nombre))
            con.commit()
        elif opcion == '4':
            correo = input("Ingrese el nuevo correo: ")
            cursor.execute("UPDATE datos SET correo = '%s' WHERE nombre='%s'" % (correo, nombre))
            con.commit()
        else:
            break

    cursor.close()

    print("")
    print("Los datos fueron agregados correctamente")

    cursor.close()
    time.sleep(2)
    menu_inicio()


def eliminar_contactos_opcion4():
    """Elimina un contacto de la Agenda"""

    print("")
    print("--------------------")
    print("[ELIMINAR CONTACTOS]")
    print("--------------------")
    print("")

    ver_contactos_opcion1()

    print("")
    print("")
    print("INGRESE LOS DATOS DEL CONTACTO QUE DESEA ELIMINAR")
    nombre = input("Nombre: ")
    apellido = input("Apellidos: ")

    print("")
    print("")

    #recupera los nombres y apellidos de la base de datos y los compara, si hay exactitud continua de lo contrario no
    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM datos WHERE nombre = '%s' AND apellido = '%s'" % (nombre, apellido))
    buscar = cursor.fetchall()

    print("")
    si_existe = 0
    for existe in buscar:
        if nombre == existe[0] and apellido == existe[1]:
            si_existe = 1

    #si existe el contacto a eliminar solicita la contraseña para eliminar
    if si_existe == 1:
        contrasena = input("Ingrese su contraseña para eliminar: ")
        if encryptar_contrasena(contrasena) == recuperar_contrasena_encryptada():

            cursor.execute("DELETE FROM datos WHERE nombre='%s'" % (nombre))

            con.commit()

            cursor.close()

            print("Contacto eliminado correctamente...")
        else:
            print("[ERROR DE CONTRASEÑA]")
    else:
        print("[ERROR: NO SE HA ENCONTRADO CONTACTO ")

    time.sleep(2)
    menu_inicio()


def buscar_contactos_opcion5():
    """Busca un contacto en la agenda y lo lista"""

    print("Buscar contacto")
    print("---------------")
    print("")

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    buscar = input("Nombre a buscar: ")

    cursor.execute("SELECT * FROM datos WHERE nombre = '%s'" % (buscar))

    x = cursor.fetchall()

    print("")

    for i in x:
        print("Nombre:", i[0])
        print("Apellido:", i[1])
        print("Telefono:", i[2])
        print("Correo:", i[3])
        print("")

    cursor.close()

    return x


def opciones_opcion6():
    opcionwhile = False

    while opcionwhile == False:
        opcionwhile = True
        print("")
        print("-------------")
        print("[MENÚ OPCIONES]")
        print("-------------")
        print("")
        print("[1] Exportar Contactos.")
        print("[2] Importar Contactos.")
        print("[0] Atras.")

        opcion = input("Eliga una Opción: ")

        if opcion != "1" and opcion != "2" and opcion != "0":
            print("")
            print("")
            print("[Opcion Incorrecta]")
            print("")
            time.sleep(2)
            opcionwhile = False

        elif opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "0":
            menu_inicio()


def salir_opcion0():
    print("")
    print("Saliendo de Agenda...")
    print("")
    print("")
    time.sleep(2)
    exit()


if __name__ == '__main__':
    run()