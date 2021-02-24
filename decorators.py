def admixture(function):
    """
    Decorator
    """
    def wrapper(sandwich, additions=''):
        """
        :param sandwich: Sandwich al cual se le van a agregar las adiciones.
        :param additions: Adiciones a agregar.
        :return: El valor total de la compra y la factura completa con lo comprado.
        """
        total = 0
        if isinstance(additions, list):
            for addition in additions:
                total += sandwich.get_cost() + function(addition)
        else:
            if additions == '':
                additions = 'Ninguna'
                total += sandwich.get_cost()
            else:
                total += sandwich.get_cost() + function(additions)

        pedido_tot = f"Tipo de Sandwich: \t {sandwich.get_name()}\n" \
                     f"Adiciones: \t\t\t {', '.join(additions) if isinstance(additions, list) else additions}\n" \
                     f"Total: \t\t\t\t ${total}"
        return total, pedido_tot
    return wrapper
