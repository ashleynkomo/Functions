#Ashley Nkomo
#Functions_Improvement Exercise
#27-11-2014

import random

def question():
    print("Times-table tester")
    print()
    
def choice():
    testTable = int(input("Which times-table do you want to be tested on? "))
    return testTable

def response(UserAnswer,Ans):
    if UserAnswer == Ans:
        print("Well done, you got the correct answer!")
        print()
    else:
        print("Sorry, you got the answer wrong. The correct answer is".format(Ans))
        print()

def answer(Num1, Num2):
        UserAnswer = int(input("{0} x {1} = ? ".format(Num1,Num2)))
        UserAnswer = int(UserAnswer)
        return UserAnswer
    
def number(testTable):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    return Num1, Num2
    
def generate_questions():
    question()
    testTable = choice()
    for macaroni in range(1,6):
        Num1, Num2 = number(testTable)
        Ans = Num1 * Num2
        UserAnswer = answer(Num1,Num2)
        response(UserAnswer,Ans)
    
    
    
#main program
generate_questions()
