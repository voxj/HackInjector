import colorama
import random
from random import randint
from time import sleep
from webbrowser import open_new_tab
import pyautogui 
import time
import tkinter as tk
import urllib.request
from PIL import ImageTk, Image
from tkinter import messagebox
# Made by voxj. and Happy Enderman, published by Chexware
# Don't release edited versions that contain anything malicious. If you want to edit something, create a pull request on https://github.com/voxj/HackInjector/pulls.
# https://voxj.github.io/chexware
# Copyright ©️ Chexware, voxj., Happy Enderman 2024
__name__ = "HackInjector"
__version__ = "1.2.2"
__state__ = "Public Release"
__safe__ = True # and always will be!
Fore = colorama.Fore
init = colorama.init
Style = colorama.Style
colorama.init()
try:
    def download_asset(url, file_name):
        try:
            urllib.request.urlretrieve(url, file_name)
            show_image(file_name)
        except Exception as e:
            print(e)
            pass
    def show_image(image_path, user):
        root = tk.Tk()
        root.title(f"{user}'s Screen")
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.pack()
        root.mainloop()
    def getIP(user):
        print(f"Getting {user}'s IP...")
        sleep(2.5)
        print("Fetching data...")
        sleep(1)
        print("Getting data...")
        sleep(0.25)
        a = str(randint(1, 10))
        if a in ["1", "2", "6", "4", "8", "9"]:
            ip = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}.{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}.{randint(1, 9)}{randint(1, 9)}.{randint(1, 9)}{randint(1, 9)}"
            print(f"IP: {ip}")
            return ip
        else:
            print(f"{Fore.LIGHTRED_EX}Error: No Access{Fore.RESET}")
            return
    def playSound():
        a = input("What sound do you want to play? ")
        sleep(0.25)
        b = input("Is the sound is gonna be played on your or someone else's PC? (mine/not mine) ")
        if b == "mine":
            print(f'Playing the sound "{a}"...')
            sleep(0.25)
        elif b == "not mine":
            u = input('What is the user? ')
            getIP(u)
            print(f"Playing the sound {a} on {u}'s PC...")
    def sendNotification():
        title = input("What is the title?: ")
        description = input("What is the description?: ")
        b = input("Is the sound going to be played on your or someone else's PC? (mine/not mine) ")
        if b == "mine":
            print("Sending the notification to yourself...")
            messagebox.showinfo(title, description)
            sleep(0.25)
        elif b == "not mine":
            u = input("What is the user? ")
            sleep(0.25)
            getIP(u)
            print(f"Sending notification to {u}...")
    def hackPC(user):
        password_length = random.randint(8, 16)
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(password_length))
        sleep(0.25)
        print("Initializing hacking sequence...")
        sleep(0.15)
        a = getIP(user)
        if a == None:
            print("No Access. Please try again!")
            return
        else:
            print(f"Target PC: {user}sPC")
            print(f"Target IP: {a}")
            sleep(0.25)
            print("Executing brute force attack...")
            sleep(2)
            print("Attempting to bypass firewall...")
            sleep(5)
            print("Gaining root access...")
            sleep(2)
            print("Hacking complete!")
            sleep(0.05)
            print("Password for root access: " + password)
    def hackPhone(user):
        password_length = random.randint(8, 16)
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(password_length))
        time.sleep(0.25)
        print("Initializing hacking sequence...")
        time.sleep(0.15)
        a = getIP(user)
        if a is None:
            print("No Access. Please try again!")
            return
        else:
            phone_models = ['Google Pixel 8a', 'Google Pixel 8 Pro', 'Xiaomi Redmi 5S', 'Xiaomi Redmi 9', 'iPhone X', 'Samsung Galaxy S20', 'Google Pixel 4', 'Google Pixel 5', 'Google Pixel 6', 'Google Pixel 7', 'Google Pixel 8', 'iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14', 'iPhone 15', 'iPhone 15 Pro', 'iPhone 15 Pro Max', 'iPhone 15 Pro mini Max (UNVERIFIED)', 'iPhone 167 Super Mega pro Mini ultra big (UNVERIFIED)']
            phone = random.choice(phone_models)
            print(f"Target Phone: {phone}")
            print(f"Target IP: {a}")
            time.sleep(0.25)
            print("Executing brute force attack...")
            time.sleep(2)
            print("Attempting to bypass antivirus...")
            time.sleep(5)
            print("Gaining root access...")
            time.sleep(2)
            print("Hacking complete!")
            time.sleep(0.05)
            print("Password for root access: " + password) # https://youtu.be/hkp65DLcktA?t=638 watch this lol
    def hackWebcam(user):
        time.sleep(0.15)
        print("Initializing hacking sequence...")
        print(f"Webcam Hacked! Webcam owner: {user}")
        print("Getting Video...")
        open_new_tab("https://youtu.be/hkp65DLcktA?t=638")
    def seeScreen():
        b = input("Which user's screen do you want to see? Yours or someone else's PC? (mine/not mine) ")
        if b == "mine":
            pyautogui.screenshot('s.png')
            sleep(0.25)
            show_image('s.png')# 
        elif b == "not mine":
            u = input('What is the user? ')
            sleep(0.25)
            print(f"Getting {u}'s screen...")
            sleep(1)
            print("Fetching data...")
            sleep(0.23)
            print("Getting data...")
            sleep(1)
            download_asset('https://i.ibb.co/RpmGCSr/rlysus.png', 'sus.png')
    def isItSafe():
        random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
        print(f"{random_color}", end="")
        for letter in HackInjector:
            random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
            print(f"{random_color}{letter}", end="")
        print(colorama.Fore.RESET + " - Is it safe?")
        sleep(5)
        random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
        print(f"{random_color}", end="")
        for letter in HackInjector:
            random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
            print(f"{random_color}{letter}", end="")
        print(f"{Fore.RESET} doesn't hack anything. It is a joke program you can use for some fun and etc., and it doesn't do anything to you device. So, it is completely safe! And, we will never do anything malicious. And even if we will, it will always be marked with some BIG MARKDOWN TEXT saying that THIS IS MALICIOUS! So, you can trust us whenever you want, but make sure you've readen the README if it exists!")
        sleep(10)
    def editPage(link, before, after):
        print(f'Editing the page on {link}...')
        sleep(5)
        print(f'Changes Made: {before} -> {after}')
    def moveMouse(x1, y1):
        print(f'Moved mouse from original position to {x1}x{y1}.')
    def giveError():
        title = input("What should be the title?: ")
        msg = input('What should be the message?: ')
        messagebox.showwarning(title, msg)
    def sendPrompt():
        msg = input('What should be the message?: ')
        r=pyautogui.prompt(msg)
        print(r)
    def disconnect(user, name):
        a = getIP(user)
        if a != None:
            sleep(2)
            print(f'Disconnecting accessory "{name}"...')
            sleep(1)
            print(f"Disconnected accessory {name} on {user}'s PC.")
            sleep(2)
        else:
            print('No Access. Please try again!')
            sleep(3)
            return
            
    hackascii = """  _    _            _    _____       _           _             
     | |  | |          | |  |_   _|     (_)         | |            
     | |__| | __ _  ___| | __ | |  _ __  _  ___  ___| |_ ___  _ __ 
     |  __  |/ _` |/ __| |/ / | | | '_ \| |/ _ \/ __| __/ _ \| '__|
     | |  | | (_| | (__|   < _| |_| | | | |  __/ (__| || (_) | |   
     |_|  |_|\__,_|\___|_|\_\_____|_| |_| |\___|\___|\__\___/|_|   
                                       _/ |                        
                                      |__/                         """
    
    hackinjector = "HackInjector"
    HackInjector = hackinjector
    
    for char in hackascii:
        random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
        print(f"{random_color}{char}", end=f"{colorama.Fore.RESET}")
    print()
    
    sleep(1)
    
    random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
    print(f"Welcome to {random_color}", end="")
    for letter in HackInjector:
        random_color = random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])
        print(f"{random_color}{letter}", end="")
    print(colorama.Fore.RESET + "!")
    
    sleep(2)
    
    while True:
        options = input(
        """
    Those are your options:
    1) Get IP
    2) Play Sound
    3) Send Notification
    4) Hack Phone
    5) Hack PC
    6) Hack Webcam
    7) Edit Page
    8) See Screen
    9) Move Mouse
    10) Give Error
    11) Send a Prompt
    12) Disconnect Accessory
    13) Is it safe?
    14) Data
    15) Exit
    What do you choose? Note: used like 1), 2) etc.: """
        )
        if options != None:
            if options.startswith('1)'):
                user = input('Username: ')
                getIP(user)
            elif options.startswith("2)"):
                playSound()
            elif options.startswith("3)"):
                sendNotification()
            elif options.startswith("4)"):
                user = input('Username: ')
                hackPhone(user)
            elif options.startswith("5)"):
                user = input('Username: ')
                hackPC(user)
            elif options.startswith("6)"):
                user = input('Username: ')
                hackWebcam(user)
            elif options.startswith("7)"):
                link = input("Link: ")
                before = input("Change from: ")
                after = input("To: ")
                editPage(link, before, after)
            elif options.startswith("8)"):
                seeScreen()
            elif options.startswith("9"):
                x1 = input("What should be the X (Position)?: ")
                y1 = input("What should be the Y (Position)?: ")
                moveMouse(x1, y1)
            elif options.startswith("10)"):
                giveError()
            elif options.startswith("11)"):
                sendPrompt()
            elif options.startswith("12)"):
                user = input('Username: ')
                accessory = input('Accessory: ')
                disconnect(user, accessory)
            elif options.startswith("13)"):
                isItSafe()
            elif options.startswith("14)"):
                print(f"{__name__} {__state__} v{__version__}")
            elif options.startswith("15)"):
                exit()
        else:
            pyautogui.alert('Expected valid choice, got unknown')
            exit()
except Exception as e:
    print(f'Some error happened: {e}')
    exit()
# made with ❤️ by voxj. & Happy Enderman
# Copyright ©️ Chexware, voxj., Happy Enderman 2024
