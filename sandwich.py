class Sandwich:
    """
    Clase Sandwich que genera un Sandwich con nombre y costo de este.
    """
    def __init__(self, name):
        """
        name:param: nombre del sandwich
        cost:param: costo del sandwich
        """
        self.name = name
        if self.name == 'JyQ':
            self.cost = 7000
        elif self.name == 'Ita':
            self.cost = 8500
        elif self.name == 'RB':
            self.cost = 10300
        else:
            raise Exception('El sandwich pedido no existe.')

    def get_cost(self):
        """
        retorna el costo del sandwich respectivo.
        """
        return self.cost

    def get_name(self):
        """
        retorna el nombre completo del sandwich seleccionado.
        """
        if self.name == 'JyQ':
            complete_name = 'Jamón y Queso'
        elif self.name == 'Ita':
            complete_name = 'Italiano'
        elif self.name == 'RB':
            complete_name = 'Roast Beef'
        else:
            raise Exception('El sandwich pedido no existe.')
        return complete_name

    def __str__(self):
        return self.get_name()
