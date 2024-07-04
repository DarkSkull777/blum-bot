from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
from termcolor import colored
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)

putih = '\033[1;97m'
merah = '\033[1;91m'
hijau = '\033[1;92m'
kuning = '\033[1m\033[93m'
biru = '\033[1;94m'
reset = '\033[0m'
putihmerah = '\033[97m\033[41m'
putihhijau = '\033[97m\033[42m'
merahhijau = '\033[1;91m\033[42m'

def anjaymabar():
    print(f"""{hijau}
  {hijau}|      |                         {kuning}  |             |   
  {hijau}__ \   |  |   |  __ `__ \        {kuning}  __ \    _ \   __| 
  {hijau}|   |  |  |   |  |   |   | {merah}_____|{kuning}  |   |  (   |  |   
 {hijau}_.__/  _| \__,_| _|  _|  _|       {kuning} _.__/  \___/  \__| {reset}
    """)

anjaymabar()
print(f" {putihmerah}Author: Dymles Ganz{reset}")
print(f" {putihhijau}Contact me on telegram: @XSkull7{reset}")
print(f" {kuning}Donations (TON):{putih} UQCOmaICnycqfLPWKtcPjpxQzc26CxTtPFuQMNfm2RfEHfKA{reset}")
print()
print(colored("  ...:::: CHOOSE LANGUAGE ::::...", 'light_cyan'))
print(colored("  [ ", 'white') + colored("1 ", 'light_green') + colored("] ", 'white') + colored("English", 'light_yellow'))
print(colored("  [ ", 'white') + colored("2 ", 'light_green') + colored("] ", 'white') + colored("Bahasa Indonesia", 'light_yellow'))

while True:
    try:
        language_choice = int(input(f"\n  {putih}blum.bot@main:~# {reset}"))
        if language_choice in [1, 2]:
            break
        else:
            print(f"{merah} Yo bro wrong choose. You can input {kuning}1 {merah}or {kuning}2{merah}.{reset}")
    except ValueError:
        print(f" {merah}What??? your input not valid. Please enter number {kuning}1 {merah}or {kuning}2 {merah}bro.{reset}")

if language_choice == 1:
    window_input = f"\n{putih} [?] | Enter Window {hijau}(1 - TelegramDesktop){putih}: {reset}"
    window_not_found = f"{putih} [>] | Your Window - {{}} {kuning}not found!{reset}"
    window_found = f"{hijau} [>] | Window found - {{}}\n{hijau} Now bot working... {putih}Press {kuning}'K'{putih} on the keyboard to pause.{reset}"
    pause_message = f"{biru} Bot paused...\n{putih} Press {kuning}'K'{putih} again on the keyboard to continue{reset}"
    continue_message = f"{biru} Bot continue working...{reset}"
elif language_choice == 2:
    window_input = f"\n{putih} [?] | Masukin Window nya {hijau}(1 - TelegramDesktop): {reset}"
    window_not_found = f"{putih} [>] | Window - {{}} {kuning}gak di temukan!{reset}"
    window_found = f"{hijau} [>] | Window ditemukan - {{}}\n{hijau} Sekarang bot berjalan... {putih}Pencet {kuning}'K' {putih}di keyboard buat jeda.{reset}"
    pause_message = f"{biru} Bot terjeda... \n{putih}Pencet {kuning}'spasi'{putih} di keyboard buat lanjut lagi{reset}"
    continue_message = f'{biru} Bot ngelanjutin proses...{reset}'

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
    print(f" {putihmerah}EN:{reset}\n   {putihmerah}Make sure you use the TelegramDesktop application (not Telegram Web).{reset}\n   {putihmerah}And have opened the Blum bot on your TelegramDesktop.{reset}\n   {putihmerah}Until the Blum window is available{reset}")
    print(f" {putihmerah}ID:{reset}\n   {putihmerah}Pastikan kamu menggunakan aplikasi TelegramDesktop (bukan Telegram Web).{reset}\n   {putihmerah}Dan telah membuka Blum bot di TelegramDesktop kamu.{reset}\n   {putihmerah}Hingga tersedia window Blum nya{reset}")
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
                if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break
