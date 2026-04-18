from multiprocessing import Pool
from sequential import divide_and_merge_sort, merge_lists


def process_chunk(chunk):
    return divide_and_merge_sort(chunk)


def parallel_merge_sort(values, workers=4):
    if len(values) <= 1:
        return values

    chunk_size = max(1, len(values) // workers)
    segments = [values[i:i + chunk_size] for i in range(0, len(values), chunk_size)]

    with Pool(processes=workers) as pool:
        sorted_segments = pool.map(process_chunk, segments)

    while len(sorted_segments) > 1:
        merged_segments = []
        for i in range(0, len(sorted_segments), 2):
            if i + 1 < len(sorted_segments):
                merged_segments.append(merge_lists(sorted_segments[i], sorted_segments[i + 1]))
            else:
                merged_segments.append(sorted_segments[i])
        sorted_segments = merged_segments

    return sorted_segments[0]