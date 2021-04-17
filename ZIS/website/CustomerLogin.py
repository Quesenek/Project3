import inspect
import random

#Created By: Marcus Taylor
#Date: 03-16-21

#CustomerLogin module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
class CustomerLogin:
    def __init__(self, database):
        super().__init__()
        self.db = database
        self.auth = False

    def authentication(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        print("Authenticate User")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        print("Authentication Successful")
        self.auth = True
        db.closeConnection()

    def getCustomerInfo(self):
        self.authentication()
        if(self.auth):
            db = self.db
            print(f"{inspect.stack()[0][3]} Method Accessed")
            db.connectDatabase()
            db.queryDatabase(f"{inspect.stack()[0][3]}")
            db.closeConnection()
        else:
            print("User not logged in")

    def modifyCustomerInfo(self):
        self.authentication()
        if(self.auth):
            nameList = ['Mark', 'Bobby', 'Angel', 'Stan']
            db = self.db
            print(f"{inspect.stack()[0][3]} Method Accessed")
            db.connectDatabase()
            db.executeDatabase(f"Alter information for customer {random.randint(1, 10000)} to {nameList[random.randint(0, 3)]}")
            db.closeConnection()
        else:
            print("User not logged in")

    def createCustomerInfo(self):
        self.authentication()
        if(self.auth):
            nameList = ['Mark', 'Bobby', 'Angel', 'Stan']
            db = self.db
            print(f"{inspect.stack()[0][3]} Method Accessed")
            db.connectDatabase()
            db.executeDatabase(f"Insert information for customer {random.randint(1, 10000)} to {nameList[random.randint(0, 3)]}")
            db.closeConnection()
        else:
            print("User not logged in")

        