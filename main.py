import random
import pyautogui
import time

keys = ["w", "a", "s", "d", "space", "shift"]
mouse = ["left", "right"]


class term_color:
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def mode_selection():
    available_selection = [1, 2]
    while True:
        try:
            selection = int(input(
                "Select your anti-AFK mode\n" +
                "[1] Social (Teams,Skype,Discord) This mode moves the mouse every interval you specified. \n" +
                "[2] Games (Minecraft,CSGO....) This mode moves the mouse and presses movement keys (WASD) every interval you specified.\n"
                ">>> "))
            if available_selection.__contains__(selection):
                return selection
            else:
                raise ValueError
        except ValueError:
            print(f"{term_color.FAIL}Chose a valid number from the list{term_color.ENDC}")


def seconds_interval():
    while True:
        try:
            second_selection = int(input("Select every how many seconds it will repeat \n>>> "))
            if isinstance(second_selection, int):
                return second_selection
            else:
                raise ValueError
        except ValueError:
            print(f"{term_color.FAIL}Value must be a number{term_color.ENDC}")


def main():
    try:
        mode = mode_selection()
        seconds_to_repeat = seconds_interval()
        print()
        failsafe_question = input("[y or n] Enable failsafe? Potentially problematic.\n>>> ").lower()
        time.sleep(5)
        pixel_color_initial = pyautogui.pixel(804, 972) #<<< This line could be causing some trouble, consider playing around with co-ordinates if you want the failsafe.
        while True:

            pixel_color_now = pyautogui.pixel(804, 972)
            if failsafe_question == "y":
                pixel_color_now = pyautogui.pixel(804, 972)

            elif failsafe_question == "n":
                pixel_color_now = pixel_color_initial

            if pixel_color_now == pixel_color_initial:
                if mode == 1:
                    randx = random.randint(-500, 500)
                    randy = random.randint(-50, 50)
                    current_mouse_x, current_mouse_y = pyautogui.position()
                    pyautogui.moveTo(current_mouse_x + randx, current_mouse_y + randy, 1)
                elif mode == 2:
                    randx = random.randint(-500, 500)
                    randy = random.randint(-50, 50)
                    current_mouse_x, current_mouse_y = pyautogui.position()
                    pyautogui.moveTo(current_mouse_x + randx, current_mouse_y + randy, 1)
                    ran = random.randint(-5, 10)
                    rand_kb = random.randint(0, len(keys) - 1)
                    rand_ms = random.randint(0, len(mouse) - 1)
                    press_and_depress_with_delay_keyboard(keys[rand_kb], 0.5 + (ran/10))
                    press_and_depress_with_delay_mouse(key=mouse[rand_ms], sleep=0.5 + (ran / 10))
                time.sleep(seconds_to_repeat)
            else:
                break
    except KeyboardInterrupt:
        pass


def press_and_depress_with_delay_keyboard(key, sleep):
    pyautogui.keyDown(key)
    time.sleep(sleep)
    pyautogui.keyUp(key)

def press_and_depress_with_delay_mouse(key, sleep):
    pyautogui.mouseDown(button=key)
    time.sleep(sleep)
    pyautogui.mouseUp(button=key)


if __name__ == "__main__":
    main()
