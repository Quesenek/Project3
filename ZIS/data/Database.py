import inspect

#Created By: Marcus Taylor
#Date: 03-16-21

#Database module, skeleton structure
#inspect allows for the method name to be sent to be printed
#Methods defined will mostly be used to connect and pull information from the database to be used, other methods to fully implement features unknown
def connectDatabase():
    print(f"{inspect.stack()[0][3]} Method Accessed")
def executeDatabase(input):
    print(f"({inspect.stack()[0][3]} accessed) Executing: {input}")
def queryDatabase(input):
    print(f"({inspect.stack()[0][3]} accessed) Query: {input}")
def closeConnection():
    print(f"{inspect.stack()[0][3]} Method Accessed")