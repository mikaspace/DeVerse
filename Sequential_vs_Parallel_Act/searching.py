from multiprocessing import Process, Queue


def sequential_search(values, target):
    for idx, val in enumerate(values):
        if val == target:
            return idx
    return -1


def search_segment_worker(segment, target, queue, offset):
    for idx, val in enumerate(segment):
        if val == target:
            queue.put(offset + idx)
            return
    queue.put(-1)


def parallel_search(values, target, workers=4):
    queue = Queue()
    processes = []
    chunk_size = max(1, len(values) // workers)

    for i in range(workers):
        start = i * chunk_size
        end = len(values) if i == workers - 1 else min(len(values), (i + 1) * chunk_size)

        if start >= len(values):
            break

        segment = values[start:end]
        p = Process(target=search_segment_worker, args=(segment, target, queue, start))
        processes.append(p)
        p.start()

    results = [queue.get() for _ in processes]

    for p in processes:
        p.join()

    valid = [r for r in results if r != -1]
    return min(valid) if valid else -1