from components import vars

def qAgain():
    print("Would you like to take the quiz again?")
    choice = input(" y / n ?")

    if choice == "n":
        print("============== Alright. Have a great day then !! ======================")
        exit()
        
    elif choice == "y":
        print("---------------------------  OKAY! ------------------------------------")
        print("=======================================================================")
        print("                        LET THE QUIZ BEGIN !!                        ")
        print("=======================================================================")

        vars.quizTotal = False
