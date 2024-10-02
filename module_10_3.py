import random
import time
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 500
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            calc = random.randint(50, 500)
            self.balance += calc
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {calc}. Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        for y in range(100):
            calc2 = random.randint(50, 500)
            print(f'Запрос на {calc2}')
            if calc2 <= self.balance:
                self.balance -= calc2
                print(f'Снятие: {calc2}. Баланс: {self.balance}')
            else:

                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)


bk = Bank()


th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')



