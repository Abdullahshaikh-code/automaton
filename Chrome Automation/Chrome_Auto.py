from selenium import webdriver
import os
import time

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

def chromeAuto(selected_profiles):
    for profile in selected_profiles:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=" + profile,)
        options.add_argument("--disable-application-cache")
        driver = webdriver.Chrome()
        time.sleep(5)
        driver.get('https://www.youtube.com/watch?v=6lrPSL7jHog')  
        time.sleep(20)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        links = driver.find_elements('xpath','//div[@id="description"]//a')
        if len(links) > 0:
            links[2].click()
        time.sleep(30)
        driver.quit()
p=profiles()
chromeAuto(p)