"""FACTORY METHOD DB EXAMPLE"""
from typing import Literal
from abc import ABC, abstractmethod
from mysql import connector


#   For more databases
class DB(ABC):
    """PRODUCT"""

    @abstractmethod
    def connect(self, host: str, user: str, password: str, database: str):
        """ABSTRACT CONNECT METHOD"""

    @abstractmethod
    def disconnect(self):
        """ABSTRACT DISCONNECT METHOD"""


class MysqlDB(DB):
    """CONCRETE PRODUCT MYSQL"""

    def __init__(self) -> None:
        self.connector = connector

    def connect(self, host: str, user: str, password: str, database: str):
        self.connector.connect(
            host=host, user=user, password=password, database=database
        )
        print("Connected")

    def disconnect(self):
        self.disconnect()
        print("Disconnected")


class Creator(ABC):
    """ABSTRACT FACTORY CLASS"""

    @abstractmethod
    def factory_method(self):
        """ABSTRACT FACTORY METHOD"""


class MysqlDBCreator(Creator):
    """MYSQL DB CREATOR"""

    def factory_method(self):
        return MysqlDB()


class ConcreteCreator(Creator):
    """DIRECTOR CLASS"""

    def get_db(self, product: Literal["mysql"]):
        """GET PRODUCT METHOD"""
        return self.factory_method(product=product)

    def factory_method(self, product: str):
        if product == "mysql":
            return MysqlDBCreator().factory_method()
        print("That's not a db")


if __name__ == "__main__":
    factory = ConcreteCreator()
    mysql_db = factory.get_db("mysql")
    mysql_db.connect()
    mysql_db.disconnect()
