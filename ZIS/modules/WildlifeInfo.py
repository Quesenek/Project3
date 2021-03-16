import inspect
import random

#Created By: Marcus Taylor
#Date: 03-16-21

#WildlifeInfo module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
class WildlifeInfo:
    def __init__(self, database):
        super().__init__()
        self.db = database

    def lookUp(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def modifyWildlifeInfo(self):
        animalList = ['Monkey', 'Zebra', 'Elephant', 'Giraffe']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Alter information for {animalList[random.randint(0, 3)]} with id {random.randint(1, 10)}")
        db.closeConnection()

    def createWildlifeInfo(self):
        animalList = ['Monkey', 'Zebra', 'Elephant', 'Giraffe']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert new {animalList[random.randint(0,3)]} with id {random.randint(1, 10)}")
        db.closeConnection()
