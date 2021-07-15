import math
import random
import os
import time
import tkinter.font
from tkinter import *
import pyautogui
import pyperclip

main = Tk()

main.title('m-Boom by Rifat')
main.geometry('800x700')
main.resizable(False, False)
p1 = PhotoImage(file='image/p1.png')
main.iconphoto(False, p1)
main.config(bg='#edd8d5')
p2 = PhotoImage(file='image/p2.png')
label1 = Label(main, image=p2)
label1.configure(background='#edd8d5')
label1.grid()

font_main = tkinter.font.Font(size=16, weight='bold', family='Ubuntu')
font_menu = tkinter.font.Font(size=10, weight='bold', family='MS Sans Serif')
font_text = tkinter.font.Font(size=12, weight='bold', family='MS Serif')
font_rifat = tkinter.font.Font(size=13, family='MS Serif', weight='bold')
font_suc = tkinter.font.Font(size=70, family='Modern', weight='bold')

Label(main, text='by Rifat', font=font_rifat, bg='#edd8d5', fg='#9d5925').place(x=690, y=105)


def success():
    successful = Toplevel(main)
    successful.title('Successful!')
    successful.geometry('600x400')
    successful.resizable(True, True)
    successful.config(bg='#edd8d5')
    p1 = PhotoImage(file='image/p1.png')
    successful.iconphoto(False, p1)
    label2 = Label(successful, text='Message Sent!', font=font_suc, bg='#edd8d5', fg='#d96714')
    label2.place(x=50, y=110)
    pyautogui.keyDown('alt')
    pyautogui.press('space')
    pyautogui.keyUp('alt')
    pyautogui.hotkey('n')


input_text_var = StringVar()

spaces = 40
spaces_msg = 30


def plain_text():
    for i in range(number_of_msg):
        pyperclip.copy(input_text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.press('enter')
    success()


def split_word():
    input_text_2 = input_text.split()
    for i in range(int(number_of_msg / len(input_text_2))):
        for char in range(len(input_text_2)):
            pyperclip.copy(input_text_2[char])
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')
    success()


def send_story():
    lines = input_text.splitlines()

    for line in lines:
        letters = list(line)
        for letter in letters:
            pyperclip.copy(letter)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
        pyautogui.press('enter')
    success()


def countdown(count):
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        main.after(1000, countdown, count - 1)

    if count < 1:
        main.withdraw()
        if confirm == 2:
            plain_text()
        if confirm == 3:
            split_word()
        if confirm == 4:
            sine_msg()
        if confirm == 5:
            cossine_msg()
        if confirm == 6:
            v_msg()
        if confirm == 7:
            randoms_msg()
        if confirm == 8:
            send_story()


def result():
    global results, texts
    results = Toplevel(main)
    results.iconphoto(False, p1)
    results.geometry('600x700')
    results.title('Result')
    results.config(bg='#edd8d5')
    texts = Text(results)
    texts.place(x=50, y=20, height=600, width=485)
    Label(results, text='You can copy result and paste anywhere.', font=font_text, bg='#edd8d5').place(x=130, y=630)


def finish_button():
    Button(text='Go to Result', font=font_menu, bg='#9d5925', command=main.withdraw).place(x=350, y=600)


def sine():
    result()
    for angle in range(0, 360, 10):
        space = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle / 10) % len(text))
        texts.insert(END, (int(spaces / 2) + space) * ' ' + text[serial])
        texts.insert(END, '\n')
    finish_button()
    results.mainloop()


def sincos():
    result()
    for angle in range(0, 180, 10):
        space1 = int((spaces / 2) * math.sin(math.radians(angle + 180)))
        space2 = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle / 10) % len(text))
        texts.insert(END,
                     (int(spaces / 2) + space1) * ' ' + text[serial] + (
                             (int(spaces / 2)) - 15 - space1 + space2) * ' ' + text[
                         serial])
        texts.insert(END, '\n')
    for angle in range(0, 180, 10):
        space1 = int((spaces / 2) * math.sin(math.radians(angle + 180)))
        space2 = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle / 10) % len(text))
        texts.insert(END,
                     (int(spaces / 2) + space1) * ' ' + text[serial] + (
                             (int(spaces / 2)) - 15 - space1 + space2) * ' ' + text[
                         serial])
        texts.insert(END, '\n')
    finish_button()
    results.mainloop()


def v():
    result()
    for i in range(12):
        serial = int(i % len(text))
        texts.insert(END, i * ' ' + text[serial] + i * '  ' + text[serial])
        texts.insert(END, '\n')
    for j in range(11, -1, -1):
        serial = int(j % len(text))
        texts.insert(END, j * ' ' + text[serial] + j * '  ' + text[serial])
        texts.insert(END, '\n')
    for i in range(12):
        serial = int(i % len(text))
        texts.insert(END, i * ' ' + text[serial] + i * '  ' + text[serial])
        texts.insert(END, '\n')
    for j in range(11, -1, -1):
        serial = int(j % len(text))
        texts.insert(END, j * ' ' + text[serial] + j * '  ' + text[serial])
        texts.insert(END, '\n')
    finish_button()
    results.mainloop()


def randoms():
    choice = random.randint(1, 3)
    if choice == 1:
        sine()
    if choice == 2:
        v()
    if choice == 3:
        sincos()


def submit_1():
    global p3, p4, p5, text
    input_text = input_text_var.get()
    text = input_text.split()
    p3 = PhotoImage(file='image/p3.png')
    p4 = PhotoImage(file='image/p4.png')
    p5 = PhotoImage(file='image/p5.png')
    Label(text='Select a Shape from below or ', font=font_text, bg='#edd8d5').place(x=10, y=320)
    Button(main, text='Randomize All Shape', font=font_menu, bg='#cd7636', command=randoms).place(x=238, y=320)
    Button(main, image=p3, command=sine).place(x=70, y=355)
    Button(main, image=p4, command=sincos).place(x=300, y=355)
    Button(main, image=p5, command=v).place(x=530, y=355)
    Label(main, text='You can click more than one time for more output', font=font_rifat, bg='#edd8d5').place(x=180,
                                                                                                              y=530)


def text():
    Label(main, text='Texts for Design', font=font_text, bg='#edd8d5').place(x=10, y=243)
    a = Entry(main, textvariable=input_text_var)
    a.place(x=15, y=265, height=28, width=250)
    input_text_var.set('Example: Happy Birthday')
    Button(main, text='Submit', font=font_menu, bg='#cd7636', command=submit_1).place(x=270, y=265)


def submit_2_1():
    global label
    Label(main, text='Your Messages sending in    Seconds. Go to Chat box and put Cursor there', font=font_text,
          bg='#edd8d5').place(x=100, y=560)
    label = Label(main, font=font_text, bg='#edd8d5', fg='red')
    label.place(x=299, y=560)
    countdown(9)


def submit_2():
    global input_text, number_of_msg
    input_text = input_text_var.get()
    number_of_msg = number_of_msg_var.get()
    number_of_msg = int(number_of_msg)
    Label(main, text='Minimize this window and open your chat box where you type and send message automatically.',
          font=font_rifat, bg='#edd8d5', fg='#d16e26').place(x=50, y=450)
    Label(main, text='Then back here and when you ready', font=font_rifat, bg='#edd8d5', fg='#d16e26').place(x=170,
                                                                                                             y=490)
    Button(main, text='Click here', font=font_menu, bg='#cd7636', command=submit_2_1).place(x=450, y=490)


def submit_2_1_msg():
    global label
    Label(main, text='Your Messages sending in    Seconds. Go to Chat box and put Cursor there', font=font_text,
          bg='#edd8d5').place(x=100, y=540)
    label = Label(main, font=font_text, bg='#edd8d5', fg='red')
    label.place(x=299, y=540)
    countdown(9)


def submit_2_msg():
    global input_text_2, number_of_msg
    input_text = input_text_var.get()
    input_text_2 = input_text.split()
    number_of_msg = number_of_msg_var.get()
    number_of_msg = int(number_of_msg)
    Label(main, text='Minimize this window and open your chat box where you type and send message automatically.',
          font=font_rifat, bg='#edd8d5', fg='#d16e26').place(x=50, y=600)
    Label(main, text='Then back here and when you ready', font=font_rifat, bg='#edd8d5', fg='#d16e26').place(x=170,
                                                                                                             y=620)
    Button(main, text='Click here', font=font_menu, bg='#cd7636', command=submit_2_1_msg).place(x=450, y=620)


def sine_msg():
    for numb in range(number_of_msg):
        for angle in range(0, 360, 10):
            space = int((spaces_msg / 2) * math.sin(math.radians(angle)))
            serial = int((angle / 10) % len(input_text_2))
            pyperclip.copy('.' + (int(spaces / 2) + space) * ' ' + input_text_2[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.20)
            pyautogui.press('enter')


def cossine_msg():
    for numb in range(number_of_msg):
        for angle in range(0, 180, 10):
            space1 = int((spaces_msg / 2) * math.sin(math.radians(angle + 180)))
            space2 = int((spaces_msg / 2) * math.sin(math.radians(angle)))
            serial = int((angle / 10) % len(input_text_2))
            pyperclip.copy('.' + (int(spaces_msg / 2) + space1) * ' ' + input_text_2[serial] + (
                        (int(spaces / 2)) - 15 - space1 + space2) * ' ' + input_text_2[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')


def v_msg():
    for numb in range(number_of_msg):
        for i in range(12):
            serial = int(i % len(input_text_2))
            pyperclip.copy('.' + i * ' ' + input_text_2[serial] + i * '  ' + input_text_2[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')
        for j in range(11, -1, -1):
            serial = int(j % len(input_text_2))
            pyperclip.copy('.' + j * ' ' + input_text_2[serial] + j * '  ' + input_text_2[serial])
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.15)
            pyautogui.press('enter')


def randoms_msg():
    global number_of_msg
    number_of_msg_3 = number_of_msg
    number_of_msg = 1
    for numb in range(number_of_msg_3):
        choice = random.randint(1, 3)
        if choice == 1:
            sine_msg()
        if choice == 2:
            v_msg()
        if choice == 3:
            cossine_msg()


def text2():
    Label(main, text='Texts for Send', font=font_text, bg='#edd8d5').place(x=10, y=360)
    Entry(main, textvariable=input_text_var).place(x=15, y=385, height=28, width=250)
    input_text_var.set('Example: Happy Birthday')

    global number_of_msg_var, confirm
    number_of_msg_var = IntVar()
    Label(main, text='How many message you want to send?', font=font_text, bg='#edd8d5').place(x=350, y=360)
    Entry(main, textvariable=number_of_msg_var).place(x=355, y=385, height=28, width=80)
    number_of_msg_var.set(50)
    confirm = 2

    Button(main, text='Submit', font=font_menu, bg='#cd7636', command=submit_2).place(x=670, y=385)


def text3():
    Label(main, text='Line for Send', font=font_text, bg='#edd8d5').place(x=10, y=360)
    Entry(main, textvariable=input_text_var).place(x=15, y=385, height=28, width=250)
    input_text_var.set('Example: Happy Birthday')

    global number_of_msg_var, confirm
    number_of_msg_var = IntVar()
    Label(main, text='How many message you want to send?', font=font_text, bg='#edd8d5').place(x=350, y=360)
    Entry(main, textvariable=number_of_msg_var).place(x=355, y=385, height=28, width=80)
    number_of_msg_var.set(50)
    confirm = 3

    Button(main, text='Submit', font=font_menu, bg='#cd7636', command=submit_2).place(x=670, y=385)


def sine_assign():
    global confirm
    confirm = 4


def cossine_assign():
    global confirm
    confirm = 5


def v_assign():
    global confirm
    confirm = 6


def randoms_assign():
    global confirm
    confirm = 7


def submit_shape_msg():
    global p3, p4, p5, text
    input_text = input_text_var.get()
    text = input_text.split()
    p3 = PhotoImage(file='image/p3.png')
    p4 = PhotoImage(file='image/p4.png')
    p5 = PhotoImage(file='image/p5.png')
    Label(text='Select a Shape from below or ', font=font_text, bg='#edd8d5').place(x=10, y=430)
    Button(main, text='Randomize All Shape', font=font_menu, bg='#cd7636', command=lambda: [randoms_assign(),
                                                                                            submit_2_msg()]).place(
        x=238, y=430)
    Button(main, image=p3, command=lambda: [sine_assign(), submit_2_msg()]).place(x=70, y=465)
    Button(main, image=p4, command=lambda: [cossine_assign(), submit_2_msg()]).place(x=300, y=465)
    Button(main, image=p5, command=lambda: [v_assign(), submit_2_msg()]).place(x=530, y=465)


def text4():
    Label(main, text='Texts for Design)', font=font_text, bg='#edd8d5').place(x=10, y=360)
    Entry(main, textvariable=input_text_var).place(x=15, y=385, height=28, width=250)
    input_text_var.set('Example: Happy Birthday')

    global number_of_msg_var, confirm
    number_of_msg_var = IntVar()
    Label(main, text='How many Shape you want to send?', font=font_text, bg='#edd8d5').place(x=350, y=360)
    Entry(main, textvariable=number_of_msg_var).place(x=355, y=385, height=28, width=80)
    number_of_msg_var.set(5)

    Button(main, text='Submit', font=font_menu, bg='#cd7636', command=submit_shape_msg).place(x=670, y=385)


def read_story():
    global input_text, confirm
    input_text = input_text_var.get('1.0', 'end')
    confirm = 8
    Label(main, text='Minimize this window and open your chat box where you type and send message automatically.',
          font=font_rifat, bg='#edd8d5', fg='#d16e26').place(x=50, y=500)
    Label(main, text='Then back here and when you ready', font=font_rifat, bg='#edd8d5', fg='#d16e26').place(x=170,
                                                                                                             y=530)
    Button(main, text='Click here', font=font_menu, bg='#cd7636', command=submit_2_1).place(x=450, y=530)


def text5():
    global input_text_var
    Label(main, text='Write or Paste Long Message here', font=font_text, bg='#edd8d5').place(x=10, y=360)
    input_text_var = Text(main)
    input_text_var.place(x=15, y=383, height=100, width=520)
    input_text_var.insert(END, 'This will split your long message in lines\nThen type line in editor with animation'
                               '\nThen send line to the receiver.\nExample: Here is total 5 lines.'
                               '\nIt will send 5 messages.')
    Button(main, text='Submit', font=font_menu, bg='#cd7636', command=read_story).place(x=540, y=455)


def send_msg():
    Label(main, text='Select Type for sending Message frequently', font=font_text, bg='#edd8d5').place(x=10, y=245)
    Button(main, text='Send only a word or line', bg='#cd7636', font=font_menu, command=text2).place(x=100, y=280)
    Button(main, text='Split line into word and send', bg='#cd7636', font=font_menu, command=text3).place(x=400, y=280)
    Button(main, text='Design in shape and send', bg='#cd7636', font=font_menu, command=text4).place(x=100, y=320)
    Button(main, text='Send a long message line by line', bg='#cd7636', font=font_menu, command=text5).place(x=400,
                                                                                                             y=320)


def start():
    Button(main, text='Design Text with Various Shape', command=text, font=font_menu, bg='#cd7636').place(x=150, y=200)
    Button(main, text='Send Frequent Message', font=font_menu, bg='#cd7636', command=send_msg).place(x=390, y=200)


Button(main, text='Start', command=start, bg='#9d5925', font=font_main).place(x=350, y=150)

main.mainloop()
