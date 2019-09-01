import time


# Вариант с обычным декоратором
def time_this(num_runs=10):
    def wrap_(func):
        def wrapper():
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            return "Average execution time is %.5f seconds" % avg_time

        return wrapper

    return wrap_


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


print(f())


# Вариант с декоратором-объектом
class Timer:
    def __call__(self, num_runs=10):
        def wrap_(func):
            def wrapper():
                avg_time = 0
                for _ in range(num_runs):
                    t0 = time.time()
                    func()
                    t1 = time.time()
                    avg_time += (t1 - t0)
                avg_time /= num_runs
                return "Average execution time is %.5f seconds" % avg_time

            return wrapper

        return wrap_

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# Использование как объект
time_this = Timer()


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


print(f())

# Использование как контекстный менеджер
with Timer() as time_this:
    @time_this(num_runs=10)
    def f():
        for j in range(1000000):
            pass


    print(f())
