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

        looping = True
        while looping:
            clear()

            displayInfoValues = ["staff", ""]
            displayInfo(displayInfoValues)

            userInput = input("Enter one of the above to use the service, or exit to return to the main menu ")
            if(userInput == "exit"):
                getUserInput("init")
            displayInfoValues1 = ["check", str(userInput)]
            if(displayInfo(displayInfoValues1)):
                looping = False
                print("entered")
                displayInfoValues = ["staff", userInput]
        displayInfo(displayInfoValues)

def displayInfo(displayValue):
    staffPortalNames = ["Staff", "WildlifeInfo", "WildlifeCare", "SalesInformation", "GiftShop"]
    # staffMethodNames = {"Staff": ["lookUpStaff","modifyStaffInfo","createStaff","getSchedule","createSchedule","modifySchedule","printSchedule","getTasks","createTasks","modifyTasks","printTasks"],
    #                     "WildlifeInfo": ["lookUp","modifyWildlifeInfo","createWildlifeInfo"],
    #                     "WildlifeCare": ["animalInfo","careRoutine","createCareRoutine","modifyCareRoutine","schedule","print"],
    #                     "SalesInformation": ["getTicketPrice","setTicketPrice","modifyTicketPrice","getCustomerInformation","createCustomerInformation","modifyCustomerInformation","createTransaction","receiptPrintout"],
    #                     "GiftShop": ["displayInventory","modifyInventory","createInventory","getCustomerInformation","createCustomerInformation","modifyCustomerInformation","CreateTransaction","receiptPrintout"]}
    staffMethodNames = {"Staff": ["Look up staff","Modify staff info","Create staff","Get schedule","Create schedule","Modify schedule","Print schedule","Get tasks","Create tasks","Modify tasks","Print tasks"],
                        "WildlifeInfo": ["Look up animal","Modify wildlife info","Create wildlife info"],
                        "WildlifeCare": ["Get Animal info","Care routine","Create care routine","Modify care routine","Schedule","Print"],
                        "SalesInformation": ["Get ticket price","Set ticket price","Modify ticket price","Get customer information","Create customer information","Modify customer information","Create transaction","Receipt printout"],
                        "GiftShop": ["Display inventory","Modify inventory","Create inventory","Get customer information","Create customer information","Modify customer information","Create transaction","Receipt printout"]}

    displayValue[0] = displayValue[0].lower()
    print(f"{displayValue[0]} {displayValue[1]}")

    if(displayValue[0] == "staff" and displayValue[1] == ""):
        for x in staffPortalNames:
            print(x)
    elif(displayValue[0] == "check"):
        return displayValue[1] in staffPortalNames
    elif(displayValue[0] == "staff" and displayValue[1] != ""):
        for x in staffMethodNames[displayValue[1]]:
            print(x)
        print("Modify inventory" in staffMethodNames["GiftShop"])

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
    elif(methodInfo[0] == "website"):
        pass

if __name__ == "__main__":
    main()