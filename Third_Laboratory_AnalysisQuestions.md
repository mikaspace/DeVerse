# Concurrency and Parallelism Analysis – Payroll System

## 1. Difference Between Task Parallelism and Data Parallelism

Task Parallelism refers to running different tasks at the same time using the same data. In Part A of the implementation, each payroll deduction such as SSS, PhilHealth, Pag-IBIG, and Withholding Tax was written as a separate function. These functions all used the same salary value but were executed concurrently using `ThreadPoolExecutor`. The workload was divided by function, meaning different tasks were processed simultaneously while operating on the same input.

Data Parallelism, on the other hand, applies the same function to different pieces of data at the same time. In Part B, a single payroll computation function was applied to multiple employees using `ProcessPoolExecutor`. Instead of dividing the workload by function, it was divided by employee. Each process handled a different employee’s payroll computation, allowing multiple employee records to be processed simultaneously.

## 2. How `concurrent.futures` Managed Execution

The `concurrent.futures` module provides high-level tools for asynchronous and concurrent execution. The `submit()` method schedules a single function for execution and returns a `Future` object. The `map()` method applies a function to an iterable of data and returns the results in order. A `Future` object represents a result that may not yet be completed, and calling `.result()` retrieves the computed value once the task has finished executing.

The `with` statement is important when working with executors. When an Executor is created inside a `with` block, worker threads or processes are automatically started. The executor also waits for all tasks to complete before exiting the block and properly shuts down all workers. This ensures clean resource management and prevents memory leaks or orphaned processes.

For example:

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    future = executor.submit(function_name, argument)
    result = future.result()
```

## 3. ThreadPoolExecutor, GIL, and CPU Cores

`ThreadPoolExecutor` uses multiple threads within a single Python process. However, CPython includes a Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time. Because payroll computation is a CPU-bound task, true parallel execution across multiple CPU cores does not fully occur when using threads. Although threads may appear to run at the same time, only one thread executes Python instructions at any given moment. As a result, this approach provides concurrency but not true parallelism for CPU-heavy operations.

## 4. Why ProcessPoolExecutor Enables True Parallelism

`ProcessPoolExecutor` creates separate processes instead of threads. Each process has its own memory space, its own Python interpreter, and its own GIL. Since the processes are independent of one another, multiple CPU cores can be utilized simultaneously. This bypasses the limitation imposed by the GIL and enables true parallel execution, which is especially beneficial for CPU-bound tasks such as payroll computations.

Although using multiple processes introduces slight overhead due to inter-process communication and memory separation, the performance gains for heavy computations generally outweigh the added cost.

For example:

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as executor:
    results = executor.map(payroll_function, employee_list)
```

## 5. Scalability from 5 to 10,000 Employees

If the payroll system scales from a small number of employees to around 10,000 employees, the difference between thread-based and process-based execution becomes more significant. Task Parallelism using `ThreadPoolExecutor` would not scale efficiently for CPU-bound payroll calculations because all computations remain within a single process and are restricted by the GIL. This limits the ability to fully utilize multiple CPU cores.

In contrast, Data Parallelism using `ProcessPoolExecutor` scales more effectively because multiple processes distribute the workload across available CPU cores. For large datasets, process-based execution improves workload distribution, increases CPU utilization, and enhances overall performance efficiency.

## 6. Real-World Payroll System Example

In a real-world payroll system, Task Parallelism could be used when calculating different payroll components for a single employee. For example, tax computation, benefits deduction, loan deduction, and bonus calculation could run concurrently. If these tasks involve database queries or other I/O operations, `ThreadPoolExecutor` would be appropriate because threads perform well for I/O-bound work.

For processing payroll for thousands of employees, Data Parallelism would be more suitable. The same payroll computation function would be applied to each employee record simultaneously using `ProcessPoolExecutor`. Since payroll calculations are typically CPU-intensive, using multiple processes allows the system to utilize multiple CPU cores and handle large-scale payroll processing more efficiently.
