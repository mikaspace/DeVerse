from sequential import divide_and_merge_sort
from parallel_sorting import parallel_merge_sort
from searching import sequential_search, parallel_search
from utils import (
    generate_values,
    generate_reverse_values,
    time_execution,
    check_sorted
)


def run_test(values, label):
    print(f"\n--- {label} ---")
    target = values[-1] if values else -1

    seq_sorted, seq_sort_time = time_execution(divide_and_merge_sort, values.copy())
    par_sorted, par_sort_time = time_execution(parallel_merge_sort, values.copy())
    seq_idx, seq_search_time = time_execution(sequential_search, values, target)
    par_idx, par_search_time = time_execution(parallel_search, values, target)

    print(f"Sequential Sort: {seq_sort_time:.6f}s | Sorted: {check_sorted(seq_sorted)}")
    print(f"Parallel Sort:   {par_sort_time:.6f}s | Sorted: {check_sorted(par_sorted)}")
    print(f"Sequential Search: {seq_search_time:.6f}s | Index: {seq_idx}")
    print(f"Parallel Search:   {par_search_time:.6f}s | Index: {par_idx}")


def main():
    sizes = [1000, 100000, 1000000]

    for size in sizes:
        values = generate_values(size)
        run_test(values, f"Random ({size})")

    reverse_values = generate_reverse_values(100000)
    run_test(reverse_values, "Reverse Sorted (100000)")


if __name__ == "__main__":
    main()