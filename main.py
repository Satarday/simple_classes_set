class Plants:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def see_plant(self):
        print("Растение ", self.name, " вида ", self.species)


class Tree(Plants):

    def __init__(self, name, species, age):
        super().__init__(name, species)
        self.age = age

    def see_age(self):
        print("Возраст дерева: ", self.age)


class Flower(Plants):

    def __init__(self, name, species, lenght):
        super().__init__(name, species)
        self.lenght = lenght

    def see_len(self):
        print("Длинна стебля цветка ", self.lenght, " мм")


class Rose(Flower):

    def __init__(self, name, species, lenght, color):
        super().__init__(name, species, lenght)
        self.color = color

    def see_color(self):
        print("Цвет розы - ", self.color)


a = Plants("Ламинария", "Водросль")
a.see_plant()
b = Flower("Ромашка", "полевые", 16)
b.see_plant()
b.see_len()
c = Tree("Ёлка", "хвойные", 100)
c.see_plant()
c.see_age()
d = Rose("Роза", "розы", 300, "Красный")
d.see_plant()
d.see_len()
d.see_color()
