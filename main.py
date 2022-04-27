import pyautogui
from telethon import TelegramClient, events, sync

Coin_name = (input("Coin name: "))
api_id = 12444392
api_hash = '6002b94f2240a52c07e068858d8cf47c'
client = TelegramClient('session_name', api_id, api_hash)
client.start()
channel_username = 't.me/hotbitpumpevents'

if Coin_name == "YA":
    for messages in client.get_messages(channel_username):
        pyautogui.click(x=133, y=160)
        pyautogui.sleep(0.05)
        pyautogui.write(messages.message)
        pyautogui.sleep(0.1)
        pyautogui.click(x=97, y=218)
        pyautogui.sleep(0.07)
        pyautogui.click(x=1083, y=586)
        pyautogui.sleep(0.07)
        pyautogui.click(x=1047, y=676)
        pyautogui.sleep(0.4)
        pyautogui.click(x=742, y=465)
        pyautogui.sleep(1.5)
        pyautogui.click(button='right', x=139, y=18)
        pyautogui.sleep(0.3)
        pyautogui.click(x=225, y=150)
        pyautogui.sleep(5)
        pyautogui.click(x=1347, y=585)
        pyautogui.sleep(0.1)
        pyautogui.doubleClick(x=256, y=199)
        pyautogui.sleep(0.2)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.sleep(0.1)
        pyautogui.doubleClick(x=1236, y=527)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(0.1)
        pyautogui.click(x=1234, y=676)
        pyautogui.sleep(0.3)
        pyautogui.click(x=742, y=465)
