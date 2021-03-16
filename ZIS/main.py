import modules.Staff as Staff
import modules.WildlifeInfo as WildlifeInfo
import modules.WildlifeCare as WildlifeCare
import modules.SalesInformation as SalesInformation
import modules.Giftshop as Giftshop
import website.CustomerLogin as CustomerLogin
import website.ZooInformation as ZooInformation
import website.AlterZooInformation as AlterZooInformation
import data.Database as Database

import os

def main():
    getUserInput("init")

def getUserInput(state):
    state = state.lower()
    clear = lambda: os.system('cls')
    if(state == "init"):
        clear()
        print("Welcome to the Zoo Information System")
        userInput = ""
        looping = True
        while looping:
            userInput = input("Input staff or website to start using the service: ")
            userInput = userInput.lower()
            if(userInput == "staff" or userInput == "website"):
                looping = False

        getUserInput(userInput)
    elif(state == "staff"):

        displayInfoValues = []
        displayInfoValues1 = []

        Outerloop = True
        while Outerloop:
            clear()

            displayInfoValues = ["staff", ""]
            displayInfo(displayInfoValues)

            userInput = input("Enter one of the above to use the service, or exit to return to the main menu, or close to exit completely ")
            if(str(userInput) == "exit"):
                getUserInput("init")
            elif(str(userInput) == "close"):
                clear()
                break
            displayInfoValues1 = ["checkKey", str(userInput)]
            if(displayInfo(displayInfoValues1)):
                Outerloop = False
                displayInfoValues = ["staff", str(userInput)]

                key = str(userInput)

                innerLoop = True
                while innerLoop:
                    clear()
                    displayInfo(displayInfoValues)
                    
                    userInput = input("Enter one of the above to use the service, or up to return to the menu above, or exit to return to the main menu, or close to exit completely ")
                    if(str(userInput) == "up"):
                        innerLoop = False
                        Outerloop = True
                    elif(str(userInput) == "exit"):
                        getUserInput("init")
                    elif(str(userInput) == "close"):
                        clear()
                        break

                    tempString = ""
                    for x, y in enumerate(userInput):
                        if(x == 0):
                            tempString += y.upper()
                        else:
                            tempString += y.lower()

                    userInput = tempString

                    displayInfoValues1 = ["checkValues", key, str(userInput)]
                    if(displayInfo(displayInfoValues1)):
                        clear()
                        methodInfoValues = ["staff", key, str(userInput)]
                        getMethod(methodInfoValues)
                        userInput = input("Enter next to do another task, up to go back one level, or exit to restart, or close to exit completely ")
                        if(str(userInput) == "next"):
                            pass
                        elif(str(userInput) == "up"):
                            innerLoop = False
                            Outerloop = True
                        elif(str(userInput) == "exit"):
                            getUserInput("init")
                        elif(str(userInput) == "close"):
                            clear()
                            break
        

def displayInfo(displayValue):
    staffPortalNames = ["Staff", "WildlifeInfo", "WildlifeCare", "SalesInformation", "GiftShop"]
    staffMethodNames = {"Staff": ["Look up staff","Modify staff info","Create staff","Get schedule","Create schedule","Modify schedule","Print schedule","Get tasks","Create tasks","Modify tasks","Print tasks"],
                        "WildlifeInfo": ["Look up animal","Modify wildlife info","Create wildlife info"],
                        "WildlifeCare": ["Get Animal info","Care routine","Create care routine","Modify care routine","Schedule","Print"],
                        "SalesInformation": ["Get ticket price","Set ticket price","Modify ticket price","Get customer information","Create customer information","Modify customer information","Create transaction","Receipt printout"],
                        "GiftShop": ["Display inventory","Modify inventory","Create inventory","Get customer information","Create customer information","Modify customer information","Create transaction","Receipt printout"]}

    if(displayValue[0] == "staff" and displayValue[1] == ""):
        for x in staffPortalNames:
            print(x)
    elif(displayValue[0] == "checkKey"):
        return displayValue[1] in staffPortalNames
    elif(displayValue[0] == "checkValues"):
        return displayValue[2] in staffMethodNames[displayValue[1]]
    elif(displayValue[0] == "staff" and displayValue[1] != ""):
        for x in staffMethodNames[displayValue[1]]:
            print(x)

def getMethod(methodInfo):
    db = Database
    staffPortalModules = {"Staff": Staff.Staff(db), 
                          "WildlifeInfo": WildlifeInfo.WildlifeInfo(db),
                          "WildlifeCare": WildlifeCare.WildlifeCare(db),
                          "SalesInformation": SalesInformation.SalesInformation(db),
                          "GiftShop": Giftshop.GiftShop(db)}
    webPortalModules = {"CustomerLogin": CustomerLogin.CustomerLogin(db),
                        "ZooInformation": ZooInformation.ZooInformation(db),
                        "AlterZooInformation": AlterZooInformation.AlterZooInformation(db)}

    if(methodInfo[0] == "staff"):
        if(methodInfo[1] == "Staff"):
            if(methodInfo[2] == "Look up staff"):
                staffPortalModules[methodInfo[1]].lookUpStaff()
            elif(methodInfo[2] == "Modify staff info"):
                staffPortalModules[methodInfo[1]].modifyStaffInfo()
            elif(methodInfo[2] == "Create staff"):
                staffPortalModules[methodInfo[1]].createStaff()
            elif(methodInfo[2] == "Get schedule"):
                staffPortalModules[methodInfo[1]].getSchedule()
            elif(methodInfo[2] == "Create schedule"):
                staffPortalModules[methodInfo[1]].createSchedule()
            elif(methodInfo[2] == "Modify schedule"):
                staffPortalModules[methodInfo[1]].modifySchedule()
            elif(methodInfo[2] == "Print schedule"):
                staffPortalModules[methodInfo[1]].printSchedule()
            elif(methodInfo[2] == "Get tasks"):
                staffPortalModules[methodInfo[1]].getTasks()
            elif(methodInfo[2] == "Create tasks"):
                staffPortalModules[methodInfo[1]].createTasks()
            elif(methodInfo[2] == "Modify tasks"):
                staffPortalModules[methodInfo[1]].modifyTasks()
            elif(methodInfo[2] == "Print tasks"):
                staffPortalModules[methodInfo[1]].printTasks()    
        elif(methodInfo[1] == "WildlifeInfo"):
            if(methodInfo[2] == "Look up animal"):
                staffPortalModules[methodInfo[1]].lookUp()
            elif(methodInfo[2] == "Modify wildlife info"):
                staffPortalModules[methodInfo[1]].modifyWildlifeInfo()
            elif(methodInfo[2] == "Create wildlife info"):
                staffPortalModules[methodInfo[1]].createWildlifeInfo()
        elif(methodInfo[1] == "WildlifeCare"):
            if(methodInfo[2] == "Get Animal info"):
                staffPortalModules[methodInfo[1]].animalInfo()
            elif(methodInfo[2] == "Care routine"):
                staffPortalModules[methodInfo[1]].careRoutine()
            elif(methodInfo[2] == "Create care routine"):
                staffPortalModules[methodInfo[1]].createCareRoutine()
            elif(methodInfo[2] == "Modify care routine"):
                staffPortalModules[methodInfo[1]].modifyCareRoutine()
            elif(methodInfo[2] == "Schedule"):
                staffPortalModules[methodInfo[1]].schedule()
            elif(methodInfo[2] == "Print"):
                staffPortalModules[methodInfo[1]].print()
        elif(methodInfo[1] == "SalesInformation"):
            if(methodInfo[2] == "Get ticket price"):
                staffPortalModules[methodInfo[1]].getTicketPrice()
            elif(methodInfo[2] == "Set ticket price"):
                staffPortalModules[methodInfo[1]].setTicketPrice()
            elif(methodInfo[2] == "Modify ticket price"):
                staffPortalModules[methodInfo[1]].modifyTicketPrice()
            elif(methodInfo[2] == "Get customer information"):
                staffPortalModules[methodInfo[1]].getCustomerInformation()
            elif(methodInfo[2] == "Create customer information"):
                staffPortalModules[methodInfo[1]].createCustomerInformation()
            elif(methodInfo[2] == "Modify customer information"):
                staffPortalModules[methodInfo[1]].modifyCustomerInformation()
            elif(methodInfo[2] == "Create transaction"):
                staffPortalModules[methodInfo[1]].createTransaction()
            elif(methodInfo[2] == "Receipt printout"):
                staffPortalModules[methodInfo[1]].receiptPrintout()
        elif(methodInfo[1] == "GiftShop"):
            if(methodInfo[2] == "Display inventory"):
                staffPortalModules[methodInfo[1]].displayInventory()
            elif(methodInfo[2] == "Modify inventory"):
                staffPortalModules[methodInfo[1]].modifyInventory()
            elif(methodInfo[2] == "Create inventory"):
                staffPortalModules[methodInfo[1]].createInventory()
            elif(methodInfo[2] == "Get customer information"):
                staffPortalModules[methodInfo[1]].getCustomerInformation()
            elif(methodInfo[2] == "Create customer information"):
                staffPortalModules[methodInfo[1]].createCustomerInformation()
            elif(methodInfo[2] == "Modify customer information"):
                staffPortalModules[methodInfo[1]].modifyCustomerInformation()
            elif(methodInfo[2] == "Create transaction"):
                staffPortalModules[methodInfo[1]].createTransaction()
            elif(methodInfo[2] == "Receipt printout"):
                staffPortalModules[methodInfo[1]].receiptPrintout()   
    elif(methodInfo[0] == "website"):
        pass

if __name__ == "__main__":
    main()