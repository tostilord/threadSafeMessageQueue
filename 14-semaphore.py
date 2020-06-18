import threading

sem = threading.Semaphore(value=50)
sem.acquire()
sem.acquire()
sem.acquire()
sem.release()
print(sem._value)
