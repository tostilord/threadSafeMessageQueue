import time
import threading


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(5)
    print("myfunc ended")


if __name__ == '__main__':
    print("main started")
    t = threading.Thread(target=myfunc, args=['Terrance'])
    t.start()
    t.join()
    print("main ended")
