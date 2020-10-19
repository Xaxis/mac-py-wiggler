import time
from pynput import mouse
from pynput.mouse import Button, Controller as MouseController
mouseController = MouseController()
alt_pos = True
# The event listener will be running in this block
with mouse.Events() as events:

    # Iterate over out events
    for event in events:

        # Wiggle the mouse back and forth
        if hasattr(event, 'x'):
            time.sleep(5)

            # Move mouse back and forth
            if alt_pos == True:
                alt_pos = False
                mouseController.position = (100, 100)
            else:
                alt_pos = True
                mouseController.position = (-100, -100)

        # Print the event details
        print(event)
