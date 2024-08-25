from guizero import *
import json

def endoftest():
    #displays the score, removes most elements and changest the submit button to an exit button
    title.value = f"Score: {score}/{len(data)}"
    question.visible = False
    answerbox.visible = False
    submitbutton.text= "Exit"
    submitbutton._command = quizwindow.destroy


def checkanswer():
    global questioncounter, score
    #checks if the answer is correct
    if answerbox.value.lower() == data[questioncounter]["answer"].lower():
        score += 1
        answerresponse.value = "Correct!"
    else:
        #displays correct answer if the wrong one was input
        answerresponse.value = (f"Incorrect, the answer is: {data[questioncounter]['answer']}")
    #checks if it is the end of the quiz 
    if questioncounter < len(data)-1:
        #moves onto the next question
        answerbox.value = ""
        questioncounter += 1
        title.value = f"Question {questioncounter+1}"
        question.value = data[questioncounter]["question"]
    else:
        #triggers the end of the quiz
        endoftest()

def main(quizname, master):   
    global answerbox, answerresponse, title, data, submitbutton, questioncounter, score, question, quizwindow
    #loads the json file with the questions and answers
    file = open("QuizAnswers.json")
    data = json.load(file)[quizname]

    #initialises the key variables
    questioncounter = 0
    score = 0
    quizwindow = Window(master, title="Physics Quiz")
    quizwindow.set_full_screen()

    #intialises all the interactive and text elements in order
    title = Text(quizwindow, text=f"Question {questioncounter+1}", size=64)
    filler1 = Text(quizwindow,text="",size=32)
    question = Text(quizwindow, text=data[questioncounter]["question"], size=32)
    filler2 = Text(quizwindow,text="",size=32)
    answerbox = TextBox(quizwindow, width=32)
    filler3 = Text(quizwindow,text="",size=32)
    submitbutton = PushButton(quizwindow, text="Submit", command=checkanswer)
    filler4 = Text(quizwindow,text="",size=32)
    answerresponse = Text(quizwindow, text="", size=32)