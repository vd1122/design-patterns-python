"""
Creational Pattern --> Factory Pattern

Create factory of different source types and let class calling method decide which source type to invoke
"""

from abc import ABC, abstractmethod

class Database(ABC):
   @abstractmethod
   def connection(self):
        pass

class MySql:
    def connection(self):
        return('Invoking MySql connection')


class Postgres:
    def connection(self):
        return('Invoking Postgres connection')


class DbFactory:
    def get_database_connection(self, database):
        if database == 'mysql':
            return MySql().connection()

        if database == 'postgres':
            return Postgres().connection()

factory = DbFactory()
print(factory.get_database_connection('mysql'))
print(factory.get_database_connection('postgres'))
