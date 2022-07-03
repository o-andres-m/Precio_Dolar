import requests
import os
from tabulate import tabulate

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
    except:
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
        r = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolaroficial')
        response_value = r.json()
    except:
        print ('Error al conectar con el servidor...')
        return None
    if options == 0:
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
        r = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarblue')
        response_value = r.json()
    except:
        print ('Error al conectar con el servidor...')
        return None
    if options == 0:
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
    ofdicial_price = dolar_oficial(options=1)
    blue_price = dolar_blue(options=1)
    list_to_print= [['OFICIAL',ofdicial_price['compra'],ofdicial_price['venta']],['BLUE',blue_price['compra'],blue_price['venta']]]
    print (tabulate(list_to_print,['TIPO','COMPRA','VENTA']))
    print ('Precios actualizados al dia : ',ofdicial_price['fecha'][0:10])
    input ('Presione ENTER para continuar...')

while True:
    os.system('cls')
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