import pyautogui as pag
from auto_clicker import AutoClicker
import time

pag.FAILSAFE = True

pag.confirm('Make sure PioSOLVER is visible on the screen.')

autoclicker = AutoClicker()

# Build Tree
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/Postflop_Tree_Building_and_Calculations.png', debug=True)
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/6maxBTNvsBB-SRP.png', debug=True)
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/Build_tree.png', debug=True)
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/Go.png', debug=True)
autoclicker.wait(30)
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/Stop.png', debug=True)

# Open Check -> 2c
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/Browser.png', debug=True)
autoclicker.click_next_to('/home/mike/projects/autogui/autogui/images/ROOT.png', debug=True)

autoclicker.click_button('/home/mike/projects/autogui/autogui/images/darkgreen__CHECK.png', debug=True, grayscale=True)
autoclicker.click_button('/home/mike/projects/autogui/autogui/images/2c.png', debug=True)
