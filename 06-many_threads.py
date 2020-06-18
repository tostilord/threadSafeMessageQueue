import time
import threading


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(5)
    print("myfunc ended")


def myfunc2(name):
    print(f"myfunc2 started with {name}")
    time.sleep(5)
    print("myfunc2 ended")


def myfunc3(name):
    print(f"myfunc3 started with {name}")
    time.sleep(5)
    print("myfunc2 ended")


if __name__ == '__main__':
    print("main started")
    t1 = threading.Thread(target=myfunc, args=['Terrance'])
    t1.start()
    t2 = threading.Thread(target=myfunc2, args=['Barry'])
    t2.start()
    t3 = threading.Thread(target=myfunc3, args=['Mathilda'])
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("main ended")
