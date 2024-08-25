from guizero import *
import json
import subprocess

file = open("Logins.json")
data = json.load(file)["Credentials"]

app = App(title="PhysicsGo")
app.hide()

def backtologin(currentwindow):
    global useraccess
    currentwindow.destroy()
    useraccess = ""
    loginscreen()

def runprogram(currentwindow,program):
    currentwindow.destroy()
    subprocess.run(['python',program])
    menu()

def runquiz(currentwindow, quiz):
    import Quiz
    Quiz.main(quiz, app)

def loginchecker(username, password):
    global useraccess
    if username.value == data[0]["Username"] and password.value == data[0]["Password"]:
        useraccess = "Teacher"
        loginwindow.destroy()
        menu()
    elif username.value == data[1]["Username"] and password.value == data[1]["Password"]:
        useraccess = "Student"
        loginwindow.destroy()
        menu()
    else:
        loginresponse.value = "Incorrect username or password"

def loginscreen():
    global loginresponse, loginwindow
    loginwindow = Window(app, title="balls")
    loginwindow.set_full_screen()
    title = Text(loginwindow, text="Welcome to PhysicsGo!", size=72)
    fillertextb = Text(loginwindow, text="", size=50)
    usernametext = Text(loginwindow, text="Username")
    usernamebox = TextBox(loginwindow, width=25)
    fillertextc = Text(loginwindow, text="")
    passwordtext = Text(loginwindow, text="Password")
    passwordbox = TextBox(loginwindow, width=25, hide_text=True)
    fillertextf = Text(loginwindow, text="")
    loginresponse = Text(loginwindow, text="")
    fillertextd = Text(loginwindow, text="")
    enterbutton = PushButton(loginwindow, text="Log In", command=loginchecker, args=[usernamebox, passwordbox])
    fillertexte = Text(loginwindow, text="", size=64)
    exitbutton = PushButton(loginwindow, text="Exit", command=quit)

def menu():
    global menuwindow
    menuwindow = Window(app, title="Second window")
    menuwindow.set_full_screen()
    title = Text(menuwindow, text="Please choose an option:", size=32)
    fillertexta = Text(menuwindow, text="")
    doppleroption = PushButton(menuwindow, text="Doppler Effect Simulation", command=runprogram, args=[menuwindow,"DopplerEffect.py"])
    dopplerquizoption = PushButton(menuwindow, text="Doppler Effect Quiz", command=runquiz, args=[menuwindow, "Doppler Effect Quiz"])
    pressureoption = PushButton(menuwindow, text="Pressure Simulation", command=runprogram, args=[menuwindow,"ParticlePressure.py"])
    pressurequizoption = PushButton(menuwindow, text="Pressure Quiz", command=runquiz, args=[menuwindow, "Pressure Quiz"])
    kinematicsoption = PushButton(menuwindow, text="Kinematics Simulation", command=runprogram, args=[menuwindow,"Kinematics.py"])
    kinematicsquizoption = PushButton(menuwindow, text="Kinematics Quiz", command=runquiz, args=[menuwindow, "Kinematics Quiz"])
    fillertextb = Text(menuwindow, text="")
    logout = PushButton(menuwindow, text="Log Out", command=backtologin, args=[menuwindow])

loginscreen()

app.display()