import pyautogui
import time
import pyperclip
import math
import random
import os
import time

def digsign():
    os.system('clear')
    print('''
     ____ ___ ____   ____ ___ ____ _   _ 
    |  _ \_ _/ ___| / ___|_ _/ ___| \ | |
    | | | | | |  _  \___ \| | |  _|  \| |
    | |_| | | |_| |  ___) | | |_| | |\  |
    |____/___\____| |____/___\____|_| \_|
                   \033[91mMade by:  \033[93mRIFAT
    ''')
    time.sleep(1)
    print("\033[95mLoading", flush=True, end='')
    for i in range(3):
        time.sleep(0.5)
        print('.', flush=True, end='')
    print("\n\n")
    spaces = 30



    def sine():
        for angle in range(0, 360, 10):
            space = int((spaces / 2) * math.sin(math.radians(angle)))
            serial = int((angle/10) % len(text))
            pyperclip.copy('.'+(int(spaces / 2) + space) * ' ' + text[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')


    def v():
        for i in range(12):
            serial = int(i % len(text))
            pyperclip.copy('.'+i * ' ' + text[serial] + i * '  ' + text[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')
        for j in range(11, -1, -1):
            serial = int(j % len(text))
            pyperclip.copy('.'+j * ' ' + text[serial] + j * '  ' + text[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')


    def sincos():
        for angle in range(0, 180, 10):
            space1 = int((spaces / 2) * math.sin(math.radians(angle + 180)))
            space2 = int((spaces / 2) * math.sin(math.radians(angle)))
            serial = int((angle/10) % len(text))
            pyperclip.copy('.'+(int(spaces / 2) + space1) * ' ' + text[serial] + ((int(spaces / 2)) - 15 - space1 + space2) * ' ' + text[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')


    def randoms():
        choice = random.randint(1, 3)
        if choice == 1:
            sine()
        if choice == 2:
            v()
        if choice == 3:
            sincos()


    repeat ='y'
    while repeat =='y':
        word = input("\033[96m[?] Enter the sentence that you want to design and send frequently \033[91m(Example: Happy Birthday) \033[93m:")
        print(" ")
        text = word.split()
        choices = input('\033[96mWhat type? \n\033[91m[s] Sine shape (Look ike a snake)\n[sc] Sine Cosine shape (Look like a snake and a reverse) \n[v] V shape (Look like "V")\n[r] Random (Randomize previous shapes)\n \033[93m\n[?] ')
        print(" ")
        num = int(input("\033[96m[?] How much? \033[91m(Enter a number like '2' or anything. Higher number give a long output): \033[93m"))
        os.system('clear')

        print("\033[91m Starting in 5 second. Go to typewriter.", flush=True, end='')
        for i in range(5):
            time.sleep(1)
            print('.', flush=True, end='')

        for i in range(num):
            if choices == 'r':
                randoms()
            if choices == 's':
                sine()
            if choices == 'sc':
                sincos()
            if choices == 'v':
                v()
        print('\n')
        repeat = input('Do you want to repeat \033[96mDigsign? (y/n):\n\033[91m')

def plain_text():
    repeat ='y'
    while repeat =='y':
        text = input('Enter a sentence here that you want to send frequently:')
        numb = int(input('How much message you want to sent:'))
        print("\033[91m Starting in 5 second. Go to typewriter.", flush=True, end='')
        for i in range(5):
            time.sleep(1)
            print('.', flush=True, end='')
        for i in range(numb):
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.15)
            pyautogui.press('enter')

        print('\n')
        repeat = input('Do you want to repeat \033[96mPlain text?(y/n): \n\033[91m')

def split_word():
    repeat ='y'
    while repeat =='y':
        text = input('Enter full sentence that you want to send frequently:')
        words =text.split()
        numb = int(input('How much message you want to send:'))
        print("\033[91m Starting in 5 second. Go to typewriter.", flush=True, end='')
        for i in range(5):
            time.sleep(1)
            print('.', flush=True, end='')
        for i in range(numb):
            for word in words:
                pyperclip.copy(word)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.15)
                pyautogui.press('enter')

        print('\n')
        repeat = input('Do you want to repeat \033[96mSplit word? \n\033[91m(y/n):')

os.system('clear')
print('''
 __  __       ____   ___   ___  __  __
|  \/  |     | __ ) / _ \ / _ \|  \/  |
| |\/| |_____|  _ \| | | | | | | |\/| |
| |  | |_____| |_) | |_| | |_| | |  | |
|_|  |_|     |____/ \___/ \___/|_|  |_|
                \033[91mMade by:  \033[93mRIFAT
''')

repeats ='y'
while repeats =='y':
    os.system('clear')
    types = input('\033[96mWhat type of frequent message you want to send? \n\033[91m[1] Plain texts \033[95m(It will send a single sentence frequently)\n\n\033[91m[2] Split Word \033[95m(It will split sentence to words and sent word separately) \n\n\033[91m[3] DigSign \033[95m(It will design the words in various shape and sent frequently) \n \033[93m\n[?] ')
    if types =='1':
        plain_text()
    if types =='2':
        split_word()
    if types =='3':
        digsign()
    repeats =input('Do you want to repeat this program? (y/n):')
