# -*- coding:utf-8 -*-
import sqlite3
import time
import os

# Conexion con Base de Datos Sqlite3
con = sqlite3.connect("agenda.db")
cursor = con.cursor()
# Comprueba si la tabla existe, en caso de no existir la crea
cursor.execute("""CREATE TABLE IF NOT EXISTS datos (nombre TEXT, apellido TEXT, telefono TEXT, correo TEXT)""")

cursor.close()



def run():
    print("[BIENVENIDO A SU AGENDA]")
    menu_contrasena()
    menu_inicio()





def menu_contrasena():
    print("...")
    contrasena1 = input("Ingrese su nueva contraseña: ")
    contrasena2 = input("Repita su contraseña: ")

    if contrasena1 == contrasena2:
        contrasena = contrasena1


    else:
        print("Error:[Las contraseñas deben ser iguales]")
        menu_contrasena()




def limpiar():
    """Limpia la pantalla"""

    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")


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
            ver_contactos_opcion1()
        elif opcion == "2":
            anadir_contactos_opcion2()
        elif opcion == "3":
            editar_contactos_opcion3()
        elif opcion == "4":
            eliminar_contactos_opcion4()
        elif opcion == "5":
            buscar_contactos_opcion5()
        elif opcion == "6":
            opciones_opcion6()
        elif opcion == "0":
            salir_opcion0()


def ver_contactos_opcion1():
    """Devuelve todos los contactos de la agenda"""

    print("")
    print("--------------------")
    print("[LISTA DE CONTACTOS]")
    print("--------------------")
    print("")

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()

    for i in resultado:
        print("%s %s %s %s" % (i[0], i[1], i[2], i[3]))

    cursor.close()

    print("")
    input("Presione una tecla para continuar...")
    menu_inicio()


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
    pass


def eliminar_contactos_opcion4():
    """Elimina un contacto de la Agenda"""

    print("")
    print("--------------------")
    print("[ELIMINAR CONTACTOS]")
    print("--------------------")
    print("")

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()

    for i in resultado:
        print("%s %s %s %s" % (i[0], i[1], i[2], i[3]))

    cursor.close()

    #eliminar

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    print("")
    print("")
    eliminar = input("Nombre de contacto que desea eliminar: ")

    cursor.execute("DELETE FROM datos WHERE nombre='%s'" % (eliminar))

    con.commit()

    cursor.close()

    print("Contacto eliminao correctamente...")
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

    print("")
    input("Presione una tecla para continuar...")
    menu_inicio()


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
        elif opcion == "3":
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