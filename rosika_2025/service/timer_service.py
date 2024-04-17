import time
from rosika_2025.repository import timer_repo
from rosika_2025.service.timer import Timer

timer = Timer()


def button_clicked(pos):
    timestamp = str(time.time())
    print("timer;" + pos + " at " + timestamp)
    if pos == "LEFT":
        button_id = 1
    elif pos == "RIGHT":
        button_id = 2
    else:
        raise Exception("dude")
    timer_repo.store_btn_clicked_event(Event(button_id, timestamp))
    timer.start_timer(button_id)


class Event:
    def __init__(self, btn_id, timestamp):
        self.button_id = btn_id
        self.timestamp = timestamp
