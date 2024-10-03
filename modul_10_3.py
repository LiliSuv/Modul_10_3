from threading import Thread, Lock
import time
import threading
from random import choice


class Bank():
    def __init__(self):
        self.balance =0
        self.lock = threading.Lock ()
    def deposit(self):
        for i in range(1,100):
            rng = range (50, 500, 1)
            a=choice(rng)
            with self.lock:
                self.balance=self.balance+a
                print(f'Пополнение: {a}. Баланс: {self.balance} ')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep (0.001)

    def take(self):
        for i in range (1, 100):
            rng = range (50, 500, 1)
            a = choice (rng)
            print(f'Запрос на {a} ')
            with self.lock:
                if a<=self.balance:
                    self.balance = self.balance - a
                    print(f'Снятие: {a}. Баланс: {self.balance}. ')
                else:
                    print(f'Запрос отклонён, недостаточно средств. ')

            time.sleep (0.001)

bk = Bank()

th1 = threading.Thread (target=Bank.deposit, args=(bk,))
th2 = threading.Thread (target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')