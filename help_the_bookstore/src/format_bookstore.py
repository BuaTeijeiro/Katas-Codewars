"""Modulo para dar formato al ejercicio de bookstore"""

def format_bookstore(type_stock, categories):
    """Da el formato deseado para el ejercicio de bookstore"""
    
    requested_stock = []
    for category in categories:
        requested_stock.append(category+' : '+str(type_stock[category]))
        
    requested_stock = ') - ('.join(requested_stock)
    return '(' + requested_stock + ')'
