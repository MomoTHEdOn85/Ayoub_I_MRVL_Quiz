from components.quizQuestions import questions
from components import vars

def display():

    print("\033[1;37;40m ----------------------------------------------------\n")

    ans1 = questions["q1"][input(questions["q1"]["question"])]
    print(ans1)
    vars.quizTotal += ans1
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans2 = questions["q2"][input(questions["q2"]["question"])]
    print(ans2)
    vars.quizTotal += ans2
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans3 = questions["q3"][input(questions["q3"]["question"])]
    print(ans3)
    vars.quizTotal += ans3
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans4 = questions["q4"][input(questions["q4"]["question"])]
    print(ans4)
    vars.quizTotal += ans4
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans5 = questions["q5"][input(questions["q5"]["question"])]
    print(ans5)
    vars.quizTotal += ans5
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    ans6 = questions["q6"][input(questions["q6"]["question"])]
    print(ans6)
    vars.quizTotal += ans6
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans7 = questions["q7"][input(questions["q7"]["question"])]
    print(ans7)
    vars.quizTotal += ans7
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans8 = questions["q8"][input(questions["q8"]["question"])]
    print(ans8)
    vars.quizTotal += ans8
    print("\033[1;37;40m ----------------------------------------------------\n")
    
    
    ans9 = questions["q9"][input(questions["q9"]["question"])]
    print(ans9)
    vars.quizTotal += ans9
    print("\033[1;37;40m ----------------------------------------------------\n")

    ans10 = questions["q10"][input(questions["q10"]["question"])]
    print(ans10)
    vars.quizTotal += ans10
    print("\033[1;37;40m ----------------------------------------------------\n")


