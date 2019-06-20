import signal
def onsignal():
    print('hello')
signal.signal(signal.SIGKILL, onsignal)

while True:
    signal.pause()