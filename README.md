# Smart_anti_AFK

A smart anti-AFK script

## Abilities:

- Provides all the necessary actions to avoid AFK-induced kicks, including random pressing of WASD buttons, Shift, Space, and both mouse buttons.
- All actions and their durations are randomly selected.
- Features a crucial failsafe: the script can constantly check for sudden changes in constant variables within your screen, specifically detecting sudden color changes. If it detects one, it automatically stops the execution of the script to prevent unintended actions (such as clicking outside the game).

## Usage:

1. Download the `main.py` file.
2. Run the script. A terminal should open, where you'll need to answer a couple of questions.
3. After answering, you have 5 seconds to switch to the game window where the script will be executed.
4. There could potentially be some trouble with color sampling of the script, so consider either:
    - A. Completely disabling the failsafe (not recommended)
    - B. Changing the coordinates of the sample pixel that it compares new ones to. To do that, go to line 48 of the code and change the values of `(804, 972)` to whatever pixel coordinates stay constant most of the time in your game. However, there is an embedded failsafe in PyAutoGUI. If you need to stop the program but can't use my failsafe, simply move the mouse to the upper right corner of your screen, and the program will stop the execution.

This script should generally work for all games as long as you have Python installed. However, be aware that you may need to install the PyAutoGUI module. To install it, open your command prompt on Windows and type:

```bash
pip install PyAutoGUI
```
P.S. I'd recommend setting the repeat time to a single second.

### **Godspeed lazy-goers!**


Feel free to use this updated version or make further modifications according to your preferences!


