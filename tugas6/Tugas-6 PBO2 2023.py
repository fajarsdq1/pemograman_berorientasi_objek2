import threading
import time

def a():
    print(f"Fungtion a runs at time:\ {str(int(time.time()))} seconds")
def b():
    print(f"Fungtion b runs at time:\ {str(int(time.time()))} seconds")

threading.Thread(target =a).start
threading.Thread(target =b).start