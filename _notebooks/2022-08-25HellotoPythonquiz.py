# Python Vocabulary Quiz

import getpass, sys
from tkinter import Y

def question_and_answer(prompt):
    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)
    
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 6
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("What command is used to include other functions that are developed?")
if rsp == "import":
    print(rsp + " is correct :)")
    correct += 1
else:
    print(rsp + " is incorrect:(")

rsp = question_with_response("What command in this example is used to evaluate a response?")
if rsp == "if":
    print(rsp + " is correct :)")
    correct += 1
else:
    print(rsp + " is incorrect :(")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct :)")
    correct += 1
else:
    print(rsp + " is incorrect :(")

rsp = question_with_response("To use Static Text, what is the command or function?") 
if rsp == "print()":
    print(rsp + "is correct :)")
    correct += 1
else:
    print(rsp + "is incorrect :(")

rsp = question_with_response("What is the key word that defines a function, in Python?")
if rsp == "def":
    print (rsp + " is correct :)")
    correct += 1
else:
    print(rsp + " is incorrect :(")
    
rsp = question_with_response("What turns number into string?")
if rsp == "function str()":
    print (rsp + "is correct :)")
    correct += 1
else:
    print(rsp + "is incorrect :(") 

print(getpass.getuser() + " great job! you scored " + str(correct) +"/" + str(questions))