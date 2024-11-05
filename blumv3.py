# BLUM Airdrop Auto Click - President trump/kamala
# Made by Dymles Ganz
# Recoded by yourname

from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
from termcolor import colored

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
print("  Contact telegram: @BraveXploiter")
print("  Donations USDT (TRC20): TYna9WAoVCAF2f7ynnjS2bQixkLQz8XxFh")
print()
print("  ...:::: CHOOSE LANG ::::...")
print("  [ 1 ] English")
print("  [ 2 ] Bahasa Indonesia")

while True:
    try:
        language_choice = int(input("\n   blumbot@main:~# "))
        if language_choice in [1, 2]:
            break
        else:
            print(" Yo bro wrong choose. You can input 1 or 2.")
    except ValueError:
        print(" What??? your input not valid. Please enter number 1 or 2 bro.")

if language_choice == 1:
    print("\n  ...:::: CHOOSE WINDOW APP ::::...")
    print("  [ 1 ] Telegram Desktop")
    print("  [ 2 ] Kotatogram Desktop")
    window_input = "\n blumbot@app:~# "
    window_not_found = " Your Window - {} not found!"
    window_found = " Window found! - {}\n Now bot working... Press 'K' on the keyboard to pause."
    pause_message = " Bot paused...\n Press 'K' again in the keyboard to continue"
    continue_message = " Bot continue working..."
elif language_choice == 2:
    print("\n  ...:::: PILIH APLIKASI ::::...")
    print("  [ 1 ] Telegram Desktop")
    print("  [ 2 ] Kotatogram Desktop")
    window_input = "\n blumbot@app:~# "
    window_not_found = "Window - {} gak di temukan!"
    window_found = " Window ditemukan - {}\n Sekarang bot berjalan... Pencet 'K' di keyboard buat jeda."
    pause_message = " Bot terjeda... \n Pencet 'K' di keyboard buat lanjut lagi"
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
    input("\n Press 'ENTER' to exit...")
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

        for x in range(0, width, 13):
            for y in range(0, height, 13):
                r, g, b = scrn.getpixel((x, y))
                if (63 <= r <= 73) and (219 <= g <= 229) and (0 <= b <= 10):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break

                elif (226 <= r <= 236) and (170 <= g <= 180) and (131 <= b <= 141):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break

                elif (255 <= r <= 265) and (137 <= g <= 147) and (97 <= b <= 107):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break
