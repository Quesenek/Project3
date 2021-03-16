import inspect
import random

class GiftShop:
    def __init__(self, database):
        super().__init__()
        self.db = database

    def displayInventory(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def modifyInventory(self):
        itemList = ['KeyChain', 'Stuffed Animal', 'Animal Art', 'Candy']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Altered item price of {itemList[random.randint(0, 3)]} to {random.randint(1, 10)}")
        db.closeConnection()

    def createInventory(self):
        itemList = ['KeyChain', 'Stuffed Animal', 'Animal Art', 'Candy']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert new {itemList[random.randint(0,3)]} into database")
        db.closeConnection()

    def getCustomerInformation(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    #Name changed from setCustomerInformation to createCustomerInformation.  setCustomerInformation was a confusing name because it was too close in meaning to modifyCustomerInformation
    def createCustomerInformation(self):
        nameList = ['Mark', 'Bobby', 'Angel', 'Stan']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert information for customer {random.randint(1, 10000)} to {nameList[random.randint(0, 3)]}")
        db.closeConnection()

    def modifyCustomerInformation(self):
        nameList = ['Mark', 'Bobby', 'Angel', 'Stan']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Alter information for customer {random.randint(1, 10000)} to {nameList[random.randint(0, 3)]}")
        db.closeConnection()

    def createTransaction(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Create new transaction for order number {random.randint(1, 1000)}")
        db.closeConnection()

        self.receiptPrintout()

    def receiptPrintout(self):
        print(f"{inspect.stack()[0][3]} Method Accessed")