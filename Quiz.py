from guizero import *
import json

file = open("QuizAnswers.json")
data = json.load(file)["Doppler Effect Quiz"]
questioncounter = 0
score = 0
app = App(title="Physics Quiz")

def endoftest():
    title.value = f"Score: {score}/{len(data)}"
    question.visible = False
    answerbox.visible = False
    submitbutton.text= "Exit"
    submitbutton._command = quit


def checkanswer():
    global questioncounter
    if questioncounter < len(data)-1:
        questioncounter += 1
        title.value = f"Question {questioncounter+1}"
        question.value = data[questioncounter]["question"]
    else:
        endoftest()
        

title = Text(app, text=f"Question {questioncounter+1}", size=64)
filler1 = Text(app,text="",size=32)
question = Text(app, text=data[questioncounter]["question"], size=32)
filler2 = Text(app,text="",size=32)
answerbox = TextBox(app, width=32)
filler3 = Text(app,text="",size=32)
submitbutton = PushButton(app, text="Submit", command=checkanswer)

app.display()