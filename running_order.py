import pyautogui
import cv2
import numpy as np

def match_image_with_screen(reference_image_path, threshold=0.95):
    # Load the reference image
    reference_image = cv2.imread(reference_image_path)

    # Capture a screenshot of the screen
    # screenshot = np.array(cv2.screenshot())
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    # Convert the reference image to grayscale
    reference_image_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)



    result = cv2.matchTemplate(screenshot_gray, reference_image_gray, cv2.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(cv2.minMaxLoc(result))




# Example usage
needle = r'C:/Users/Jason/Desktop/python/MultiViewer_Formula_1/png/ALO.png'
match_image_with_screen(needle)
