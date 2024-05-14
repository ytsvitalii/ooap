from abc import ABC, abstractmethod


class IMapComponent(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def find_child(self, name):
        ...


class MapComponent(IMapComponent):
    def __init__(self, name, x, y):
        super().__init__(x, y)
        self.name = name
        self._children = []

    def add_component(self, component: IMapComponent):
        component.parent = self
        self._children.append(component)

    def draw(self, indent=''):
        print(f"{indent}- {self.name} ({self._x}, {self._y})")
        for child in self._children:
            child.draw(indent + "  ")

    def find_child(self, name):
        if self.name == name:
            return True

        for child in self._children:
            if child.find_child(name):
                return True
        return False


class Building(MapComponent):
    def draw(self, indent=""):
        super().draw(indent + "  ")


class Road(MapComponent):
    def draw(self, indent=""):
        super().draw(indent + "  ")


class Park(MapComponent):
    def draw(self, indent=""):
        super().draw(indent + "  ")


city_map = MapComponent("Рівне", 0, 0)

park1 = Park("Центральний парк", 10, 10)
city_map.add_component(park1)

building1 = Building("Школа №22", 20, 30)
building1.add_component(Building("Школа кунг-фу", 21, 31))
park1.add_component(building1)

road1 = Road("Проспект Миру", 40, 50)
city_map.add_component(road1)

building2 = Building("Фокстрот", 50, 60)
road1.add_component(building2)
road1.add_component(Building("Ельдорадо", 50, 65))
road1.add_component(Building("АТБ", 55, 70))

city_map.draw()

print('\nПрисутні на карті?\n'
      f'Школа Кунг-Фу: {"Так" if city_map.find_child("Школа кунг-фу") else "Ні"}\n'
      f'Супермаркет Novus: {"Так" if city_map.find_child("Novus") else "Ні"}')
