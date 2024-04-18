import time
from rosika_2025.repository import timer_repo
from rosika_2025.service.timer import Timer
from rosika_2025.service.event import Event


class TimerService:
    pressed_button = None
    timer = None
    start_time = None

    points = 0

    def __init__(self):
        self.timer = Timer()
        pass

    def button_clicked(self, pos):
        self.start_time = time.time()
        print("timer;" + pos + " at " + str(self.start_time))
        if pos == "LEFT":
            button_id = 1
        elif pos == "RIGHT":
            button_id = 2
        else:
            raise Exception("dude")
        self.pressed_button = button_id
        timer_repo.store_btn_clicked_event(Event(button_id, str(self.start_time), False, event_type="btn_clicked"))
        self.timer.start_timer(button_id)

    def get_current_timer(self):
        if not self.timer:
            return None
        return self.timer.seconds

    def get_pressed_button(self):
        return self.pressed_button

    def update_points(self, duration=600):

        while True:
            current_time = time.time()
            elapsed_time = current_time - self.start_time

            if elapsed_time >= duration:
                print("Adding 1 point")
                self.points += 1
                print("Points:", self.points)
                self.start_time = time.time()  # Update start time after adding a point

                # Optional: Uncomment the break statement below if you want to stop after a certain number of points
                # if self.points >= MAX_POINTS:
                #     break

                timer_repo.store_points_event(Event(None, None, None, None))

            time.sleep(5)
