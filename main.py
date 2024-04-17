from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from rosika_2025.service.timer_service import TimerService
from rosika_2025.database.database import SQLiteDatabase
from rosika_2025.config.config import Configuration


class RosikaApp(App):
    print("Rosika APP starting...")
    Configuration.load()
    SQLiteDatabase().init_db()

    class BoxLayoutTimerButtons(BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.timer_service = TimerService()

        def on_button_click(self, pos):
            self.timer_service.button_clicked(pos)

    class BoxLayoutExample(BoxLayout):
        pass


RosikaApp().run()
