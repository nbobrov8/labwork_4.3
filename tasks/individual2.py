#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


"""
Создать абстрактный базовый класс Figure с абстрактными методами вычисления площади
и периметра. Создать производные классы: Rectanglе (прямоугольник), Circle (круг),
Trapezium (трапеция) со своими функциями площади и периметра. Самостоятельно
определить, какие поля необходимы, какие из них можно задать в базовом классе, а какие —
в производных.
"""


class Figure(ABC):

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Rectangle(Figure):
    def square(self, a, b):
        print("Площадь прямоугольника: ", a * b)

    def perimetr(self, a, b):
        print("Периметр прямоугольника: ", 2 * (a + b))


class Circle(Figure):
    def square(self, b, h):
        print("Площадь треугольника: ", 0.5 * b * h)

    def perimetr(self, a, b, c):
        print("Периметр треугольника: ", a + b + c)

class Trapezium(Figure):
    def square(self, a, b, h):
        print("Площадь трапеции: ", (a + b) * h / 2)

    def perimetr(self, a, b, c, d):
        print("Периметр трапеции: ", a + b + c + d)


def main():
    r1 = Rectangle()
    r1.square(2, 5)
    r1.perimetr(3, 2)

    c1 = Circle()
    c1.square(4, 6)
    c1.perimetr(1, 4, 3)

    t1 = Trapezium()
    t1.square(4, 8, 2)
    t1.perimetr(2, 4, 6, 7)


if __name__ == "__main__":
    main()