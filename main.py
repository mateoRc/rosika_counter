from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from rosika_2025.service import timer_service
from rosika_2025.database.database import SQLiteDatabase
from rosika_2025.config.config import Configuration


class RosikaApp(App):
    print("Rosika APP starting...")
    Configuration.load()
    SQLiteDatabase().init_db()

    class BoxLayoutTimerButtons(BoxLayout):
        def on_button_click(self, pos):
            timer_service.button_clicked(pos)

    class BoxLayoutExample(BoxLayout):
        pass


RosikaApp().run()
