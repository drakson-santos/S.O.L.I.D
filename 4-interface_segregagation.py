
# Problema
class IShoppingCart:
    def clear(self):
        raise NotImplementedError()

    def add_item(self, item):
        raise NotImplementedError()

    def accommodate_child(self, child):
        raise NotImplementedError()

class Cart(IShoppingCart):
    def clear(self):
        pass

    def add_item(self, item):
        pass

    def accommodate_child(self, child):
        pass


class Basket(IShoppingCart):
    def clear(self):
        pass

    def add_item(self, item):
        pass

    def accommodate_child(self, child):
        raise Exception("Method not allowed")


# Solucao
class IShoppingCart:
    def clear(self):
        raise NotImplementedError()

    def add(self, item):
        raise NotImplementedError()

class IAccommodateChild:
    def accommodate(self, child):
        raise NotImplementedError()

class Cart(IShoppingCart, IAccommodateChild):
    def clear(self):
        pass

    def add_item(self, item):
        pass

    def accommodate_child(self, child):
        pass


class Basket(IShoppingCart):
    def clear(self):
        pass

    def add_item(self, item):
        pass

    def accommodate_child(self, child):
        raise Exception("Method not allowed")