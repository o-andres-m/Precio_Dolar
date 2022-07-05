import requests
import os
from tabulate import tabulate
import argparse

def validate_numbers(number):
    """Recieves a variable, and try to make a casting to int var,
    if they cant do it, print an error, and call again to the function.
    Args:
        number (str)
    Returns:
        an INT Number
    """
    try:
        number=int(number)
        return number
    except ValueError:
        print('Ingrese solo un VALOR NUMERICO...')
        number=input('>>>')
        number = validate_numbers(number)
        return number

def print_menu():
    """Print the options menu, make an user input, and call 'validate_numbers' function
    Args:
        None
    Returns:
        Returns the option validated (INT Number)
    """
    print ("""Menu:
    1 - Consultar Precio DOLAR OFICIAL.
    2 - Consultar Precio DOLAR BLUE.
    3 - Precio OFICIAL vs BLUE
    4 - Salir""")
    number_value = input ('>>>')
    number_value = validate_numbers(number_value)
    return number_value

def dolar_oficial(options =0):
    """Connect to server and returns the price of Dolar OFICIAL

    Args:
        options (int, optional): if reciebves '1', returns only the response of server . Defaults to 0.
    Returns:
        2 cases.
        in firs case, do not returns anything, only print in screen the prices
        in second case, returns the json response of server.
    """
    print ('Obteniendo datos....')
    try:
        r = requests.get(official_url)
        response_value = r.json()
    except requests.exceptions.ConnectionError:
        print ('Error al conectar con el servidor...')
        input ('Presione ENTER para continuar...')
        return None
    except requests.exceptions.JSONDecodeError:
        print ('Error al obtener los datos. Verifique URL.')
        input ('Presione ENTER para continuar...')
        return None
    except requests.exceptions.MissingSchema:
        print ('Error al obtener los datos. Verifique URL.')
        input ('Presione ENTER para continuar...')
        return None
    if options == 0:
        os.system('cls')
        print ('PRECIOS DOLAR OFICIAL')
        print ('Precio de Compra: ',response_value['compra'])
        print ('Precio de venta: ',response_value['venta'])
        print ('Precios actualizados al dia : ',response_value['fecha'][0:10])
        print('')
        input ('Presione ENTER para continuar...')
    else:
        return response_value

def dolar_blue(options = 0):
    """Connect to server and returns the price of Dolar BLUE
    Args:
        options (int, optional): if reciebves '1', returns only the response of server . Defaults to 0.
    Returns:
        2 cases.
        in firs case, do not returns anything, only print in screen the prices
        in second case, returns the json response of server.
    """
    print ('Obteniendo datos....')
    try:
        r = requests.get(blue_url)
        response_value = r.json()
    except requests.exceptions.ConnectionError:
        print ('Error al conectar con el servidor...')
        input ('Presione ENTER para continuar...')
        return None
    except requests.exceptions.JSONDecodeError:
        print ('Error al obtener los datos. Verifique URL.')
        input ('Presione ENTER para continuar...')
        return None
    except requests.exceptions.MissingSchema:
        print ('Error al obtener los datos. Verifique URL.')
        input ('Presione ENTER para continuar...')
        return None
    if options == 0:
        os.system('cls')
        print ('PRECIOS DOLAR BLUE')
        print ('Precio de Compra: ',response_value['compra'])
        print ('Precio de venta: ',response_value['venta'])
        print ('Precios actualizados al dia : ',response_value['fecha'][0:10])
        print('')
        input ('Presione ENTER para continuar...')
    else:
        return response_value

def compare_prices():
    """Make a comparation the price of Official and BLue Prices
        Print the prices in the screen with 'tabulate' style
    Args:
        None
    Returns:
        None
    """
    official_price = dolar_oficial(options=1)
    blue_price = dolar_blue(options=1)
    try:
        list_to_print= [['OFICIAL',official_price['compra'],official_price['venta']],['BLUE',blue_price['compra'],blue_price['venta']]]
        os.system('cls')
        print (tabulate(list_to_print,['TIPO','COMPRA','VENTA']))
        print ('Precios actualizados al dia : ',official_price['fecha'][0:10])
        input ('Presione ENTER para continuar...')
    except TypeError:
        print ("Error en formato al obtener los datos, verifique URL...")
        input ('Presione ENTER para continuar...')


#create parser
parser = argparse.ArgumentParser()
parser.add_argument('--burl', type=str, help='Url de la API para obtener el precio del Dolar Blue',required=False)
parser.add_argument('--ourl', type=str, help='Url de la API para obtener el preciodel Dolar Oficial',required=False)
parser.add_argument('--type', type=str, help='"oficial" para obtener oficial, "blue" para obtener blue',required=False)
args = parser.parse_args()

#set defaults urls and type of selection
blue_url ='https://api-dolar-argentina.herokuapp.com/api/dolarblue'
official_url ='https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
price_selected = 0

#take the URLS and the type of dollar to get price if the program have arguments
if args.burl:
    blue_url = args.burl
if args.ourl:
    official_url = args.ourl
if args.type:
    price_selected = args.type

#set flag=0
flag=0

while True:
    os.system('cls')
    #default starts program, flag = 0
    if flag == 0:
        if price_selected == 'oficial':
            dolar_oficial()
            os.system('cls')
        elif price_selected == 'blue':
           dolar_blue()
           os.system('cls')
        elif price_selected == 0:
            compare_prices()
            os.system('cls')
        #set flag = 1
        flag = 1
    
    #now the program print the menu for options
    option_menu = print_menu()
    if not 0<option_menu<5:
        input ('Seleccione una opcion valida...(ENTER PARA CONTINUAR)')
        continue
    if option_menu == 1:
        dolar_oficial()
        os.system('cls')
    if option_menu == 2:
        dolar_blue()
        os.system('cls')
    if option_menu == 3:
        compare_prices()
        os.system('cls')
    if option_menu == 4:
        os.system('cls')
        print ('Fin del programa...')
        break