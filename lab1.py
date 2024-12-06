import doctest
from typing import Union
class Door:
    def __init__(self, color: str, width: int, height: int):
        """

        Создание и подготовка к работе объекта "Дверь"

        :param color: цвет двери
        :param width: ширина двери
        :param height: высота двери

        Примеры:
        >>> door = Door('белый', 75, 150) #инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError('Цвет двери должен быть типа str')
        if not isinstance(width, int):
            raise TypeError('Ширина двери должна быть типа int')
        if not isinstance(height, int):
            raise TypeError('Высота двери должна быть типа int')
        if width <= 0:
            raise ValueError('Ширина двери не может быть отрицательной или равна 0')
        if height <=0:
            raise ValueError('Высота двери не может быть отрицательной или равна 0')
        self.color = color
        self.width = width
        self.height = height

    def open_or_close_door(self, position: int) -> None:
        """
        Функция, которая открывает или закрывает дверь (position = 0 - дверь закрыта,
        position = 1 - дверь открыта)

        :return ValueError: Если дверь уже открыта/закрыта

        Пример:
        >>> door = Door('белый', 75, 150)
        >>> door.open_or_close_door(1)
        """
        ...

    def  is_door_opened(self) -> bool:
        """
        Функция, которая проверяет, открыта ли дверь

        :return: Открыта ли дверь

        Примеры:
        >>> door = Door('белый', 75, 150)
        >>> door.is_door_opened()
        """
        ...

class Cylinder:
    def __init__(self, radius: Union[float, int], element: Union[float, int]):
        """

        Создание и подготовка к работе объекта "Цилиндр"

        :param radius: радиус окружности в основании
        :param element: длина образующей

        Примеры:
        >>> cylinder = Cylinder(10, 5) #инициализация экземпляра класса
        """
        if not isinstance(radius, (float, int)):
            raise TypeError('Радиус окружности в основании должен быть типа int или float')
        if not isinstance(element, (float, int)):
            raise TypeError('Длина образующей должна быть типа int или float')
        if radius < 0:
            raise ValueError('Радиус окружности в основанияя должен быть больше нуля')
        if element  <= 0:
            raise ValueError('Длина образуйющей должна быть больше 0')
        self.radius = radius
        self.element = element

    def volume(self) -> float:
        """
        Функция для вычисления объема цилиндра

        :return: Объем цилиндра

        Примеры:
        >>> cylinder = Cylinder(10, 5)
        >>> print(cylinder.volume())
        1570.0
        """
        v = 3.14 * self.radius ** 2 * self.element
        return v

    def area(self) -> float:
        """
        Функция для вычисления площади поверхности цилиндра

        :return: Площадь поверхности цилиндра

        Примеры:
        >>> cylinder = Cylinder(10, 5)
        >>> print(cylinder.area())
        942.0
        """
        c = 2 * 3.14 * self.radius ** 2 + 2 * 3.14 * self.radius * self.element
        return c

class Human:
    def __init__(self, sex: str, age: int, name: str):
        """

        Создание и подготовка к работе объекта "Человек"

        :param sex: пол человека
        :param age: возраст человека
        :param name: имя человека

        Примеры:
        >>> human = Human('мужчина', 20, 'Егор') #инициализация экземпляра класса
        """
        if not isinstance(sex, str):
            raise TypeError('Пол должен быть задан типом str')
        if not isinstance(age, int):
            raise TypeError('Возраст должен быть задан типом int')
        if not isinstance(name, str):
            raise TypeError('Имя должно быть задано типом str')
        if age < 0:
            raise ValueError('Возраст не может быть меньше нуля')
        self.sex = sex
        self.age = age
        self.name = name

    def birthday(self):
        """
        Функция увеличения возраста человека на год

        :return: Текущий возраст

        Пример:
        >>> human = Human('мужчина', 20, 'Егор')
        >>> human.birthday()
        """
        ...

    def name_changing(selfself, new_name: str):
        """
        Функция замены имени

        :param new_name: Новое имя
        :raise ValueError: Если имя не типа str, то вызываем ошибку

        Пример:
        >>> human = Human('мужчина', 20, 'Егор')
        >>> human.name_changing('Антон')
        """
        ...

if __name__ == "__main__":
    doctest.testmode() # TODO работоспособность экземпляров класса проверить с помощью doctest