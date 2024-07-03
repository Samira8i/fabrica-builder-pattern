from abc import ABC, abstractmethod

class PastaFactory(ABC):
    @abstractmethod
    def create_pasta(self):
        pass


class SpaghettiFactory(PastaFactory):
    def create_pasta(self):
        return Spaghetti()

class CapelliniFactory(PastaFactory):
    def create_pasta(self):
        return Capellini()

class BukatiniFactory(PastaFactory):
    def create_pasta(self):
        return Bukatini()

class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additives(self):
        pass


class Spaghetti(Pasta):
    def get_type(self):
        return "Спагетти"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Курица"

    def get_additives(self):
        return ["Сыр", "Чеснок"]


class Capellini(Pasta):
    def get_type(self):
        return "Капеллини"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Курица"

    def get_additives(self):
        return ["Пармезан", "Петрушка"]


class Bukatini(Pasta):
    def get_type(self):
        return "Букатини"

    def get_sauce(self):
        return "Песто соус"

    def get_filling(self):
        return "Мясо"

    def get_additives(self):
        return ["Анчоусы", "Томаты"]


class PastaDirector:
    def __init__(self, pasta_factory):
        self.pasta_factory = pasta_factory
        self.pasta = None

    def build_pasta(self):
        self.pasta = self.pasta_factory.create_pasta()

    def get_pasta(self):
        return self.pasta

    def print_pasta_details(self):
        print(f"Pasta type: {self.pasta.get_type()}")
        print(f"Sauce: {self.pasta.get_sauce()}")
        print(f"Filling: {self.pasta.get_filling()}")
        print(f"Toppings: {self.pasta.get_additives()}")


pasta_builder = PastaDirector(SpaghettiFactory)

pasta_builder.build_pasta()
pasta_builder.print_pasta_details()
print()

#я вообще не поняла, но идея у меня такая, что я создаю фабрики, а потом уже директор просто вызывает сами фабрики и его методы. Потому что я не вижу смысла создавать отдельно строителей для отдельных фабрик, если это примерно одно и то же
# но я запуталась, что вообще нужно вызывать и как код должен работать, так что он у меня выдает ошибку(