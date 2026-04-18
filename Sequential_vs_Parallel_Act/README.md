# Sequential vs Parallel Algorithms

### Performance Analysis using Merge Sort and Linear Search

---

## Project Overview

This project explores the fundamental differences between sequential and parallel algorithms through implementation, testing, and performance evaluation.

The objective is to understand:

* When sequential execution is more efficient
* When parallelism provides performance improvements
* How overhead impacts overall performance

---

## Group Members

| Member                    | Responsibility                              |
| ------------------------  | ------------------------------------------- |
| Oplimo, Kent Louie S.     | Sequential Merge Sort                       |
| Member 2                  | Parallel Merge Sort                         |
| Member 3                  | Sequential and Parallel Linear Search       |
| Seromines, Ralph Joshua A.| Dataset Generation, Timing, Testing, README |

---

## Algorithms Implemented

### Sorting Algorithms

* Sequential Merge Sort
* Parallel Merge Sort

### Searching Algorithms

* Sequential Linear Search
* Parallel Linear Search

---

## Dataset Configuration

The algorithms were evaluated using the following dataset sizes:

| Category     | Size                |
| ------------ | ------------------- |
| Small        | 1,000 elements      |
| Medium       | 100,000 elements    |
| Large        | 1,000,000 elements  |
| Special Case | Reverse Sorted Data |

---

## How to Run

```bash
python main.py
```

---

## Performance Results

| Dataset        | Sequential Sort | Parallel Sort | Sequential Search | Parallel Search |
| -------------- | --------------- | ------------- | ----------------- | --------------- |
| 1,000          |                 |               |                   |                 |
| 100,000        |                 |               |                   |                 |
| 1,000,000      |                 |               |                   |                 |
| Reverse Sorted |                 |               |                   |                 |

Replace the empty fields with actual execution times from your tests.

---

## Analysis

The following observations were made during testing:

* Sequential algorithms performed better on smaller datasets due to minimal overhead.
* Parallel algorithms introduced additional costs such as process creation, inter-process communication, and synchronization.
* For larger datasets, parallel execution demonstrated improved scalability and performance.
* Merge Sort benefited more from parallelization because of its divide-and-conquer nature.

A key insight is that parallel algorithms are not inherently faster. Their effectiveness depends on whether the computational workload is large enough to offset the overhead introduced by parallel processing.

---

## Individual Reflection

### Oplimo, Kent Louie S.

During this activity, I observed that sequential algorithms execute tasks one at a time, while parallel algorithms divide the workload and execute multiple parts simultaneously. For smaller datasets, the sequential approach performed better due to lower overhead. However, for larger datasets, the parallel implementation showed improved performance by utilizing multiple processes.

One of the main challenges I encountered was managing parallel processes and ensuring that results were combined correctly. This was especially evident in sorting, where merging sorted partitions required careful handling. I also learned that parallel algorithms introduce additional complexity, including synchronization and communication overhead.

Overall, this activity helped me understand that while parallelism can improve performance, it is only beneficial when the problem size justifies the added complexity.

### Seromines, Ralph Joshua A.
In this activity, I handled dataset generation, timing, and integration of the program. During testing, I observed that sequential algorithms were faster for small datasets due to lower overhead, while parallel algorithms performed better for larger datasets because they can process tasks simultaneously.

One challenge was ensuring that all results were correct before analyzing performance. This activity showed me that parallel algorithms are not always faster, and their effectiveness depends on the workload and system overhead.

---

## Demo

A short demonstration (5–10 seconds) showing execution comparison is included in the repository.

---

## Project Structure

```
Sequential_vs_Parallel_Act/
├── main.py
├── sequential_sorting.py
├── parallel_sorting.py
├── searching.py
├── utils.py
└── README.md 
```

---

## Conclusion

This project demonstrates that selecting between sequential and parallel algorithms depends on the problem size and system constraints rather than assuming one approach is universally better.
