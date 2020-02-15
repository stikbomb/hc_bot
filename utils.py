import random
from time import sleep

from ppadb.client import Client as AdbClient


def connect_device():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    device = devices[0]
    return device


def random_sleep(value='mid'):
    if value == 'min':
        sleep(random.randrange(300, 600) / 1000)
    elif value == 'mid':
        sleep(random.randrange(2100, 4300) / 1000)
    elif value == 'max':
        sleep(random.randrange(4500, 7000) / 1000)
    else:
        sleep(1)


def tap(device, x, y):
    device.shell('input tap {} {}'.format(x, y))


def swipe(device, template):
    gifts_swipe_template = [
        random.randrange(1300, 1700),
        random.randrange(1000, 1100),
        random.randrange(1300, 1700),
        random.randrange(1000, 1100) - 500 - random.randrange(-3, 3),
        1000
    ]
    map_swipe_template_right = [
        random.randrange(300, 900),
        random.randrange(1000, 1100),
        random.randrange(2600, 2900),
        random.randrange(1000, 1100) - random.randrange(-3, 3),
        200
    ]
    map_swipe_template_left = [
        random.randrange(2600, 2900),
        random.randrange(1000, 1100),
        random.randrange(300, 900),
        random.randrange(1000, 1100) - random.randrange(-3, 3),
        200
    ]

    if template == 'gifts':
        x1, y1, x2, y2, sss = gifts_swipe_template
    elif template == 'map_right':
        x1, y1, x2, y2, sss = map_swipe_template_right
    elif template == 'map_left':
        x1, y1, x2, y2, sss = map_swipe_template_left

    device.shell('input swipe {} {} {} {} {}'.format(x1, y1, x2, y2, sss))