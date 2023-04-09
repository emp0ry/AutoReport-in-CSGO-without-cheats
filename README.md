# AutoReport in CS:GO without cheats

### How to configure?
In the code, change the path to the folder with screenshots of csgo. (f5 screenshots)

For example
```python
CSGO_SCREENSHOT_FOLDER_PATH = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\screenshots'
```

If you playing in fullscreen change False to True
```python
IS_CSGO_IN_FULLSCREEN = True
```

#### \\/ If you playing in fullscreen mode \\/
• If you have csgo config change the screenshot bind to ```bind "f5" "jpeg screenshot 100"``` <br/>
• If you don't have a config write this command in the csgo console ```bind "f5" "jpeg screenshot 100"``` <br/>
• If you want to turn off the notification and screenshot sound, in cs:go press ```alt + tab``` then go to ```settings```>```in-Game```> in tab ```When a screenshot is taken``` turn off ```Display a notification``` and turn off ```Play a sound```

### How to use?
• Run ```main.py``` <br />
• In the tab, click on the player you want to report and press 1 or 2 seconds ```q``` <br/>
• If you don't want to ```unmute``` the player, when the script will report the player, release the ```tab```


<h3> PS: Tested on resolutions 1920x1080, 1280x1024, 1280x960 <h2/>
