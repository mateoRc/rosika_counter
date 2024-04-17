import time
from rosika_2025.repository import timer_repo
from rosika_2025.service.timer import Timer
from rosika_2025.service.event import Event

timer = Timer()


class TimerService:
    pressed_button = None

    def __init__(self):
        pass

    def button_clicked(self, pos):
        timestamp = str(time.time())
        print("timer;" + pos + " at " + timestamp)
        if pos == "LEFT":
            button_id = 1
        elif pos == "RIGHT":
            button_id = 2
        else:
            raise Exception("dude")
        self.pressed_button = button_id
        timer_repo.store_btn_clicked_event(Event(button_id, timestamp, False))
        timer.start_timer(button_id)


