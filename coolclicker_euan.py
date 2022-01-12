import random
from tkinter import Tk
from tkinter import Canvas
import time
import json
import math
#import time.wait


def getState(file, deftData):
    try:
        infile = open('data.json', 'r')
        data = json.load(infile)
        return data
    except:
        return deftData 

def reset(e):
    confirm = input("Are u sure? This will delete ALL your progress FOREVER! Type 'YES' exactly (Case sensitive)")
    if confirm == "YES":
        print("Reset happened!")
        UHDB = 0
        clicks = 0
        money = 0
        moneyupgrade1 = 25
        upgrade1owned = 0
        moneyupgrade2 = 100
        upgrade2owned = 0
        moneyupgrade3 = 150
        upgrade3owned = 0
        moneyupgrade4 = 250
        upgrade4owned = 0
        mpc = 1
        print("Variables were reset!")
        saveState()
        print("State was saved! new state: ")
        delete_and_replace()
    else:
        print("abort")

xxx = False
color = "green"
color2 = "black"
color3 = "white"
color4 = "black"
symbol = "$"
zzzz = ["You sure you typed it in right?", "Uhhhh... no.", "What?", "Hmmmmmm, are you trying to cheat or something?", "...", "Not gonna work!", "Try again..."]
isAlfredo = False
isDev = False

ask = input("If you are a dev, please type in your dev code: ") #dev stuff
if ask == "18-001-CJWasHere": #if you are a dev, please enter a code then post the newly editted game code in Google Classroom
    #do whatever you want here
    print("Your dev/real name here + whatever message you like")
elif ask == "placement2 + your dev number(for example, the third person to join would be '003', or the fifteenth would be '015')": #if you are a dev, please enter a code then post the newly editted game code in Google Classroom
    #do whatever you want here
    print("Your dev/real name here + whatever message you like")
elif ask == "63-002-brrr": #Snowlander dev code
    print("Snowlander dev code had been activated -- o_o 'I've been discovered'")
    xxx = True
elif ask == "Alfredo":
    oask = input("Hello, Secret Password: ")
    ooask = input("Do u have a private key")
    if ooask == 'y' or ooask == 'Y':
        part1ofkey = open("firstkeypeice.txt")
        part2ofkey = open("otherkeypeice.txt")
        if math.log(int(part1ofkey.read()))/math.log(int(part2ofkey.read())) == 6.892479911602366:
            oask = "Hola! ni3 hao3! Psst... Ingles es aburido. blek."
            print("encryption key worked")
        else:
            print(str(math.log(int(part1ofkey.read()))/math.log(int(part2ofkey.read()))))
    if oask == "Hola! ni3 hao3! Psst... Ingles es aburido. blek.":
        print("Bienvenido, Alfredo! Eres muy padre!")
        isAlfredo = True
    else:
        print("bu2 dui4!! No More Cheating!")
elif ask == "devParaphrase":
    oask = input("Hello, Secret Password: ")
    if oask == "azFFreMinecraftShi4Fun":
        isDev = True
elif ask == '':
    print("Ok, go ahead normal user")
else:
    print(random.choice(zzzz))
while True:
    currencyType = input("Enter currency code, leave blank or type code for USD/MXN: ")
    if currencyType == "USD":
        symbol = "$"
        break
    elif currencyType == "MXN":
        symbol = "$"
        break
    elif currencyType == "JPY":
        symbol = "¥"
        break
    elif currencyType == "EUR":
        symbol = "€"
    elif currencyType == "":
        symbol = "$"
        break
    else:
        print("Invalid Code, please try again.")
        print("Key:")
        print("USD = $")
        print("MXN = $")
        print("JPY = ¥")
        print("EUR = €")
        print("This is case sensitive!")
        print("")
        print("")
global clicks
global money
UHDB = 0
clicks = 0
money = 0
moneyupgrade1 = 25
upgrade1owned = 0
moneyupgrade2 = 100
upgrade2owned = 0
moneyupgrade3 = 150
upgrade3owned = 0
moneyupgrade4 = 250
upgrade4owned = 0
mpc = 1

state = getState(None, None)
if(state != None):
    if state["moneyupgrade1"] < 25:
        state["moneyupgrade1"] = 25
    if state["moneyupgrade2"] < 100:
        state["moneyupgrade2"] = 100
    if state["moneyupgrade3"] < 150:
        state["moneyupgrade3"] = 150
    if state["moneyupgrade4"] < 250:
        state["moneyupgrade4"] = 250
    if state["mpc"] < 1:
        state["mpc"] = 1
    money = state['money']
    clicks = state['clicks']
    mpc = state["mpc"]
    moneyupgrade1 = state["moneyupgrade1"]
    upgrade1owned = state["upgrade1owned"]
    moneyupgrade2 = state["moneyupgrade2"]
    upgrade2owned = state["upgrade2owned"]
    moneyupgrade3 = state["moneyupgrade3"]
    upgrade3owned = state["upgrade3owned"]
    moneyupgrade4 = state["moneyupgrade4"]
    upgrade4owned = state["upgrade4owned"]
    print("Loaded state!" + str(state))

nomoney = 0
number = 0
universeDisruption = False
a_text = "" #a stands for achievment
if xxx == True:
    print("Ha ha colors go brrrrrr \n    -Snowlander")
    color = "#FF0DEC"
    color2 = "#535CFF"
    color3 = "black"
    color4 = "#33D6D6"
    symbol = "£"




def saveState():
    state = {}
    state['money'] = money
    state['clicks'] = clicks
    state["mpc"] = mpc
    state["moneyupgrade1"] = moneyupgrade1
    state["upgrade1owned"] = upgrade1owned
    state["moneyupgrade2"] = moneyupgrade2
    state["upgrade2owned"] = upgrade2owned
    state["moneyupgrade3"] = moneyupgrade3
    state["upgrade3owned"] = upgrade3owned
    state["moneyupgrade4"] = moneyupgrade4
    state["upgrade4owned"] = upgrade4owned
    with open('data.json', 'w') as outfile:
        json.dump(state, outfile)

def saveAndQuit():
    saveState()
    print("saveandquit occoured.")
    tk.quit()

def drawmoneyupgrades():
    canvas.create_rectangle(950,150,1150,50,fill="gray")
    canvas.create_rectangle(1000,125,1100,75,fill=color)
    canvas.create_oval(1025,110,1075,90,fill="light green")
    canvas.create_text(975,160,anchor="nw",text=str(moneyupgrade1) + " money to buy", font="TKFixedFont 15")
    canvas.create_text(975,180,anchor="nw",text="+ 1 MPS", font="TKFixedFont 15")
    canvas.create_text(975,200,anchor="nw",text="Owned: " + str(upgrade1owned), font="TKFixedFont 15")
    canvas.create_text(1045,93,anchor="nw",text="1", font="TKFixedFont 10")
    # second one
    canvas.create_rectangle(950,350,1150,250,fill="gray")
    canvas.create_rectangle(1000,325,1100,275,fill=color)
    canvas.create_oval(1025,310,1075,290,fill="light green")
    canvas.create_text(1045,293,anchor="nw",text="5", font="TKFixedFont 10")
    canvas.create_text(975,360,anchor="nw",text=str(moneyupgrade2) + " money to buy", font="TKFixedFont 15")
    canvas.create_text(975,380,anchor="nw",text="+ 5 MPS", font="TKFixedFont 15")
    canvas.create_text(975,400,anchor="nw",text="Owned: " + str(upgrade2owned), font="TKFixedFont 15")
    # third one
    canvas.create_rectangle(950,550,1150,450,fill="gray")
    canvas.create_rectangle(1000,525,1100,475,fill=color)
    canvas.create_oval(1025,510,1075,490,fill="light green")
    canvas.create_text(1045,493,anchor="nw",text="10", font="TKFixedFont 10")
    canvas.create_text(975,560,anchor="nw",text=str(moneyupgrade3) + " money to buy", font="TKFixedFont 15")
    canvas.create_text(975,580,anchor="nw",text="+ 10 MPS", font="TKFixedFont 15")
    canvas.create_text(975,600,anchor="nw",text="Owned: " + str(upgrade3owned), font="TKFixedFont 15")
    # fourth one
    canvas.create_rectangle(950,750,1150,650,fill="gray")
    canvas.create_rectangle(1000,725,1100,675,fill=color)
    canvas.create_oval(1025,710,1075,690,fill="light green")
    canvas.create_text(1045,693,anchor="nw",text="20", font="TKFixedFont 10")
    canvas.create_text(975,760,anchor="nw",text=str(moneyupgrade4) + " money to buy", font="TKFixedFont 15")
    canvas.create_text(975,780,anchor="nw",text="+ 20 MPS", font="TKFixedFont 15")
    canvas.create_text(975,800,anchor="nw",text="Owned: " + str(upgrade4owned), font="TKFixedFont 15")
    # fifth one
    

def drawmoney():
    global mpc, a_text
    canvas.create_rectangle(400,450,700,350,fill=color)
    canvas.create_oval(475,325,625,475,fill="#00C10F",outline="#00C10F")
    canvas.create_rectangle(400,450,700,550,fill=color3,outline=color3)
    canvas.create_rectangle(400,250,700,350,fill=color3,outline=color3)
    canvas.create_rectangle(800,550,700,250,fill=color3,outline=color3)
    canvas.create_rectangle(400,550,300,250,fill=color3,outline=color3)
    canvas.create_rectangle(400,450,700,430,fill=color,outline=color)
    canvas.create_rectangle(400,370,700,350,fill=color,outline=color)
    canvas.create_line(400,450,400,350, fill=color2)
    canvas.create_line(700,450,700,350, fill=color2)
    canvas.create_line(400,450,700,450, fill=color2)
    canvas.create_line(400,350,700,350, fill=color2)
    canvas.create_text(530,380,anchor="nw",text=str(mpc) + symbol, font="TKFixedFont 25")
    canvas.create_text(415,270,anchor="nw",text="You have " + str(clicks) + " clicks", font="TKFixedFont 25")
    canvas.create_text(10,10,anchor="nw",text="Most recent achievment:", font="TKFixedFont 10")
    canvas.create_text(10,30,anchor="nw",text=a_text, font="TKFixedFont 10")
    if isDev == True:
        canvas.create_text(10, 50, anchor="nw", text="You are a developer, you have command access", font="TKFixedFont 10")

def delete_and_replace():
    canvas.delete("all")
    drawmoney()
    drawmoneytext()
    drawmoneyupgrades()
    

def drawmoneytext():
    canvas.create_text(415,305,anchor="nw",text="You have " + str(money) + " money", font="TKFixedFont 25")

#clicks = 0

def drawnomoney():
    global nomoney
    global number
    nomoney = 1
    if nomoney == 1:
        canvas.create_text(420,180,anchor="nw",text="You dont have enough money to do this", font="TKFixedFont 15")
        nomoney = 0
        delete_and_replace()


def mouse_was_clicked(event):
    #"clicks = clicks + 1" won't work help
    #print(event.x,event.y)
    global money,mpc,moneyupgrade1,moneyupgrade2,moneyupgrade3,moneyupgrade4,upgrade1owned,upgrade2owned,upgrade3owned,upgrade4owned,clicks

    if 400 < event.x < 700 and 350 < event.y < 450:
        money = money + mpc
        clicks = clicks + 1
        achievementYay()
        delete_and_replace()
    if 950 < event.x < 1150 and 50 < event.y < 150:
        if money >= moneyupgrade1:
            money = money - moneyupgrade1
            moneyupgrade1 = moneyupgrade1 * (115/100)
            money = round (money,0)
            moneyupgrade1 = round (moneyupgrade1,0)
            mpc = mpc + 1
            upgrade1owned = upgrade1owned + 1
            delete_and_replace()
            print(money)
    if 950 < event.x < 1150 and 250 < event.y < 350:
        if money >= moneyupgrade2:
            money = money - moneyupgrade2
            moneyupgrade2 = moneyupgrade2 * (115/100)
            money = round (money,0)
            moneyupgrade2 = round (moneyupgrade2,0)
            mpc = mpc + 5
            upgrade2owned = upgrade2owned + 1
            delete_and_replace()
            print(money)
    if 950 < event.x < 1150 and 450 < event.y < 550:
        if money >= moneyupgrade3:
            money = money - moneyupgrade3
            moneyupgrade3 = moneyupgrade3 * (115/100)
            money = round (money,0)
            moneyupgrade3 = round (moneyupgrade3,0)
            mpc = mpc + 10
            upgrade3owned = upgrade3owned + 1
            delete_and_replace()
            print(money)
    if 950 < event.x < 1150 and 650 < event.y < 750:
        if money >= moneyupgrade4:
            money = money - moneyupgrade4
            moneyupgrade4 = moneyupgrade4 * (115/100)
            money = round (money,0)
            moneyupgrade4 = round (moneyupgrade4,0)
            mpc = mpc + 20
            upgrade4owned = upgrade4owned + 1
            delete_and_replace()
            print(money)
    
    
def achievementYay(): #find a way to draw the achievements onto the board
    global mpc,money,clicks,UHDB,a_text
    if clicks == 1:
        print("First Clicks: Click your first time. -- Nice Job!")
        a_text = ("First Clicks: Click your first time. -- Nice Job!")
    if clicks == 25:
        print("Upgrade Ready: Click 25 times. -- Now things get eaiser.")
        a_text = "Upgrade Ready: Click 25 times. -- Now things get eaiser."
    if clicks == 100:
        print("Post-Beginner Clicker: Click 100 times. -- WooHoo! Ready 2 go!")
        a_text = "Post-Beginner Clicker: Click 100 times. -- WooHoo! Ready 2 go!"
    if clicks == 150:
        print("Drowing In Clicks: Click 150 times. -- No turning back now!")
        a_text = "Drowing In Clicks: Click 150 times. -- No turning back now!"
    if clicks == 200:
        print("200 Is The Way To Go: click 200 times. -- Clicked out yet?")
        a_text = "200 Is The Way To Go: click 200 times. -- Clicked out yet?"
    if clicks == 300:
        print("TOO MANY CLICKS: Click 300 times. -- :D")
        a_text = "TOO MANY CLICKS: Click 300 times. -- :D"
    if clicks == 400:
        print("def MouseWasBroken: Click 400 times. -- D:")
        a_text = "def MouseWasBroken: Click 400 times. -- D:"
    if clicks == 500:
        print("Clicker Legend: Click 500 times. -- Now double that for the next achievement!!!")
        a_text = "Clicker Legend: Click 500 times. -- Now double that for the next achievement!!!"
        money = money + 100
    if clicks == 1000:
        print("Clicker God: Click 1k times. -- What have you done...")
        a_text = "Clicker God: Click 1k times. -- What have you done..."
        money = money + 1000
        universeDisruption = True
    if clicks == 5000:
        print("Clicker-Verse Disruption: Click 5k times. -- You successfully destroyed the world!!!")
        a_text = "Clicker-Verse Disruption: Click 5k times. -- You successfully destroyed the world!!!"
    if clicks == 10000:
        print("Too Many For Your Own Good: click 10K times. -- Great now get to 50K")
        a_text = "Too Many For Your Own Good: click 10K times. -- Great now get to 50K"
        mpc = mpc + 100
    if mpc == 666:
        if UHDB == 0:
            print("The Unholy Dollar Bill: Create a $666 bill. -- WHAT THE HECK IS THIS?!?!?!?!")
            a_text = "The Unholy Dollar Bill: Create a $666 bill. -- WHAT THE HECK IS THIS?!?!?!?!"
            money = money + 1000
            UHDB = 1
    if clicks == 50000:
        print("The 5000000th Time Is The Charm: Click 50K times. -- Well $100K is no problem now... right?")
        a_text = "The 5000000th Time Is The Charm: Click 50K times. -- Well $100K is no problem now... right?"
    if clicks == 100000:
        print("My New Life... Will Never End: Click 100K times. -- Now get to 1M alright?")
        a_text = "My New Life... Will Never End: Click 100K times. -- Now get to 1M alright?"
    if clicks == 500000:
        print("Mile Marker 1: Click 500K times. -- Whoah! We're halfway there oh, whoah oh!!!! Livin' on a prayer!") #livin' on a prayer
        a_text = "Mile Marker 1: Click 500K times. -- Whoah! We're halfway there oh, whoah oh!!!! Livin' on a prayer!"
    if clicks == 100000:
        print("The 10000000th Click: Click 100K times. -- I-I was j-j-joking o-ok???")
        a_text = "The 1000000th Click: Click 100K times. -- I-I was j-j-joking o-ok???"
    if clicks == 500000:
        print("Mile Marker 2: Click 500K times. -- Take my hand! We'll make it I swear-oh, whoah oh! Livin' on a prayer ohhhhhhhhhh...")
        a_text = "Mile Marker 2: Click 500K times. -- Take my hand! We'll make it I swear-oh, whoah oh! Livin' on a prayer ohhhhhhhhhh..."
    if clicks == 1000000:
        print("1Million Should Do It: Click 1M times. -- YOU SERIOUSLY DID THAT?!?!?!")
        a_text = "1Million Should Do It: Click 1M times. -- YOU SERIOUSLY DID THAT?!?!?!"
        money = money * 10
    if clicks == 5000000:
        print("Mile Marker 3: Click 5M times. -- (Awesome gituar solo)") #next song 5million clicks
        a_text = "Mile Marker 3: Click 5M times. -- (Awesome gituar solo)"
    
    if (isDev):
        print(clicks) #DO NOT REMOVE FOR DEVELOPING POURPOSES (though please remove once the achievements I will put status here) -- STATUS: Unfinished
    
    delete_and_replace()
    



tk = Tk()
tk.title("Cool Clicker || V1.4 || Unfinfinished || 30% finished(???) CJWasHere And Alfredo")
canvas = Canvas(tk, width=1200, height=900)
canvas.pack()

delete_and_replace()
drawmoney()
drawmoneytext()
drawmoneyupgrades()

def giveIfDev(event):
    if isAlfredo or isDev:
        global money
        global clicks
        money = money + 1
        clicks = clicks + 1
        delete_and_replace()
        saveState()
        print("Created new click and " + symbol + ".")

tk.bind( "<Button-1>",mouse_was_clicked)
tk.protocol("WM_DELETE_WINDOW", saveAndQuit)
tk.bind('<Control-r>',reset) #Resets all progress with confirmation
tk.bind('<Control-a>', giveIfDev)

tk.mainloop()
