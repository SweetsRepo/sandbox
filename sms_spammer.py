__author__ = "Christopher Sweet"
__version__ = 0.1
"""
SMS Spoofer is a script to spoof sms messages from various senders
"""

from clockwork import clockwork
import random

area_codes = [301, 311, 316, 210, 310, 365, 380, 401, 432, 447, 505, 512, 567]
api = clockwork.API("0e7f44b7bf646ccdf1361c37acd171ae4d1056da")

recipient = 0
sender = 0
#Build random sender number
rand_sender = int(str(area_codes[random.randint(0,12)]) + str(random.randint(0,585)) +
    str(random.randint(0,5000)))
msg = "Testing"
message = clockwork.SMS(from_name = sender, to = recipient, message = msg)
response = api.send(message)
