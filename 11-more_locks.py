# import threading
#
# rlock = threading.RLock()
# rlock.acquire()
# rlock.acquire()
# rlock.release()
# print(rlock)
# print(threading.currentThread())


import threading

rlock = threading.RLock()


def get_lock():
    print(threading.currentThread())
    rlock.acquire()
    print('ding')


if __name__ == '__main__':
    print(f'd0: {rlock}, thread: {threading.currentThread()}')
    t1 = threading.Thread(target=get_lock)
    t1.start()
    print(f'd1: {rlock}')
    t2 = threading.Thread(target=get_lock)
    t2.start()
    print(f'd2: {rlock}')
