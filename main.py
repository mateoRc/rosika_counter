from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.label import Label

from rosika_2025.database.database import SQLiteDatabase
from rosika_2025.config.config import Configuration
from rosika_2025.service.result_scheduler import ResultScheduler
from rosika_2025.service.timer_service import TimerService


class RosikaApp(App):
    print("Rosika APP starting...")
    Configuration.load()
    SQLiteDatabase().init_db()

    class BoxLayoutTimerButtons(BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.timer_service = TimerService()
            self.result_scheduler = ResultScheduler()
            self.result_scheduler.start()
            Clock.schedule_interval(self.update_clock, 1)

        def on_button_click(self, pos):
            self.timer_service.button_clicked(pos)

        def update_clock(self, dt):
            # Update the value of the clock variable
            current_timer = self.timer_service.get_current_timer()
            pressed_button = self.timer_service.pressed_button
            self.parent.children[1].text = str(current_timer)
            print("clock: " + self.parent.children[1].text)
            if not pressed_button:
                return
            if current_timer > 0:
                return
            print("Gaining poits side: " + str(pressed_button))
            self.timer_service.update_points(10)

    class MainView(BoxLayout):
        pass


RosikaApp().run()
