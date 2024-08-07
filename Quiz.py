from guizero import *
import json

file = open("QuizAnswers.json")
data = json.load(file)["Doppler Effect Quiz"]
questioncounter = 0

app = App(title="Physics Quiz")

title = Text(app, text=f"Question {questioncounter+1}", size=64)
filler1 = Text(app,text="",size=32)
question = Text(app, text=data[questioncounter]["question"], size=32)
filler2 = Text(app,text="",size=32)
answerbox = TextBox(app, width=32)
filler3 = Text(app,text="",size=32)
submitbutton = PushButton(app, text="Submit")

app.display()