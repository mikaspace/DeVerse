from sorting import merge_sort
from parallel_sorting import parallel_merge_sort
from searching import linear_search, parallel_linear_search
from utils import (
    gen_data,
    gen_reverse_sorted_data,
    measure_time,
    is_sorted
)


def test_dataset(data, label):
    print(f"\n--- {label} ---")
    target = data[-1] if data else -1

    seq_sorted, seq_sort_time = measure_time(merge_sort, data.copy())
    par_sorted, par_sort_time = measure_time(parallel_merge_sort, data.copy())
    seq_index, seq_search_time = measure_time(linear_search, data, target)
    par_index, par_search_time = measure_time(parallel_linear_search, data, target)

    print(f"Sequential Merge Sort: {seq_sort_time:.6f} sec | Sorted: {is_sorted(seq_sorted)}")
    print(f"Parallel Merge Sort:   {par_sort_time:.6f} sec | Sorted: {is_sorted(par_sorted)}")
    print(f"Sequential Search:     {seq_search_time:.6f} sec | Index: {seq_index}")
    print(f"Parallel Search:       {par_search_time:.6f} sec | Index: {par_index}")


def main():
    sizes = [1000, 100000, 1000000]

    for size in sizes:
        data = gen_data(size)
        test_dataset(data, f"Random dataset ({size})")

    reverse_data = gen_reverse_sorted_data(100000)
    test_dataset(reverse_data, "Special case: reverse sorted (100000)")


if __name__ == "__main__":
    main()