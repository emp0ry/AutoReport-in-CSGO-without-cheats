#####################################################################
####################### Auto Report by emp0ry #######################
############## Tested on 1920x1080, 1280x1024, 1280x960 #############
### https://github.com/emp0ry/AutoReport-in-CS-GO-without-cheats/ ###
#####################################################################

# settings
CSGO_SCREENSHOT_FOLDER_PATH = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\screenshots' # csgo (f5) screenshot folder path
IS_CSGO_IN_FULLSCREEN = False # if your game is in fullscreen mode change to True
CSGO_SCREENSHOT_BIND = 'f5' # use (bind "f5" "jpeg screenshot 100") with default bind not working
BIND_TO_RUN_SCRIPT = 'tab + q' # press tab, click on the player you want to report and press 1 or 2 seconds q
CSGO_WINDOWS_NAME = 'Counter-Strike: Global Offensive - Direct3D 9' # csgo window name

import time
import os

try: import win32process
except: os.system("pip install pywin32");  import win32process
try: import pyautogui
except: os.system("pip install keyboard"); import pyautogui
try: import keyboard
except: os.system("pip install keyboard"); import keyboard
try: import win32gui
except: os.system("pip install win32gui"); import win32gui
try: import psutil
except: os.system("pip install psutil"); import psutil

# detect if you in csgo
def in_csgo():
    try:
        hwnd = win32gui.GetForegroundWindow()
        pid = win32process.GetWindowThreadProcessId(hwnd)[1]
        process = psutil.Process(pid).name()
        return True if process == 'csgo.exe' else False
    except:
        in_csgo()

# get csgo resolution
def csgo_resolution():
    try:
        hwnd = win32gui.FindWindow(None, CSGO_WINDOWS_NAME)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bottom - top

        return width, height
    except:
        time.sleep(0.5)
        csgo_resolution()

# mouse click event
def mouse_click(coords):
    for coord in coords:
        pyautogui.moveTo(coord)
        pyautogui.mouseDown()
        pyautogui.click()
        pyautogui.mouseUp()

def main():
    if not IS_CSGO_IN_FULLSCREEN:
        while True:
            try:
                if in_csgo and keyboard.is_pressed('tab + q'):
                    report_button_location = pyautogui.locateOnScreen(path+'\\img\\report.png', grayscale=True, confidence=0.8)
                    if report_button_location is not None and in_csgo():
                        report_button_center = pyautogui.center(report_button_location)
                        mouse_pos = pyautogui.position()
                        
                        width, height = csgo_resolution()
                        button1_coords = (width/1.549636803874092, height/2.640586797066015)
                        button2_coords = (width/1.549636803874092, height/2.302771855010661)
                        button3_coords = (width/1.549636803874092, height/2.041587901701323)
                        button4_coords = (width/1.549636803874092, height/1.833616298811545)
                        button5_coords = (width/1.549636803874092, height/1.664098613251156)
                        button_confirm_coords = (width/1.794392523364486, height/1.469387755102041)

                        mouse_click([report_button_center, button1_coords, button2_coords, button3_coords, button4_coords, button5_coords, button_confirm_coords])
                        print('Reported')
                        if keyboard.is_pressed('tab'):
                            mouse_click([mouse_pos])
                            print('clicked on the muted player')
                            voice_button_location = pyautogui.locateOnScreen(path+'\\img\\voice.png', grayscale=True, confidence=0.8)
                            if voice_button_location is not None:
                                voice_button_center = pyautogui.center(voice_button_location)
                                mouse_click([voice_button_center])
                                print('player unmuted')
                            else:
                                print('Voice Button not found :(')
                            keyboard.press_and_release('tab')
                    else:
                        print('Report Button not found or you are not in cs:go :(')
                        time.sleep(0.5)
                    print()
                else:
                    time.sleep(0.1)
            except:
                print('Error (def main)')
    else:        
        try:
            os.remove(CSGO_SCREENSHOT_FOLDER_PATH+'\\screenshot.jpg')
        except:
            pass
        while True:
            try:
                if in_csgo and keyboard.is_pressed('tab + q'):
                    try:
                        os.remove(CSGO_SCREENSHOT_FOLDER_PATH+'\\screenshot.jpg')
                    except:
                        pass
                    keyboard.press_and_release(CSGO_SCREENSHOT_BIND)
                    time.sleep(0.2)
                    report_button_location = pyautogui.locate(path+'\\img\\report2.png', CSGO_SCREENSHOT_FOLDER_PATH+'\\screenshot.jpg', grayscale=True, confidence=0.8)
                    try:
                        os.remove(CSGO_SCREENSHOT_FOLDER_PATH+'\\screenshot.jpg')
                    except:
                        pass
                    if report_button_location is not None and in_csgo():
                        report_button_center = pyautogui.center(report_button_location)
                        mouse_pos = pyautogui.position()
                        
                        width, height = csgo_resolution()
                        button1_coords = (width/1.549636803874092, height/2.640586797066015)
                        button2_coords = (width/1.549636803874092, height/2.302771855010661)
                        button3_coords = (width/1.549636803874092, height/2.041587901701323)
                        button4_coords = (width/1.549636803874092, height/1.833616298811545)
                        button5_coords = (width/1.549636803874092, height/1.664098613251156)
                        button_confirm_coords = (width/1.794392523364486, height/1.469387755102041)

                        mouse_click([report_button_center, button1_coords, button2_coords, button3_coords, button4_coords, button5_coords, button_confirm_coords])
                        print('Reported')
                        if keyboard.is_pressed('tab'):
                            mouse_click([mouse_pos])
                            print('clicked on the muted player')
                            keyboard.press_and_release('f5')
                            time.sleep(0.2)
                            voice_button_location = pyautogui.locate(path+'\\img\\voice2.png', CSGO_SCREENSHOT_FOLDER_PATH+'\\screenshot.jpg', grayscale=True, confidence=0.8)
                            try:
                                os.remove(CSGO_SCREENSHOT_FOLDER_PATH+'\\screenshot.jpg')
                            except:
                                pass
                            if voice_button_location is not None:
                                voice_button_center = pyautogui.center(voice_button_location)
                                mouse_click([voice_button_center])
                                print('player unmuted')
                            else:
                                print('Voice Button not found :(')
                            keyboard.press_and_release('tab')
                    else:
                        print('Report Button not found or you are not in cs:go :(')
                        time.sleep(0.5)
                    print()
                else:
                    time.sleep(0.1)
            except:
                print('Error (def main)')

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    main()