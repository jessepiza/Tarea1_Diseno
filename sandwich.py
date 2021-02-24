class Sandwich:
    def __init__(self, name):
        if name in ['JyQ', 'Ita', 'RB']:
            self.name = name
        else:
            raise Exception('El sandwich pedido no existe.')

    def get_cost(self):
        if self.name == 'JyQ':
            cost = 7000
        elif self.name == 'Ita':
            cost = 8500
        elif self.name == 'RB':
            cost = 10300
        else:
            raise Exception('El sandwich pedido no existe.')
        return cost

    def get_name(self):
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
