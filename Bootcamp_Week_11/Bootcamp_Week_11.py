
# Practice coding

class ValueOutOfRange(Exception):
    pass

def Menu(menuOptions): # Dynamic menu
                
    isValid = False

    while isValid == False:
    
        print(menuOptions[0] + "\n")
        
        for x in range(1, len(menuOptions)):

            print(str(x) + ": " + menuOptions[x])

        try:

            userChoice = int(input("\nPlease make a selection from the list provided: "))

            if userChoice < 1 or userChoice > (len(menuOptions) - 1):

                raise ValueOutOfRange

        except ValueOutOfRange:

            input("\nPlease enter a valid option from the list, please press enter and try again...")

        except ValueError:

            input("\nPlease enter a valid whole number, please press enter and try again...")

        except:

            input("\nAn unknown error has occured, please press enter and try again...")

        else:

            isValid = True


    return userChoice

def Main(): # Function for main body of code
    
    menuOptions = ["------Menu------", "Start", "Save", "Load", "Exit"]

    bLoop = True

    while bLoop == True:

        userChoice = Menu(menuOptions)

        if userChoice == 1: # Start

            print("\nYou have selected Start\n")

        elif userChoice == 2: # Save
            
            print("\nYou have selected Save\n")

        elif userChoice == 3: # Load
            
            print("\nYou have selected Load\n")

        else: # Exit
                        
            print("\nYou have selected Exit\n")
            
            bLoop = False 

Main() # Run the main body of code
