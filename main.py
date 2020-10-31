
# here you can change your delay to what you want
delay = 1


# importing all the stuff we need

# pyautogui for typing the word and for hitting enter
import pyautogui
# time for the delay (we only need sleep)
from  time import sleep

# telling the user to enter the Word to Spam
print("Word to Spam")

# Getting the word to spam
word = input("$ ")

# telling the user it starts in 5 seconds
print("starting in 5 seconds")

# waiting 5 seconds
sleep(5)

# main Part

# making a infinite Loop
while True:
    # typing the word we specified in line 17
    pyautogui.typewrite(word)

    # hitting enter so it sends the message
    pyautogui.press('enter')

    # waiting as long as you told it to in line 3
    sleep(delay)