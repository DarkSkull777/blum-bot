# BLUM Airdrop Auto Click - Origin version
# Made by Dymles Ganz
# Recoded by yourname

from pyautogui import *
import sys
import subprocess
import pyautogui
import time
from termcolor import colored
from pynput import keyboard
import time
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

# ------------------ FUNCTIONS ------------------
def find_and_activate_window(window_name):
    platform = sys.platform
    window_rect = None

    if platform == "win32":
        import pygetwindow as gw
        # Finding windows with a title
        windows = gw.getWindowsWithTitle(window_name)
        if windows:
            telegram_window = windows[0]
            window_rect = (
                telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
            )
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

    elif platform == "darwin":
        # AppleScript for Mac OS window activation
        script = f"""
        tell application "System Events"
            set winList to every window of every process whose name is "{window_name}"
            if (count of winList) > 0 then
                set frontmost of first item of winList to true
                return properties of window 1 of process "{window_name}"
            end if
        end tell
        """
        process = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        output = process.stdout.strip()
        if "window" in output:
            pass

    elif platform.startswith("linux"):
        try:
            # Using wmctrl and xwininfo for get window info in Linux
            result = subprocess.run(['wmctrl', '-l'], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if window_name in line:
                    window_id = line.split(None, 1)[0]
                    # Window activation
                    subprocess.run(['wmctrl', '-i', '-a', window_id])

                    # Window size request
                    win_info = subprocess.run(['xwininfo', '-id', window_id], capture_output=True, text=True).stdout
                    for info_line in win_info.splitlines():
                        if "Absolute upper-left X" in info_line:
                            x = int(info_line.split(":")[1].strip())
                        elif "Absolute upper-left Y" in info_line:
                            y = int(info_line.split(":")[1].strip())
                        elif "Width" in info_line:
                            width = int(info_line.split(":")[1].strip())
                        elif "Height" in info_line:
                            height = int(info_line.split(":")[1].strip())
                    window_rect = (x, y, width, height)
                    break
        except FileNotFoundError:
            print(wmctrl_xwininfo_err_msg)
    
    return window_rect

def take_screenshot(window_rect):
    if window_rect:
        scrn = pyautogui.screenshot(region=window_rect)
        scrn.save("screenshot.png")
    else:
        print(fail_capture_msg)

    return scrn

# Инициализация переменных
paused = False
def on_press(key):
    global paused
    try:
        if key.char.lower() == 'k':  # Используем char.lower() чтобы обрабатывать и 'k', и 'K'
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)  # Исключаем повторное нажатие
    except AttributeError:
        # В случае, если нажатая клавиша не имеет атрибута char, просто пропускаем
        pass

def anjaymabar():
    print(f"""{hijau}
  {hijau}|      |                         {kuning}  |             |   
  {hijau}__ \\   |  |   |  __ `__ \\        {kuning}  __ \\    _ \\   __| 
  {hijau}|   |  |  |   |  |   |   | {merah}_____|{kuning}  |   |  (   |  |   
 {hijau}_.__/  _| \\__,_| _|  _|  _|       {kuning} _.__/  \\___/  \\__| {reset}
    """)

# ------------------ MAIN ------------------
anjaymabar()
print(f" {putihmerah}Author: Dymles Ganz{reset}")
print(f" {putihhijau}Contact on telegram: @BraveXploiter{reset}")
print(f" {kuning}Donations USDT (TRC20):{putih} TYna9WAoVCAF2f7ynnjS2bQixkLQz8XxFh{reset}")
print()
print(colored("  ...:::: CHOOSE LANGUAGE ::::...", 'light_cyan'))
print(colored("  [ ", 'white') + colored("1 ", 'light_green') + colored("] ", 'white') + colored("English", 'light_yellow'))
print(colored("  [ ", 'white') + colored("2 ", 'light_green') + colored("] ", 'white') + colored("Bahasa Indonesia", 'light_yellow'))
print(colored("  [ ", 'white') + colored("3 ", 'light_green') + colored("] ", 'white') + colored("Русский", 'light_yellow'))

while True:
    try:
        language_choice = int(input(f"\n  {putih}blum.bot@main:~# {reset}"))
        if language_choice in [1, 2, 3]:
            break
        else:
            print(f"{merah} Yo bro wrong choose. You can input {kuning}1 {merah}or {kuning}2{merah}.{reset}")
    except ValueError:
        print(f" {merah}What??? your input not valid. Please enter number {kuning}1 {merah}, {kuning}2 {merah} or {kuning}3 {merah}bro.{reset}")

'''Need to fix'''
if language_choice == 1:
    wmctrl_xwininfo_err_msg = f"{putih}wmctrl or xwininfo is not installed. Please install them using your package manager{reset}"
    fail_capture_msg = f"{putih}Failed to capture window region{reset}"
    close_bot_msg = f"{putih}The bot was closed{reset}"
    pause_message = f"{putih}Paused"
    continue_message = f"{putih}Continuing"
    window_input = f"\n{putih} [?] | Enter Window {hijau}(1 - TelegramDesktop){putih}: {reset}"
    window_not_found = f"{putih} [>] | Your Window - {{}} {kuning}not found!{reset}"
    window_found = f"{hijau} [>] | Window found - {{}}\n{hijau} Now bot working... {putih}Press {kuning}'K'{putih} on the keyboard to pause.{reset}"
    pause_message = f"{biru} Bot paused...\n{putih} Press {kuning}'K'{putih} again on the keyboard to continue{reset}"
    continue_message = f"{biru} Bot continue working...{reset}"
    adv_msg = f"{biru}Make sure that you using app {{}} (не Telegram Web).\nAnd your Blum bot is opened in {{}}{reset}"
elif language_choice == 2:
    pause_message = "Paused"
    continue_message = "Continuing"
    window_input = f"\n{putih} [?] | Masukin Window nya {hijau}(1 - TelegramDesktop): {reset}"
    window_not_found = f"{putih} [>] | Window - {{}} {kuning}gak di temukan!{reset}"
    window_found = f"{hijau} [>] | Window ditemukan - {{}}\n{hijau} Sekarang bot berjalan... {putih}Pencet {kuning}'K' {putih}di keyboard buat jeda.{reset}"
    pause_message = f"{biru} Bot terjeda... \n{putih}Pencet {kuning}'spasi'{putih} di keyboard buat lanjut lagi{reset}"
    continue_message = f'{biru} Bot ngelanjutin proses...{reset}'
elif language_choice == 3:
    wmctrl_xwininfo_err_msg = f"{putih}wmctrl или xwininfo не установлены. Установите их через пакетный менеджер.{reset}"
    fail_capture_msg = f"{putih}Не могу найти окно для захвата{reset}"
    close_bot_msg ="Бот был закрыт"
    pause_message = "Пауза"
    continue_message = "Продолжаю"
    window_input = f"\n{putih} [?] | Введите окно {hijau}(1 - TelegramDesktop){putih}: {reset}"
    window_not_found = f"{putih} [>] | Окно - {{}} {kuning}не найдено!{reset}"
    window_found = f"{hijau} [>] | Окно найдено - {{}}\n{hijau} Бот работает... {putih}Нажмите кнопку {kuning}'K'{putih} чтобы продолжить{reset}"
    pause_message = f"{biru} Бот приостановлен...\n{putih} Нажмите кнопку {kuning}'K'{putih} чтобы продолжить{reset}"
    continue_message = f"{biru}Бот продолжает работу...{reset}"
    adv_msg = f"Убедитесь, что вы используете приложение {{}} (не Telegram Web).\nИ что Blum бот открыт в вашем {{}}"

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

if window_name == '2':
    window_name = "KotatogramDesktop"

if not find_and_activate_window(window_name):
    print(window_not_found.format(window_name))
    print(adv_msg.format(window_name, window_name))
else:
    print (find_and_activate_window(window_name))
    print(window_found.format(window_name))
    paused = False

    # Running listner
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    # Main application circle
    try:
        while True:
            if paused:
                continue
            window_rect = find_and_activate_window(window_name)
            try:
                scrn = take_screenshot(window_rect)
            except UnboundLocalError:
                print (close_bot_msg)
                os._exit(0)
            
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
            time.sleep(0.1)
    except KeyboardInterrupt:
        # For correct user break
        pass
    finally:
        listener.stop()