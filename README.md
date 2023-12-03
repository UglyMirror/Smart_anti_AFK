# Smart_anti_AFK

A smart anti-AFK script

## Abilities:

- Provides all the necessary actions to avoid AFK-induced kicks, including random pressing of WASD buttons, Shift, Space, and both mouse buttons.
- All actions and their durations are randomly selected.
- It has a crucial failsafe, namely the script can constantly check for sudden changes in constant variables within your screen. Specifically, it detects sudden color changes. If it detects one, it automatically stops the execution of the script to prevent any unintended actions (such as clicking outside the game).

## Usage:

1. Download the `main.py` file.
2. Run the script. A terminal should open, where you'll need to answer a couple of questions.
3. After answering, you have 5 seconds to switch to the game window where the script will be executed.

This script should generally work for all games as long as you have Python installed. However, be aware that you may need to install the PyAutoGUI module. To install it, open your command prompt on Windows and type:

```bash
pip install PyAutoGUI
