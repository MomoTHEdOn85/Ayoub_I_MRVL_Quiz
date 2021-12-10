from components import vars, quizTally, quizAgain, quizDisplay

print("\033[1;31;40m =======================================================================")
print("                             LET THE QUIZ BEGIN !!                        ")
print("\033[1;31;40m =======================================================================")


while vars.quizTotal is 0:

    quizDisplay.display();
    
    print("Total so far: " + str(vars.quizTotal) + "\n")
    
    
    # Logic for character reveal after all the questions are answered
    quizTally.total(vars.quizTotal)

    quizAgain.qAgain();

    vars.quizTotal = 0