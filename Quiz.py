from guizero import *

app = App(title="Physics Quiz")

title = Text(app, text="Question 1", size=64)
filler1 = Text(app,text="",size=32)
question = Text(app, text="Insert Question Here", size=32)
filler2 = Text(app,text="",size=32)
answerbox = TextBox(app, width=32)
filler3 = Text(app,text="",size=32)
submitbutton = PushButton(app, text="Submit")

app.display()