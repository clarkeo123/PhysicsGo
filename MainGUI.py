from guizero import *

app = App(title="PhysicsGo")
app.set_full_screen()

def loginscreen():
    title = Text(app, text="Welcome to PhysicsGo!", size=72)
    fillertextb = Text(app, text="", size=50)
    usernametext = Text(app, text="Username")
    usernamebox = TextBox(app, width=25)
    fillertextc = Text(app, text="")
    passwordtext = Text(app, text="Password")
    passwordbox = TextBox(app, width=25, hide_text=True)
    fillertextd = Text(app, text="")
    enterbutton = PushButton(app, text="Log In")
    fillertexte = Text(app, text="", size=64)
    exitbutton = PushButton(app, text="Exit", command=quit)

loginscreen()

app.display()