#!/usr/bin/env python

"""
Structural Pattern --> Facade Pattern

This pattern present unified class to the client, hiding action/item specific complexity with the client
"""

class Exercise:
    def exercise(self):
        Yoga().exercise()
        Running().exercise()
        Weights().exercise()


class Yoga:
    def exercise(self):
        print("Yoga breathing 5 mins...")
        print("Yoga aasanas 15 mins...")


class Running:
    def exercise(self):
        print("Running slowly 15 mins...")
        print("Running fast 5 mins...")


class Weights:
    def exercise(self):
        print("Upper section 15 mins...")
        print("Mid section fast 5 mins...")
        print("Lower section fast 15 mins...")


if __name__ == "__main__":
    Exercise().exercise()

