def valida_numero(valor):
    try:
        valor=int(valor)
        return valor
    except:
        print('Ingrese solo un VALOR NUMERICO...')
        valor=input('>>>')
        valor = valida_numero(valor)
        return valor

def print_menu():
    print ("""Menu:
    1 - Consultar Precio DOLAR OFICIAL.
    2 - Consultar Precio DOLAR BLUE.
    3 - Precio OFICIAL vs BLUE
    4 - Salir""")
    valor = input ('>>>')
    valor = valida_numero(valor)
    return valor

def dolar_oficial(retorno =0):
    
    print ('Obteniendo datos....')
    try:
        r = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolaroficial')
        valor = r.json()
    except:
        print ('Error al conectar con el servidor...')
        return None
    if retorno == 0:
        print ('PRECIOS DOLAR OFICIAL')
        print ('Precio de Compra: ',valor['compra'])
        print ('Precio de venta: ',valor['venta'])
        print ('Precios actualizados al dia : ',valor['fecha'][0:10])
        print('')
        input ('Presione ENTER para continuar...')
    else:
        return valor

def dolar_blue(retorno = 0):
    print ('Obteniendo datos....')
    try:
        r = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarblue')
        valor = r.json()
    except:
        print ('Error al conectar con el servidor...')
        return None       
    if retorno == 0:
        print ('PRECIOS DOLAR BLUE')
        print ('Precio de Compra: ',valor['compra'])
        print ('Precio de venta: ',valor['venta'])
        print ('Precios actualizados al dia : ',valor['fecha'][0:10])
        print('')
        input ('Presione ENTER para continuar...')
    else:
        return valor

def comparacion():
    oficial = dolar_oficial(retorno=1)
    blue = dolar_blue(retorno=1)
    lista= [['OFICIAL',oficial['compra'],oficial['venta']],['BLUE',blue['compra'],blue['venta']]]
    print (tabulate(lista,['TIPO','COMPRA','VENTA']))
    print ('Precios actualizados al dia : ',oficial['fecha'][0:10])
    input ('Presione ENTER para continuar...')


import requests
import os
from tabulate import tabulate



while True:
    
    os.system('cls')
    op = print_menu()
    if not 0<op<5:
        input ('Seleccione una opcion valida...(ENTER PARA CONTINUAR)')
        continue
    if op == 1:
        dolar_oficial()
        os.system('cls')
    if op == 2:
        dolar_blue()
        os.system('cls')
    if op == 3:
        comparacion()
        os.system('cls')
    if op == 4:
        os.system('cls')
        print ('Fin del programa...')
        break
        