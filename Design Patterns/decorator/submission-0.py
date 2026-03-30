class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self):
        return self.decoratedCoffee.getCost()+.5
    # Implement the Milk decorator

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self):
        return self.decoratedCoffee.getCost()+.2
    # Implement the Sugar decorator

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self):
        return self.decoratedCoffee.getCost()+.7
    # Implement the Cream decorator

