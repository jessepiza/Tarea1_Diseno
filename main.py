from sandwich import Sandwich
from decorators import admixture


@admixture
def addition(adi):
    """
    :param adi: adicional a agregar (puede ser una lista de str o un str)
    :return: el costo del adicional agregado.
    """
    if adi == 'jalapeno':
        cost = 1500
    elif adi == 'pepinillo':
        cost = 650
    elif adi == 'cebolla':
        cost = 700
    elif adi == 'tomate':
        cost = 800
    else:
        raise Exception('La adición ingresada no existe.')
    return cost


# Ejemplo con varios adicionales
sandwich1 = Sandwich('JyQ') #Sandwich de Jamón y Queso
total1, pedido_tot1 = addition(sandwich1, ['tomate', 'cebolla'])
print(pedido_tot1)

print("======================================================")

#Ejemplo con un solo adicional
sandwich2 = Sandwich('RB') #Sandwich de Roast Beef
total2, pedido_tot2 = addition(sandwich2, 'pepinillo')
print(pedido_tot2)

print("======================================================")

#Ejemplo sin adicionales
sandwich3 = Sandwich('Ita') #Sandwich italiano
total3, pedido_tot3 = addition(sandwich3)
print(pedido_tot3)
