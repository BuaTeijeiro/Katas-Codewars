"""ESte modulo crea una funcion que comprueba cuantos libros de un determinado
stock hay de una serie de tipos"""

from src.format_bookstore import format_bookstore

def check_stock(stocklist, categories):
    """Esta funcion es la principal del modulo, y hace lo que este indica"""
    if stocklist == [] or categories == []:
        return ""
    
    type_stock = dict.fromkeys(categories,0)
    for code in stocklist:
        category = code[0]
        if category in type_stock:
            quantity = int(code.split(' ')[-1])
            type_stock[category] += quantity
        else:
            continue
        
    return format_bookstore(type_stock, categories)
