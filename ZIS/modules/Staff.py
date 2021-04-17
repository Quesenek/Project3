import inspect
from randomuser import RandomUser
import os

#Created By: Marcus Taylor
#Date: 03-16-21

#Staff module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
class Staff:
    
    def __init__(self, database):
        super().__init__()
        self.db = database

    def lookUpStaff(self):
        clear = lambda: os.system('cls')
        db = self.db
        print(f"{inspect.stack()[0][3]} Method Accessed")
        db.connectDatabase()
        db.queryDatabase(f"{inspect.stack()[0][3]}")
        db.closeConnection()
        self.getStaff(clear)
    
    def getStaff(self, clear):
        user_list = RandomUser.generate_users(10, {'nat': 'us'})
        RandomUser.get_first_name
        for x in user_list:
            print(x.get_full_name())

        outerLoop = True
        while outerLoop:
            userInput = input("Enter the name in (format: first last ) to look up info: exit to restart, or close to exit completely ")
            
            stringSplit = userInput.split(" ")

            for x in user_list:
                if(x.get_first_name().lower() == stringSplit[0].lower() and x.get_last_name().lower() == stringSplit[1].lower()):
                    clear()
                    print(f"Name: {x.get_full_name()}\nDOB: {x.get_dob()[:10]}\nID: {x.get_id()}\nPhone: {x.get_phone()}\nAddress: {x.get_street()}\nState: FL\n")

            
            userInput1 = input("Enter next to query another staff member or exit to restart, or close to exit completely ")
            if(str(userInput) == "exit"):
                break
            elif(str(userInput) == "close"):
                clear()
                break
            if(str(userInput1) == "next"):
                clear()
                for x in user_list:
                    print(x.get_full_name())

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
        print(f"Printing the schedule based on: getSchedule()")

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
        print(f"Printing the tasks based on: getTasks()")