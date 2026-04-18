import random
import time


def gen_data(n):
    return [random.randint(1, 1000000) for _ in range(n)]


def gen_sorted_data(n):
    return list(range(n))


def gen_reverse_sorted_data(n):
    return list(range(n, 0, -1))


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def is_sorted(data):
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))