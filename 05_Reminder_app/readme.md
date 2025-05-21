# Water Reminder App

This is a simple Python fun project desktop notification app that reminds you to drink water every hour.

## Project: 05_Reminder_app

### Features

- Sends a desktop notification every hour.
- Helps you stay hydrated with timely reminders.

### Requirements

- Python 3.x
- `plyer` module

You can install the required module using:

```bash
pip install plyer
```

### How It Works

The script runs an infinite loop and sends a notification every hour using the `plyer.notification` module.

### Code

```python
import time
from plyer import notification

while True:
    notification.notify(
        title = "Water Reminder!!",
        message = "Please drink some water",
    )
    time.sleep(60 * 60)  # Reminds every 1 hour
```

### GitHub

Repository: [Python-Projects](https://github.com/amansshrma/Python-Projects)  
Author: [amansshrma](https://github.com/amansshrma)

---

**Note**: This script must be running in the background to send hourly reminders. You can consider converting it to a background task or executable for continuous use.
