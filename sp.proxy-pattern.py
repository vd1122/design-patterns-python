#!/usr/bin/env python

"""
Structural Pattern --> Proxy Pattern

This pattern is used to extend functionality of existing class by creating new proxy class
"""
class BoozeTime:
    def drink_time(self, drinker_name):
        print (f"{drinker_name} enjoy booze.")


class BoozeTimeProxy(BoozeTime):
    legal_age_for_drinking = 18

    def __init__(self, drinker_name, drinker_age):
        self.drinker_name = drinker_name
        self.drinker_age = drinker_age

    def drink_time(self):
        if (self.drinker_age > 18):
            super().drink_time(self.drinker_name)
        else:
            print (f"{self.drinker_name} under age drinking not allowed.")


# under age for drinking
bzp = BoozeTimeProxy("Joe", 17).drink_time()

# legal drinking
bzp = BoozeTimeProxy("Jane", 21).drink_time()
