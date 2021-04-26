from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculation_of_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calculation_of_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calculation_of_consumption(self):
        return self.h * 2 + 0.3


if __name__ == '__main__':
    coat_1 = Coat(70)
    suit_1 = Suit(80)
    print(coat_1.calculation_of_consumption)
    print(suit_1.calculation_of_consumption)
