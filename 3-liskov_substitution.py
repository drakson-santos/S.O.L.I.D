# Observe que nossa class Duck (Pato) tem o metodo swin (nadar), e que toda classe que herde Duck poderá usar este metodo.
# Quando ToyDuck (Brinquedo Pato) herda de Duck e aplicamos o override no metodo swim, estamos modificando a essencia de Duck,
# pois, ele nao precisa de bateria para poder nadar.

# Problema
class Duck:

    def swim(self):
        pass


class ToyDuck(Duck):

    def __init__(self, battery):
        self.battery = battery

    # override
    def swim(self):
        if self.battery:
            # Swim
            pass

# ToyDuck nao pode herdar de duck.

# Solucao
class FemaleDuck(Duck):

    def lay_egg(self):
        pass