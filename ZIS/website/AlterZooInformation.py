import inspect
import random

#Created By: Marcus Taylor
#Date: 03-16-21

#AlterZooInformation module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
class AlterZooInformation:
    def __init__(self, database):
        super().__init__()
        self.db = database

    def createCurrentEvents(self):
        eventList = ['Half Off Week', 'Fall Festival']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert information for event {eventList[random.randint(0, 1)]}")
        db.closeConnection()

    def modifyCurrentEvents(self):
        eventList = ['Half Off Week', 'Fall Festival']
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Alter information for {eventList[random.randint(0, 1)]}")
        db.closeConnection()

    def createPublicMessage(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert information for new public message")
        db.closeConnection()

    def modifyPublicMessage(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Alter information for public message")
        db.closeConnection()

    def createOperatingHours(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Insert information for new operating hours")
        db.closeConnection()

    def modifyOperatingHours(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase(f"Alter information for operating hours")
        db.closeConnection()