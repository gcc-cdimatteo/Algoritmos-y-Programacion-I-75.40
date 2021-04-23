'''
Un importante laboratorio de la zona de Pilar decidió renovar el espacio exterior de su fábrica. 
Para esto contrata a un estudio de jardinería que sugieren un conjunto de elementos que van desde adornos, mobiliario y plantas para decorar estos lugares. 
Este laboratorio ya realizó un gasto muy significativo durante el año pasado en la ejecución de las obras y del presupuesto inicial sólo dispone de cierto dinero para esta segunda etapa de decoración.
El estudio de jardinería posee un listado de elementos que sí o sí deberán ser comprados y otros que no son obligatorios pero cuantos más elementos haya mejor será.
Se pide realizar un programa donde el usuario ingrese el total de dinero a invertir (por teclado) y determine la mayor cantidad de elementos que se pueden comprar incluyendo los objetos que sean obligatorios. Deberá indicar por pantalla qué elementos compra con ese dinero y deberá indicar si el dinero no le alcanza para comprar los elementos obligatorios.
Para esto, se reciben 2 archivos. Uno llamado listadoObligatorio.txt donde están los elementos que sí o sí deberán comprarse y por otro lado un archivo llamado lista de precios.txt que contendrá un listado muy grande de artículos junto con su correspondiente precio.
	Ejemplo archivos (deberán ser creados por el alumno y entregado junto con el código)
ListadoObligatorio.txt
[objeto, cantidad]
	Cenicero de jardín, 3
	Banco de plaza, 35
	Plantines varios, 20
	Geranios, 5
Lavanda,8
Maceta cemento mediana, 3
Maceta cemento grande, 2
Rosales,5
Álamo,4
Arce,1
Cespedxm2, 20
Limonero, 1
	Lista de precios.txt
	[objeto, precio por unidad]
	Plantines varios, 50
	Limonero, 250
	Cedro, 800
	Castaño, 600
	Ciruelo de jardín, 300
	Ciruelo, 500
Álamo, 600
Arce, 1200
	Tipa, 900
	Algarrobo, 900
	Lapacho rosado, 1300
	Palmera brasileña, 800
	Jacarandá, 700
	Palo borracho, 300
	Peral, 300
	Olivo, 600
	Banco de jardín, 4000
	Cenicero de jardín, 1200
	Maceta cemento chica, 2300
	Maceta cemento mediana, 3000
	Maceta cemento grande, 3500
	Cespedxm2, 600
	Geranios, 120
Lavanda,v80
Rosales, 250
	….
'''

import re
import copy
from collections import defaultdict

PURCHASE_HEADERS = ["objeto", "cantidad"]

PRODUCT_HEADERS = ["objeto", "precio por unidad", "stock"]


def read_file(filepath  # type: str
              ):

    data = []

    try:
        f = open(filepath, "r", encoding="utf-8")
    except IOError:
        print("No se pudo leer el archivo: ", filepath)
    
    with f:
        data = f.read().splitlines()

    return data


def validate_number(number  # type: str
                    ):

    formatted_number = ""
    value = 0

    formatted_number = re.sub("[a-zA-Z]+", "", number)

    try:
        value = int(formatted_number)

    except ValueError:
        value = float(formatted_number)

    return value


def parse_data_to_purchase(data  # type: str
                           ):
    
    formatted_data = []
    purchase = {}

    formatted_data = re.split("\t|\,\s*|\,", data)
    formatted_data = list(filter(None, formatted_data))

    for x in range(len(PURCHASE_HEADERS)):

        if PURCHASE_HEADERS[x] == "cantidad":
            purchase[PURCHASE_HEADERS[x]] = validate_number(formatted_data[x])

        else:
            purchase[PURCHASE_HEADERS[x]] = formatted_data[x]

    return purchase


def parse_data_to_product(data  # type: str
                          ):
    
    formatted_data = []
    purchase = {}

    formatted_data = re.split("\t|\,\s*|\,", data)
    formatted_data = list(filter(None, formatted_data))

    for x in range(len(PRODUCT_HEADERS)):

        if PRODUCT_HEADERS[x] == "precio por unidad":
            purchase[PRODUCT_HEADERS[x]] = validate_number(formatted_data[x])

        elif PRODUCT_HEADERS[x] == "stock":
            purchase[PRODUCT_HEADERS[x]] = validate_number(formatted_data[x])

        else:
            purchase[PRODUCT_HEADERS[x]] = formatted_data[x]

    return purchase


def fill_missing_data(data  # type: list[dict]
                      ):

    completed_data = []

    completed_data = copy.deepcopy(data)

    for x in range(len(completed_data)):
        data_item = completed_data[x]

        while("cantidad" not in data_item or
              "precio por unidad" not in data_item or
              "stock" not in data_item):

            if "cantidad" not in data_item:
                data_item["cantidad"] = 0

            elif "precio por unidad" not in data_item:
                data_item["precio por unidad"] = 0

            elif "stock" not in data_item:
                data_item["stock"] = 0

    return completed_data


def join_data_by_common_key(purchases,  # type: list[dict]
                            prices,  # type: list[dict]
                            ):

    dict_of_dicts = {}
    list_of_dicts = []

    dict_of_dicts = defaultdict(dict)

    for elem in (purchases, prices):
        
        for sub_elem in elem:
            dict_of_dicts[sub_elem["objeto"]].update(sub_elem)

    list_of_dicts = [value for value in dict_of_dicts.values()]

    list_of_dicts = fill_missing_data(list_of_dicts)

    return list_of_dicts


def filter_by_quantity(data,  # type: list[dict]
                       enforce_opposite=False,  # type: bool
                       quantity=0  # type: int
                       ):

    filtered_data = []

    if enforce_opposite:
        filtered_data = [data_item for data_item in copy.deepcopy(data) if data_item.get("cantidad") != quantity]
    else:
        filtered_data = [data_item for data_item in copy.deepcopy(data) if data_item.get("cantidad") == quantity]

    return filtered_data



def validate_input_money():
    input_money = ""
    money = 0

    input_money = input("Ingrese el dinero a invertir: ")

    while money <= 0:
        try:
            money = validate_number(input_money)

            if money <= 0:
                print("\n¡Sólo puedes ingresar montos positivos!")

        except ValueError:
            print("\n¡Sólo se pueden ingresar numeros!")

    return money


def get_valid_quantity(money,  # type: int
                       quantity,  # type: int 
                       price  # type: int
                       ):

    total = 0

    total = quantity * price

    while money < total and quantity != 0:
        quantity -= 1

        total = quantity * price

    return quantity


def update_stock(product,  # type: dict
                 purchased_product,  # type: dict
                 quantity  # type: int
                 ):
    
    for key, value in product.items():

        if value == purchased_product.get("objeto"):

            if product.get("stock") != 0:
                product.update({
                    "stock": product.get("stock") - quantity
                })


def print_essential_products(products  # type: list[dict]
                             ):

    qty_prds_not_purchased = 0
    qty_unknown_prds = 0

    for product in products:

        if product.get("cantidad") == 0:
            qty_prds_not_purchased += 1

        elif product.get("precio por unidad") == 0:
            qty_unknown_prds += 1

    if qty_unknown_prds != 0:
        qty_prds_not_purchased += qty_unknown_prds

    if qty_prds_not_purchased == qty_unknown_prds:
        print("\nEl dinero alcanzó para comprar todos los objetos obligatorios.")     

        for product in products:
            if(product.get("precio por unidad") != 0):
                print("\n\tSe compró el objeto '{0}', por una cantidad de {1} unidad/es, a un precio de ${2} c/u".format(
                    product.get("objeto"),
                    product.get("cantidad"),
                    product.get("precio por unidad")
                ))

    else:
        print("\nEl dinero no alcanzó para comprar todos los objetos obligatorios.") 

        for product in products:
            if(product.get("precio por unidad") != 0):
                if(product.get("cantidad") != 0):
                    print("\n\tSe compró el objeto '{0}', por una cantidad de {1} unidad/es, a un precio de ${2} c/u".format(
                        product.get("objeto"),
                        product.get("cantidad"),
                        product.get("precio por unidad")
                    ))    


def print_optional_products(products  # type: list[dict]
                            ):

    qty_prds_not_purchased = 0
    qty_unknown_prds = 0
    qty_optional_prds = 0

    for product in products:

        if product.get("cantidad") == 0:
            qty_prds_not_purchased += 1

        elif product.get("precio por unidad") == 0:
            qty_unknown_prds += 1

    if qty_unknown_prds != 0:
        qty_prds_not_purchased += qty_unknown_prds

    qty_optional_prds = len(products)

    if qty_optional_prds == qty_prds_not_purchased:
        print("\nNo se compró ningún objeto opcional.")

    else:
        print("\nSe logró comprar objetos opcionales.")

        for product in products:
            if(product.get("precio por unidad") != 0):
                if(product.get("cantidad") != 0):
                    print("\n\tSe compró el objeto '{0}', por una cantidad de {1} unidad/es, a un precio de ${2} c/u".format(
                        product.get("objeto"),
                        product.get("cantidad"),
                        product.get("precio por unidad")
                    ))                                    


def execute_purchase(joined_data  # type: list[dict]
                     ):

    money = 0
    products_quantity = 0
    price = 0    
    total = 0
    filtered_data = []
    essential_products_purchased = []
    optional_products_purchased = []

    money = validate_input_money()
    filtered_data = filter_by_quantity(joined_data, True)

    print(f"\nEl monto ingresado fue de ${money}")

    for x in range(len(filtered_data)):
        products_quantity = filtered_data[x].get("cantidad")
        price = filtered_data[x].get("precio por unidad")
        total = products_quantity * price

        if total == 0:
            essential_products_purchased.append(filtered_data[x])

        else:
            if money >= total:
                essential_products_purchased.append(filtered_data[x])

                for data_item in joined_data:
                    update_stock(data_item, filtered_data[x], products_quantity)
                
                money -= total

            else:
                products_quantity = get_valid_quantity(money, products_quantity, price)

                total = products_quantity * price

                filtered_data[x].update({
                    "cantidad": products_quantity
                })

                essential_products_purchased.append(filtered_data[x])

                for data_item in joined_data:
                    update_stock(data_item, filtered_data[x], products_quantity)

                money -= total

    filtered_data = copy.deepcopy(joined_data)

    for x in range(len(filtered_data)):
        products_quantity = filtered_data[x].get("stock")
        price = filtered_data[x].get("precio por unidad")
        total = products_quantity * price

        if total == 0:
            optional_products_purchased.append(filtered_data[x])

        else:
            if money >= total:
                filtered_data[x].update({
                    "cantidad": products_quantity
                })

                optional_products_purchased.append(filtered_data[x])

                for data_item in filtered_data:
                    update_stock(data_item, filtered_data[x], products_quantity)
                
                money -= total

            else:
                products_quantity = get_valid_quantity(money, products_quantity, price)

                total = products_quantity * price

                filtered_data[x].update({
                    "cantidad": products_quantity
                })

                optional_products_purchased.append(filtered_data[x])

                for data_item in filtered_data:
                    update_stock(data_item, filtered_data[x], products_quantity)

                money -= total

    print_essential_products(essential_products_purchased)

    print_optional_products(optional_products_purchased)


def main():
    data = []
    purchases = []
    prices = []
    joined_data = []

    data = read_file("listadoObligatorio.txt")

    for x in range(len(data)):

        purchases.append(
            parse_data_to_purchase(data[x])
        )

    data = read_file("precios.txt")

    for x in range(len(data)):

        prices.append(
            parse_data_to_product(data[x])
        )

    joined_data = join_data_by_common_key(purchases, prices)

    joined_data = sorted(joined_data, key=lambda x: (x['precio por unidad'], x['cantidad']))

    execute_purchase(joined_data)


if __name__ == "__main__":
    main()