import pyautogui

from time import sleep
from sys import exit
from selenium import webdriver
import os
import random
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def profiles():
    chrome_user_data_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
    profiles = [os.path.join(chrome_user_data_dir, profile) for profile in os.listdir(chrome_user_data_dir) if 'Profile' in profile]
    print("List of Profiles:")
    for count, profile in enumerate(profiles, start=1):
        print(count, profile)
    selected_indices = input("Enter the index numbers of profiles you want to include (comma-separated): ")
    selected_indices = [int(num) for num in selected_indices.split(',')]
    selected_profiles = [profiles[i-1] for i in selected_indices]
    return selected_profiles
      
def ConnectToDisconnect (script_dir):
    button_image = os.path.join(script_dir, "Capture_1.png")
    connect_button = pyautogui.locateOnScreen(button_image)
    pyautogui.moveTo(connect_button)
    pyautogui.click()
    sleep(1)
def VpnChange (state,script_dir):
   try:
        country_button_image=os.path.join(script_dir, 'Capture_2.PNG')
        search_box_img=os.path.join(script_dir, 'SearchingBox.PNG')
        country_button = pyautogui.locateOnScreen(country_button_image)

        if  country_button==None:
            country_button_image=os.path.join(script_dir,'Capture_2_1.PNG')
            country_button = pyautogui.locateOnScreen(country_button_image)
            if  country_button==None:
                country_button_image=os.path.join(script_dir,'Capture_2_2.PNG')
                country_button = pyautogui.locateOnScreen(country_button_image)
                if  country_button==None:
                    print("Something went wrong with state selection button")
                    return 0
        pyautogui.moveTo(country_button)
        pyautogui.click()
        sleep(2)
        search_box=pyautogui.locateOnScreen(search_box_img)
        pyautogui.moveTo(search_box)
        pyautogui.click()
        pyautogui.typewrite(state, interval=0.1)
        pyautogui.moveRel(0,50,0)
        sleep(0.1)
        pyautogui.click()
        sleep(1)
   except Exception as e:
    # Log the error message
    logging.error(f"An error occurred: {e}")
    pass
       
class Booking(webdriver.Chrome):
    def __init__(self, path_profile):
        # self.driver_path = driver_path
        # os.environ["PATH"] += os.pathsep + self.driver_path

        options = Options()

        index_profile = path_profile.index('Profile')
        pathdir, pr = path_profile[:index_profile], path_profile.split('\\')[-1]

        options.add_argument(f'--user-data-dir={pathdir}')
        options.add_argument(f'--profile-directory={pr}')
        options.add_argument("--window-size=400,1640")
        options.add_argument("--disable-dev-shm-usage")
        super(Booking, self).__init__(options=options)
    def navigate_to_youtube(self,link):
        self.link=link
        self.get(self.link)

    def click_description_link(self):
        # Scroll down to ensure the description is loaded
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        links = self.find_elements('xpath','//div[@id="description"]//a')
        print(links)
        if len(links) > 0:
                links[2].click()


script_dir = os.path.dirname(os.path.abspath(__file__))
ConnectedImg = os.path.join(script_dir, "Connected.PNG")

states=['USA - Albuquerque',
'USA - Atlanta',
'USA - Chicago',
'USA - Dallas',
'USA - Dallas - 2',
'USA - Denver',
'USA - Lincoln Park',
'USA - Los Angeles - 1',
'USA - Los Angeles - 2']
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
chrome_profiles=profiles()
waitTime=int(input("Enter Time InSeconds:"))
ytLink=str(input("Enter Youtube video Link:"))

sleep(3)
connected_button = pyautogui.locateOnScreen(ConnectedImg)
if connected_button :
    ConnectToDisconnect(script_dir)
    sleep(1)

try:
    for profile in chrome_profiles:
        change=VpnChange(random.choice(states),script_dir)
        if change !=0:
            ConnectToDisconnect(script_dir)               
            chrome_Obj = Booking(profile)
            chrome_Obj.navigate_to_youtube(ytLink)
            sleep(10)
            chrome_Obj.click_description_link()
            sleep(10)
            ConnectToDisconnect(script_dir)  
    sleep(waitTime)
    chrome_Obj.quit()

except Exception as e:
    logging.error(f"An error occurred: {e}")
    pass
    print(f"An error occurred: {e}")