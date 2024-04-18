import threading
import time


class Timer:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, seconds=5):
        self.start_time = seconds
        self.seconds = seconds
        self.current_button = None
        self.timer_thread = None
        self.timer_running = False
        self.timer_completed = False
        if not self._initialized:
            self._initialized = True
            print("timer initialized...")

    def start_timer(self, button_id):
        print("start_timer " + str(button_id))
        print(self.timer_running)
        print(self.timer_completed)
        if self.current_button == button_id:
            print("identical btn, ignored...")
            return

        self.timer_completed = False
        if self.timer_running:
            print("Stopping previous timer...")
            self.stop_timer()
        self.seconds = self.start_time
        self.timer_running = True
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.daemon = True
        self.current_button = button_id
        print("timer started!")

        self.timer_thread.start()

    def stop_timer(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_running = False
            self.timer_thread.join()

    def _run_timer(self):
        while self.seconds > 0 and self.timer_running:
            print(self.seconds)
            time.sleep(1)
            self.seconds -= 1
        self.timer_running = False
        if self.seconds == 0:
            self.timer_completed = True
        print("running: " + str(self.timer_running))
        print("completed: " + str(self.timer_completed))
        print("Timer finished!")
