# BLUM AUTO CLICK
# HALLOWEEN THEME
from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)

def anjaymabar():
    print("""
   |      |                         |             |   
   __ \   |  |   |  __ `__ \        __ \    _ \   __| 
   |   |  |  |   |  |   |   | _____ |   |  |   )  |  |   
  _.__/  _| \__,_| _|  _|  _|       _.__/  \___/  \__| 
    """)

anjaymabar()
print("  Author: Dymles Ganz")
print("  Contact me on telegram: @XSkull7")
print("  Donations (TON): UQCOmaICnycqfLPWKtcPjpxQzc26CxTtPFuQMNfm2RfEHfKA")
print()
print("  ...:::: CHOOSE LANGUAGE ::::...")
print("  [ 1 ] English")
print("  [ 2 ] Bahasa Indonesia")

while True:
    try:
        language_choice = int(input("\n   blum.bot@main:~# "))
        if language_choice in [1, 2]:
            break
        else:
            print(" Yo bro wrong choose. You can input 1 or 2.")
    except ValueError:
        print(" What??? your input not valid. Please enter number 1 or 2 bro.")

if language_choice == 1:
    window_input = "\n [?] | Enter Window (1 - TelegramDesktop): "
    window_not_found = " [>] | Your Window - {} not found!"
    window_found = " [>] | Window found - {}\n Now bot working... Press 'K' on the keyboard to pause."
    pause_message = " Bot paused...\n Press 'K' again on the keyboard to continue"
    continue_message = " Bot continue working..."
elif language_choice == 2:
    window_input = "\n [?] | Masukin Window nya (1 - TelegramDesktop): "
    window_not_found = "[>] | Window - {} gak di temukan!"
    window_found = "[>] | Window ditemukan - {}\n Sekarang bot berjalan... Pencet 'K' di keyboard buat jeda."
    pause_message = " Bot terjeda... \n Pencet 'spasi' di keyboard buat lanjut lagi"
    continue_message = " Bot ngelanjutin proses..."

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

if window_name == '2':
    window_name = "KotatogramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
    print("EN:\n   Make sure you use the TelegramDesktop application (not Telegram Web).\n   And have opened the Blum bot on your TelegramDesktop.\n   Until the Blum window is available")
    print("ID:\n   Pastikan kamu menggunakan aplikasi TelegramDesktop (bukan Telegram Web).\n   Dan telah membuka Blum bot di TelegramDesktop kamu.\n   Hingga tersedia window Blum nya")
    input("\n Press 'enter' to exit...")
else:
    print(window_found.format(window_name))
    telegram_window = check[0]
    paused = False

    while True:
        if keyboard.is_pressed('K'):
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)

        if paused:
            continue

        window_rect = (
            telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
        )

        if telegram_window != []:
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

        width, height = scrn.size
        pixel_found = False
        if pixel_found:
            break

        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = scrn.getpixel((x, y))
                if (r in range(216, 236)) and (g in range(111, 131)) and (b in range(39, 59)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break
