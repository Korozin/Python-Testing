import time
import signal

# Define signal handler for Ctrl+C
def signal_handler(sig, frame):
    print("\nExited")
    exit(0)

# Set signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

while True:
    print("\r" + "Loading. ", end="", flush=True)
    time.sleep(1)
    print("\r" + "Loading.. ", end="", flush=True)
    time.sleep(1)
    print("\r" + "Loading... ", end="", flush=True)
    time.sleep(1)
    print("\r" + "Loading.. ", end="", flush=True)
    time.sleep(1)
    print("\r" + "Loading. ", end="", flush=True)
    time.sleep(1)
    print("\r" + "Loading ", end="", flush=True)
    time.sleep(1)
