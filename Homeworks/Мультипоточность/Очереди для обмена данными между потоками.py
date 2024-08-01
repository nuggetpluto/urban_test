# import threading
# import time
# import queue
#
# class Table:
#     def __init__(self, number):
#         self.number = number
#         self.is_busy = False
#
# class Customer(threading.Thread):
#     def __init__(self, number, cafe):
#         super().__init__()
#         self.number = number
#         self.cafe = cafe
#
#     def run(self):
#         print(f"Посетитель номер {self.number} прибыл.")
#         self.cafe.serve_customer(self)
#         time.sleep(5)
#         self.cafe.customer_done(self)
#
# class Cafe:
#     def __init__(self, tables):
#         self.tables = tables
#         self.queue = queue.Queue()
#         self.customer_count = 0
#         self.lock = threading.Lock()
#
#     def customer_arrival(self):
#         while self.customer_count < 20:
#             self.customer_count += 1
#             customer = Customer(self.customer_count, self)
#             customer.start()
#             time.sleep(1)
#
#     def serve_customer(self, customer):
#         with self.lock:
#             free_table = None
#             for table in self.tables:
#                 if not table.is_busy:
#                     free_table = table
#                     break
#             if free_table:
#                 free_table.is_busy = True
#                 print(f"Посетитель номер {customer.number} сел за стол {free_table.number}.")
#                 customer.table = free_table
#             else:
#                 print(f"Посетитель номер {customer.number} ожидает свободный стол.")
#                 self.queue.put(customer)
#
#     def customer_done(self, customer):
#         with self.lock:
#             customer.table.is_busy = False
#             print(f"Посетитель номер {customer.number} покушал и ушёл.")
#             if not self.queue.empty():
#                 next_customer = self.queue.get()
#                 self.serve_customer(next_customer)
#
#
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
#
# tables = [table1, table2, table3]
#
# cafe = Cafe(tables)
#
# customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
#
# customer_arrival_thread.join()
#



from threading import Thread
import queue
from time import sleep


class Table:
    def __init__(self):
        self.number = 1
        self.is_busy = False

    def set_busy(self):
        self.is_busy = True

    def set_free(self):
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue
        self.tables = tables
        self.number = 1

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            print(f'Посетитель номер {customer_number} прибыл')
            customer = Customer(customer_number, self)
            customer.start()
            customer_number += 1
            sleep(1)

    def serve_customer(self, customer_number):
        for table in self.tables:
            if not table.is_busy:
                table.set_busy()
                print(f'Посетитель номер {customer_number} сел за стол {self.number}')
                self.number += 1
                sleep(5)
                print(f'Посетитель номер {customer_number} покушал и ушёл')
                table.set_free()
                self.check_queue()
                return
        else:
            self.queue.put(customer_number)
            print(f'Посетитель номер {customer_number} ожидает свободный стол')

    def check_queue(self):
        if not self.queue.empty():
            customer_number = self.queue.get()
            self.serve_customer(customer_number)


class Customer(Thread):
    def __init__(self, num, cafe):
        super().__init__()
        self.num = num
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self.num)


queue = queue.Queue()

table1 = Table()
table2 = Table()
table3 = Table()
tables = [table1, table2, table3]

cafe = Cafe(tables)


customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
