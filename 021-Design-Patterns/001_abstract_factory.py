from abc import ABC, abstractmethod


class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa(Chair):
    pass


class Table(Chair):
    pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self): ...

    @abstractmethod
    def create_sofa(self): ...

    @abstractmethod
    def create_table(self): ...


class StyledFactory(AbstractFactory):
    style = ""

    def create_chair(self):
        return Chair(f"{self.style} chair")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa")

    def create_table(self):
        return Table(f"{self.style} table")


class VictorianFactory(StyledFactory):
    style = "Victorian"


class ModernFactory(StyledFactory):
    style = "Modern"


class FuturisticFactory(StyledFactory):
    style = "Futuristic"


if __name__ == "__main__":
    factory = ModernFactory()
    print(factory.create_chair(), factory.create_sofa(), factory.create_table(), sep="\n")
