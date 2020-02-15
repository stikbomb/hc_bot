import random

from utils import random_sleep
from cv import check_template
from utils import tap


def tap_to_template(device, template_name):
    while check_template(device, template_name) is False:
        pass
    loc, h, w = check_template(device, template_name)
    print(loc)
    if loc[0].any():
        tap(device, loc[1][0] + random.randrange(w-10, w+10) / 2, loc[0][0] + random.randrange(h-10, h+10) / 2)
        print(device, loc[1][0] + w / 2, loc[0][0] + h / 2)
        return True
    return False


def tap_to_template_portal(device, template_name):
    while check_template(device, template_name) is False:
        pass
    loc, h, w = check_template(device, template_name)
    print(loc)
    if loc[0].any():
        tap(device, loc[1][-1] + random.randrange(w-10, w+10) / 2, loc[0][-1] + 300 + random.randrange(h-10, h+10) / 2)
        print(device, loc[-1][0] + w / 2, loc[0][-1] + h / 2)
        return True
    return False


def do_routine(device, routine):
    for step in routine:
        while tap_to_template(device, step[0]) is False:
            pass
        random_sleep(step[1])


def do_portal_routine(device, routine):
    for step in routine:
        while tap_to_template_portal(device, step[0]) is False:
            pass
        random_sleep(step[1])
