import time
from plyer import notification

while True:
    notification.notify(title = "Water Reminder!!", message = "Please drink some water",)
    time.sleep(60*60) #remind you in every 1Hr