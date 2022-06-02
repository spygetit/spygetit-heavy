from threading import Thread

import frontend
import backend

if __name__ == "__main__":
    bck = Thread(target=backend.start, daemon=True)
    bck.start()
    frontend.start()
    bck.join()
