import random

from cv import check_template

from utils import connect_device, random_sleep, tap, swipe



from utils import connect_device
from activities import do_invasion, do_portal, do_bay
from cv import get_screenshot


device = connect_device()
# do_invasion(device)
# get_screenshot(device)
# do_portal(device)
do_bay(device, 12)