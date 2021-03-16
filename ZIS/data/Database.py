import inspect

def connectDatabase():
    print(f"{inspect.stack()[0][3]} Method Accessed")
def executeDatabase(input):
    print(f"({inspect.stack()[0][3]} accessed) Executing: {input}")
def queryDatabase(input):
    print(f"({inspect.stack()[0][3]} accessed) Query: {input}")
def closeConnection():
    print(f"{inspect.stack()[0][3]} Method Accessed")