from sandwich import Sandwich
from decorators import admixture


@admixture
def addition(adi):
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


sandwich = Sandwich('JyQ')
total, pedido_tot = addition(sandwich, ['tomate', 'cebolla'])
print(pedido_tot)
