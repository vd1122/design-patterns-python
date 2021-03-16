
"""
Creational Pattern --> Singleton Pattern
This pattern limits class creation to one object only.
"""

class Singleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# obj1 and obj2 is referring to same object
# ----------------------------------------
obj1 = Singleton()
obj2 = Singleton()

assert (id(obj1) == id(obj2))
