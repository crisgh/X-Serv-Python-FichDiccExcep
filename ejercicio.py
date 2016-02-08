#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola
# Cristina Gallego Herrero

fichero = open('/etc/passwd', 'r')

lineas = fichero.readlines()
fichero.close()

Users = {} # Creamos un diccionario vacio al que luego le añadimos Key y value

for linea in lineas:
    elementos = linea.split(':')
    print elementos[0], elementos[-1][:-1]
    Users[elementos[0]] = elementos[-1][:-1] # Guardamos el Key y el value de cada elemento en el diccionario

print "\nHay", len(lineas),"usuarios\n"

try:
    print "Root :", Users["root"] #Nos muestra la shell del elemento Root
    print "Imaginario :",  Users["imaginario"] # Este elemento no existe --> Except

except: #Elevamos la excepcion para el elemento del diccionario que no encuentre
    print "Usuario no encontrado"
