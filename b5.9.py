import time

class Stopwatch:
    """класс "секундомер"

    как секундомер пока не работает, но умеет замерять 
    скорость работы функций через контекстный менеджер
    и как декоратор
    """
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __enter__(self):
        self.total_time = 0
        self.avg_time = 0
        return self

    def __exit__(self, type, value, traceback):
        self.avg_time = self.total_time / self.num_runs
        print(f"закончили замер времени, общее - {self.total_time:.5f} сек, среднее - {self.avg_time:.5f} сек")

    def __call__(self, func):
        def decorator():
            total_time = 0
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                total_time += (t1 - t0)
            avg_time = total_time / self.num_runs
            print(f"закончили замер времени, общее - {total_time:.5f} сек, среднее - {avg_time:.5f} сек")
        return decorator

    def timed(self, func):
        """метод класса, который используется для замера времени через контекстный менеджер"""
        for _ in range(self.num_runs):
            t0 = time.time()
            func()
            t1 = time.time()
            self.total_time += (t1 - t0)

print("=====проверяем работу декоратора как объект класса секундомер (Stopwatch)=====\n")

my_stopwatch = Stopwatch(num_runs=10)
# число запусков передаем здесь

@my_stopwatch
def inner_func():
    print("это функция, скорость работы которой мы замеряем")
    for _ in range(50000000):
        pass

def inner_func2():
    print("еще одна функция, скорость работы которой мы замеряем")
    for _ in range(50000000):
        pass

inner_func()
# вызов замеряемой функции

print("\n=====проверяем работу по замеру времени через контекстный менеджер=====\n")

with my_stopwatch as t:
    t.timed(inner_func2)
