import random

from actions import do_routine, tap_to_template_portal, do_portal_routine, tap_to_template
from utils import swipe, random_sleep, tap
from cv import check_template


def do_invasion(device):
    i = 0
    do_routine(device, [('map', 'min')])
    swipe(device, 'map_right')

    routine = [
        ['invasion_map_icon', 'min'],
        ['invasion2', 'min'],
        ['fight', 'max'],
        ['home', 'max'],
        ['map', 'mid']
    ]

    while i != 10:
        while check_template(device, 'invasion_map_icon'):
            do_routine(device, routine)
            i += 1
            continue

        swipe(device, 'map_left')


def do_gift():
    pass


def do_portal(device):
    routine1 = [
        ('map', 'min'),
        ('portal', 'min')
    ]
    do_routine(device, routine1)
    routine2 = [
        ('lock', 'max'),
        ('fight', 'max'),
        ('home', 'mid')
    ]
    while True:
        tap_to_template_portal(device, 'lock')
        random_sleep('min')
        tap_to_template(device, 'fight')
        random_sleep('min')
        if check_template(device, 'warning_health'):
            tap_to_template(device, 'yes')
        tap_to_template(device, 'home')
        random_sleep('mid')
# def do_gifts(device):
#     tap_to_template(device, 'kubok')
#     random_sleep('min')
#     tap_to_template(device, 'friends')
#     random_sleep('min')
#     #TODO добавить цикл
#     #TODO нормально делать скриншот
#     count = 0
#     while count != 20:
#         while check_template(device, 'gift'):
#             tap_to_template(device, 'gift')
#             random_sleep('min')
#             tap_to_template(device, 'send')
#             random_sleep('mid')
#             count += 1
#         swipe(device, 'gifts')
#
#
# do_gifts()
#


def do_bay(device, waves):
    # routine1 = [
    #     ('map', 'min'),
    #     ('new_bay', 'min')
    # ]
    # do_routine(device, routine1)
    i = 0
    # while True:
    while i != waves:
        tap_to_template(device, 'fight_bay')
        while check_template(device, 'fight_bay') is False:
            tap(device, 430 + random.randrange(-10, 10) / 2,
                375 + random.randrange(-10, 10) / 2)
        i += 1
