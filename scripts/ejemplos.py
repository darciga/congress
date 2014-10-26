# coding=utf-8
import sys
import urllib2

__author__ = 'pollitux'


def IF():
    nombre = "Raul"
    if nombre == "Raul":
        print "\n Hola Raúl"
    elif nombre == "Jesús":
        print "Hola Jesús"
    else:
        print "Quien eres?"


def WHILE():
    contador = 1
    while contador <= 20:
        print "Contador %d " % contador
        contador += 1


def FOR():
    for i in range(20):
        print i


def EXCEPTION():
    try:
        return 3 / 0
    except ZeroDivisionError as e:
        print "\n Division entre 0"
        print e


def getWeb():
    try:
        web = urllib2.urlopen("http://itjiquilpan.edu.mx/")
        print web.read()
        web.close()
    except urllib2.HTTPError, e:
        print e
    except urllib2.URLError as e:
        print e


class Estudiante(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return self.nombre

    def esMayor(self):
        if self.edad >= 18:
            return True
        else:
            return False


tupla = (1, 2, 3, 4)
diccionario = [{"nombre": "Raul", "apellido": "Granados", "Edad": 24},
               {"nombre": "Jesus", "apellido": "Granados", "Edad": 10}]

lista = [1, 2, 3, 4]


def estructuras():
    print "Listando los elementos de la tupla"
    for t in tupla:
        print t

    print "Listando los elementos del diccionario"
    for d in diccionario:
        print d["nombre"]

    print "Listando los elementos de la lista"
    for l in lista:
        print l


def main():
    # IF()
    # WHILE()
    # FOR()
    # EXCEPTION()
    # getWeb()
    '''e = Estudiante("Raul", 24)
    print "Hola mi nombre es %s " % e.hola()
    if e.esMayor():
        print "%s es mayor de edad" % e.nombre
    else:
        print "%s no es mayor de edad" % e.nombre'''
    # estructuras()

    anyError = False

    if anyError:
        sys.exit(1)
    else:
        print "\n Proceso terminado"
        sys.exit(0)


if __name__ == "__main__":
    main()