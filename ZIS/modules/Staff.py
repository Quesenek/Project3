import inspect

class Staff:
    
    def __init__(self, database):
        super().__init__()
        self.db = database

    def lookUpStaff(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def modifyStaffInfo(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase("Change staff")
        db.closeConnection()

    def createStaff(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase("Insert new Staff")
        db.closeConnection()

    def getSchedule(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def createSchedule(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase("Insert new schedule")
        db.closeConnection()

    def modifySchedule(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase("Change schedule")
        db.closeConnection()

    def printSchedule(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        print(f"Printing the schedule based on: {self.printSchedule()}")

    def getTasks(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()

    def createTasks(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase("Insert new task")
        db.closeConnection()

    def modifyTasks(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.executeDatabase("Change task")
        db.closeConnection()

    def printTasks(self):
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        print(f"Printing the tasks based on: {self.getTasks()}")