import pyautogui
from AppOpener import open, close
from time import sleep
def ConnectToDisconnect ():
    button_image = 'Capture_1.PNG'
    connect_button = pyautogui.locateOnScreen(button_image)
    pyautogui.moveTo(connect_button)
    pyautogui.click()

def VpnChange (state):
    country_button_image='Capture_2.PNG'
    search_box_img='SearchingBox.PNG'
    country_button = pyautogui.locateOnScreen(country_button_image)

    if  country_button==None:
        country_button_image='Capture_2.1.PNG'
        country_button = pyautogui.locateOnScreen(country_button_image)
        if  country_button==None:
            country_button_image='Capture_2.2.PNG'
            country_button = pyautogui.locateOnScreen(country_button_image)
            if  country_button==None:
                print("Something went wrong with state selection button")
                return 0
    pyautogui.moveTo(country_button)
    pyautogui.click()
    sleep(0.5)
    search_box=pyautogui.locateOnScreen(search_box_img)
    pyautogui.moveTo(search_box)
    pyautogui.click()
    pyautogui.typewrite(state, interval=0.1)
    pyautogui.moveRel(0,50,0)
    sleep(0.1)
    pyautogui.click()


states=['USA - Albuquerque',
'USA - Atlanta',
'USA - Chicago',
'USA - Dallas',
'USA - Dallas - 2',
'USA - Denver',
'USA - Lincoln Park',
'USA - Los Angeles - 1',
'USA - Los Angeles - 2']
open("ExpressVpn") 
sleep(10)
button_image = 'Connected.PNG'
connected_button = pyautogui.locateOnScreen(button_image)
if connected_button :
    ConnectToDisconnect()
    sleep(1)

count=0
FLAG=True
try:
    while FLAG:
        change=VpnChange(states[count])
        ConnectToDisconnect()
        if change==0:
            break
        sleep(20)
        ConnectToDisconnect()
        sleep(1)
        count += 1
        if count == len(states):
            count = 0
except KeyboardInterrupt:
    print("Program terminated by user.")