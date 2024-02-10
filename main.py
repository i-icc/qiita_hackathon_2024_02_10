import threading
from google.cloud import firestore
from google.oauth2 import service_account
from time import sleep
from sound_player import SoundPlayer

sp_open = SoundPlayer('./open.mp3')
sp_close = SoundPlayer('./close.mp3')


callback_done = threading.Event()

def on_snapshot(col_snapshot, changes, read_time):
        change = changes[0]
        is_open= change.document.get("is_open")
        print(f"is_open: {is_open}")
        if(is_open):
            sp_open.play()
        else:
            sp_close.play()

key_path = ".keys/firestore.json"
credentials = service_account.Credentials.from_service_account_file(key_path)
db = firestore.Client(
    credentials=credentials,
    project="ikiterutel"
    )

col_query = db.collection("ikiterutel")

query_watch = col_query.on_snapshot(on_snapshot)


# 監視
while True:
    sleep(1)
    print('processing...')