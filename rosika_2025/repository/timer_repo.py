import sqlite3

conn = sqlite3.connect('button_events.db')

def store_btn_clicked_event(event):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (button_id, timestamp) VALUES (?, ?)",
                   (event.button_id, event.timestamp))
    conn.commit()
