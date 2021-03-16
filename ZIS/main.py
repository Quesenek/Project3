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

#Created By: Marcus Taylor
#Date: 03-16-21

#Initial iteration of the ZIS by Marcus Taylor: implemented using command line interaction with the skeleton structure

#Simple main method for the application start
def main():
    getUserInput("init")

#This method controls the state of the user interaction and changes depending on the entered information
def getUserInput(state):
    #Change state values to lower case and initialize clear to the os command
    state = state.lower()
    clear = lambda: os.system('cls')

    #Initializes the loop and starts the application
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
        portalInteraction("staff", state, clear)
    
    elif(state == "website"):
        portalInteraction("website", state, clear)
        
#Object oriented implementation for code reusage.
#This method is the program loop when a state is entered for either staff or website
def portalInteraction(name, state, clear):
    #Lists that will hold values for sending to the displayInfo method
    displayInfoValues = []
    displayInfoValues1 = []

    #loop control boolean, start of the main loop
    Outerloop = True
    while Outerloop:
        #Clean up the console while using the menu, works on windows
        clear()

        #Displays the module names
        displayInfoValues = [name, ""]
        displayInfo(displayInfoValues, state)

        #User input to select the module the user wants to use, Case Sensitive
        #Along with getting the user input for the module, the structure allows for the navigation of the menu when available
        userInput = input("Enter one of the above to use the service, or exit to return to the main menu, or close to exit completely ")
        if(str(userInput) == "exit"):
            getUserInput("init")
        elif(str(userInput) == "close"):
            clear()
            break
        #Check if module is in the list, if it is, the next stage is entered
        displayInfoValues1 = ["checkKey", str(userInput)]
        if(displayInfo(displayInfoValues1, state)):
            #Loop control structure, by changing these values the menus can be traversed up and down
            Outerloop = False
            #Display the methods for the chosen module
            displayInfoValues = [name, str(userInput)]

            #The current module that is chosen is assigned to a key value for the dictionary
            key = str(userInput)
            #Loop control value
            innerLoop = True
            #The inner loop allows for the user to stay within the methods for the module without exiting out unless specified in the input
            while innerLoop:
                #Clean console and display methods for the active module
                clear()
                displayInfo(displayInfoValues, state)
                
                #Menu interaction
                userInput = input("Enter one of the above to use the service, or up to return to the menu above, or exit to return to the main menu, or close to exit completely ")
                if(str(userInput) == "up"):
                    innerLoop = False
                    Outerloop = True
                elif(str(userInput) == "exit"):
                    getUserInput("init")
                elif(str(userInput) == "close"):
                    clear()
                    break
                #Because the methods were turned into plain text versions of the methods so that they were clearer to the user this for loop takes any input and changes it to the correct case
                #By using enumerate(somelist) the index of the current value is also provided along with the current value within two variables
                tempString = ""
                for x, y in enumerate(userInput):
                    if(x == 0):
                        tempString += y.upper()
                    else:
                        tempString += y.lower()

                userInput = tempString
                #Check value for accuracy, if the value is accurate it is sent to the module method translation method where the method is called
                displayInfoValues1 = ["checkValues", key, str(userInput)]
                if(displayInfo(displayInfoValues1, state)):
                    clear()
                    methodInfoValues = [name, key, str(userInput)]
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

# This method has lists/dictionaries that display their contents based on user input
def displayInfo(displayValue, portal):
    staffPortalNames = ["Staff", "WildlifeInfo", "WildlifeCare", "SalesInformation", "GiftShop"]
    staffMethodNames = {"Staff": ["Look up staff","Modify staff info","Create staff","Get schedule","Create schedule","Modify schedule","Print schedule","Get tasks","Create tasks","Modify tasks","Print tasks"],
                        "WildlifeInfo": ["Look up animal","Modify wildlife info","Create wildlife info"],
                        "WildlifeCare": ["Get Animal info","Care routine","Create care routine","Modify care routine","Schedule","Print"],
                        "SalesInformation": ["Get ticket price","Set ticket price","Modify ticket price","Get customer information","Create customer information","Modify customer information","Create transaction","Receipt printout"],
                        "GiftShop": ["Display inventory","Modify inventory","Create inventory","Get customer information","Create customer information","Modify customer information","Create transaction","Receipt printout"]}

    websitePortalNames = ["CustomerLogin", "ZooInformation", "AlterZooInformation"]
    websiteMethodNames = {"CustomerLogin": ["Authentication", "Get customer info", "Modify customer info", "Create customer info"],
                          "ZooInformation": ["Current events", "Public message", "Operating hours", "Wildlife information"],
                          "AlterZooInformation": ["Create current events", "Modify current events", "Create public message", "Modify public message", "Create operating hours", "Modify operating hours"]}

    if(portal == "staff"):
        #Based on the current state of the software the output will be displayed for the module name, or the method names
        if(displayValue[0] == "staff" and displayValue[1] == ""):
            for x in staffPortalNames:
                print(x)
        elif(displayValue[0] == "staff" and displayValue[1] != ""):
            for x in staffMethodNames[displayValue[1]]:
                print(x)
        #Methods to check if the value is in the list or dictionary
        elif(displayValue[0] == "checkKey"):
            return displayValue[1] in staffPortalNames
        elif(displayValue[0] == "checkValues"):
            return displayValue[2] in staffMethodNames[displayValue[1]]

    elif(portal == "website"):
        #Based on the current state of the software the output will be displayed for the module name, or the method names
        if(displayValue[0] == "website" and displayValue[1] == ""):
            for x in websitePortalNames:
                print(x)
        elif(displayValue[0] == "website" and displayValue[1] != ""):
            for x in websiteMethodNames[displayValue[1]]:
                print(x)
        #Methods to check if the value is in the list or dictionary        
        elif(displayValue[0] == "checkKey"):
            return displayValue[1] in websitePortalNames
        elif(displayValue[0] == "checkValues"):
            return displayValue[2] in websiteMethodNames[displayValue[1]]
        
# This gets sent the information that the user wants to access for the methods of each module.  It translates the plain text into the corresponding method
def getMethod(methodInfo):
    db = Database

    # dictionaries of the different modules to allow for object oriented implementation
    staffPortalModules = {"Staff": Staff.Staff(db), 
                          "WildlifeInfo": WildlifeInfo.WildlifeInfo(db),
                          "WildlifeCare": WildlifeCare.WildlifeCare(db),
                          "SalesInformation": SalesInformation.SalesInformation(db),
                          "GiftShop": Giftshop.GiftShop(db)}
    webPortalModules = {"CustomerLogin": CustomerLogin.CustomerLogin(db),
                        "ZooInformation": ZooInformation.ZooInformation(db),
                        "AlterZooInformation": AlterZooInformation.AlterZooInformation(db)}

    #Values for methodInfo are [Portal, Key, Value]
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
        if(methodInfo[1] == "CustomerLogin"):
            if(methodInfo[2] == "Authentication"):
                webPortalModules[methodInfo[1]].authentication()
            elif(methodInfo[2] == "Get customer info"):
                webPortalModules[methodInfo[1]].getCustomerInfo()
            elif(methodInfo[2] == "Modify customer info"):
                webPortalModules[methodInfo[1]].modifyCustomerInfo()
            elif(methodInfo[2] == "Create customer info"):
                webPortalModules[methodInfo[1]].createCustomerInfo()
        elif(methodInfo[1] == "ZooInformation"):
            if(methodInfo[2] == "Current events"):
                webPortalModules[methodInfo[1]].currentEvents()
            elif(methodInfo[2] == "Public message"):
                webPortalModules[methodInfo[1]].publicMessage()
            elif(methodInfo[2] == "Operating hours"):
                webPortalModules[methodInfo[1]].operatingHours()
            elif(methodInfo[2] == "Wildlife information"):
                webPortalModules[methodInfo[1]].wildlifeInformation()
        elif(methodInfo[1] == "AlterZooInformation"):
            if(methodInfo[2] == "Create current events"):
                webPortalModules[methodInfo[1]].createCurrentEvents()
            elif(methodInfo[2] == "Modify current events"):
                webPortalModules[methodInfo[1]].modifyCurrentEvents()
            elif(methodInfo[2] == "Create public message"):
                webPortalModules[methodInfo[1]].createPublicMessage()
            elif(methodInfo[2] == "Modify public message"):
                webPortalModules[methodInfo[1]].modifyPublicMessage()
            elif(methodInfo[2] == "Create operating hours"):
                webPortalModules[methodInfo[1]].createOperatingHours()
            elif(methodInfo[2] == "Modify operating hours"):
                webPortalModules[methodInfo[1]].modifyOperatingHours()
            

if __name__ == "__main__":
    main()