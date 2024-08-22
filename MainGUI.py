from guizero import *
import json

file = open("Logins.json")
data = json.load(file)["Credentials"]

app = App(title="PhysicsGo")
app.set_full_screen()

def loginchecker(username, password):
    if username.value == data[0]["Username"] and password.value == data[0]["Password"]:
        loginresponse.value = "Teacher logged in"
    elif username.value == data[1]["Username"] and password.value == data[1]["Password"]:
        loginresponse.value = "Student logged in"
    else:
        loginresponse.value = "Incorrect username or password"

def loginscreen():
    global loginresponse
    title = Text(app, text="Welcome to PhysicsGo!", size=72)
    fillertextb = Text(app, text="", size=50)
    usernametext = Text(app, text="Username")
    usernamebox = TextBox(app, width=25)
    fillertextc = Text(app, text="")
    passwordtext = Text(app, text="Password")
    passwordbox = TextBox(app, width=25, hide_text=True)
    fillertextf = Text(app, text="")
    loginresponse = Text(app, text="")
    fillertextd = Text(app, text="")
    enterbutton = PushButton(app, text="Log In", command=loginchecker, args=[usernamebox, passwordbox])
    fillertexte = Text(app, text="", size=64)
    exitbutton = PushButton(app, text="Exit", command=quit)

loginscreen()

app.display()