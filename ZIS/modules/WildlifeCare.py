import inspect
import random

#Created By: Marcus Taylor
#Date: 03-16-21

#WildlifeCare module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
class WildlifeCare:
    def __init__(self, database):
        super().__init__()
        self.db = database

    def animalInfo(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def careRoutine(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def createCareRoutine(self):
        animalList = ['Monkey', 'Zebra', 'Elephant', 'Giraffe']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert new {animalList[random.randint(0,3)]} with id {random.randint(1, 10)}")
        db.closeConnection()

    def modifyCareRoutine(self):
        animalList = ['Monkey', 'Zebra', 'Elephant', 'Giraffe']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Alter information for {animalList[random.randint(0, 3)]} with id {random.randint(1, 10)}")
        db.closeConnection()

    def schedule(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def print(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        print(f"Printing the animal information based on: animalInfo()")