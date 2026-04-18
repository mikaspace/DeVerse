import random
import time


def generate_values(n):
    return [random.randint(1, 1000000) for _ in range(n)]


def generate_reverse_values(n):
    return list(range(n, 0, -1))


def time_execution(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def check_sorted(values):
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))