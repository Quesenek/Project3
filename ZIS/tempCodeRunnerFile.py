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