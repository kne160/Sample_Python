import threading, queue
import time

def washer(dishes, dish_queue):
    for dish in dishes:
        print('Washing', dish)
        time.sleep(3)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('Drying', dish)
        time.sleep(10)
        dish_queue.task_done()


dish_queue = queue.Queue()
for n in range(1):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()

dishes = ['SALAD', 'BREAD', 'ENTREE', 'DESERT']
washer(dishes, dish_queue)
dish_queue.join()
