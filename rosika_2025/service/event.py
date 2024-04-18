class Event:
    def __init__(self, btn_id, timestamp, sent, event_type):
        self.event_type = event_type
        self.button_id = btn_id
        self.timestamp = timestamp
        self.sent = sent