import cv2
import numpy as np


def get_screenshot(device):
    with open("tmp/screen.png", "wb") as fp:
        fp.write(device.screencap())


def check_template(device, template_name):
    template_full_path = "{}{}{}".format('src/', template_name, '.png')
    template = cv2.imread(template_full_path, cv2.IMREAD_GRAYSCALE)
    get_screenshot(device)
    screen = cv2.imread("tmp/screen.png", cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= 0.85)

    if loc[0].any():
        return loc, h, w

    return False
