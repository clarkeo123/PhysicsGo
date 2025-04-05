from guizero import *
import json
import subprocess
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#gets the login details from the database
file = open("Logins.json")
data = json.load(file)["Credentials"]

#creates the master app object
app = App(title="PhysicsGo")
app.hide()

def backtologin(currentwindow):
    #closes the current window and returns them to the login page
    global useraccess
    currentwindow.destroy()
    useraccess = ""
    loginscreen()

def runprogram(currentwindow,program):
    #closes the menu and opens a simulation
    currentwindow.destroy()
    subprocess.run(['python',program])
    menu()

def runquiz(currentwindow, quiz):
    #replaces the menu objects with a quiz
    import Quiz
    Quiz.main(quiz, app)

def loginchecker(username, password):
    global useraccess
    #compares username and password input by the user with the database's login details
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
    #creates all gui objects for the login screen
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
    enterbutton = PushButton(loginwindow, text="Log In", command=loginchecker, args=[usernamebox, passwordbox]) #triggers the login checker
    fillertexte = Text(loginwindow, text="", size=64)
    exitbutton = PushButton(loginwindow, text="Exit", command=quit)

def menu():
    #creates all gui objects for the main menu
    global menuwindow
    menuwindow = Window(app, title="Second window")
    menuwindow.set_full_screen()
    title = Text(menuwindow, text="Please choose an option:", size=32)
    fillertexta = Text(menuwindow, text="")
    #each button calls a simulation or quiz
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