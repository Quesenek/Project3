import inspect
import random

#Created By: Marcus Taylor
#Date: 03-16-21

#ZooInformation module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
class ZooInformation:
    def __init__(self, database):
        super().__init__()
        self.db = database

    def currentEvents(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def publicMessage(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def operatingHours(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def wildlifeInformation(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()