import pyautogui as pag
import time

class AutoClicker(object):

    def __init__(self, sleep=3, interval=3):
        self.sleep = sleep
        self.interval = interval

    def wait(self, sleep=None):

        sleep = self.sleep if sleep is None else sleep

        print(f'Waiting {sleep} seconds...')
        time.sleep(sleep)

    def get_button_center(self, image, grayscale=False):

        button_center = pag.locateCenterOnScreen(image, grayscale=grayscale)
        return button_center

    def get_button_box(self, image):

        button_box = pag.locateOnScreen(image)
        return button_box

    def click_location(self, x, y, interval=None, debug=False):

        interval = self.interval if interval is None else interval

        pag.click(x, y, interval=interval)

        if debug:
            print(x, y)

    def click_button(self, image, button='left', debug=False, interval=None, grayscale=False):

        interval = self.interval if interval is None else interval

        button_center = self.get_button_center(image, grayscale=grayscale)
        pag.click(x=button_center.x, y=button_center.y, interval=interval, button=button)

        time.sleep(self.sleep)

        if debug:
            print(button_center)

    def click_next_to(self, image, direction='right', distance='width', scale=0.5, debug=False):

        button_box = self.get_button_box(image)

        if direction == 'right':
            x_edge = button_box.left + button_box.width
            y_edge = button_box.top + button_box.height / 2

            x_click = x_edge + button_box.width / 2
            y_click = y_edge

            self.click_location(x_click, y_click)
