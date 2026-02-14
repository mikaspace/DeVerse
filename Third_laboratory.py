from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading


# PART A – Task Parallelism

def compute_sss(salary):
    print(f"SSS computed by {threading.current_thread().name}")
    return salary * 0.045

def compute_philhealth(salary):
    print(f"PhilHealth computed by {threading.current_thread().name}")
    return salary * 0.025

def compute_pagibig(salary):
    print(f"Pag-IBIG computed by {threading.current_thread().name}")
    return salary * 0.02

def compute_tax(salary):
    print(f"Tax computed by {threading.current_thread().name}")
    return salary * 0.10


def task_parallelism_example():
    name = "Alice"
    salary = 25000

    print(f"\n--- Task Parallelism for {name} ---")
    print(f"Salary: {salary}")

    with ThreadPoolExecutor() as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_philhealth = executor.submit(compute_philhealth, salary)
        future_pagibig = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        sss = future_sss.result()
        philhealth = future_philhealth.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total_deduction = sss + philhealth + pagibig + tax

    print(f"SSS: {sss:.2f}")
    print(f"PhilHealth: {philhealth:.2f}")
    print(f"Pag-IBIG: {pagibig:.2f}")
    print(f"Withholding Tax: {tax:.2f}")
    print(f"Total Deduction: {total_deduction:.2f}")


# PART B – Data Parallelism

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def compute_payroll(employee):
    name, salary = employee

    sss = salary * 0.045
    philhealth = salary * 0.025
    pagibig = salary * 0.02
    tax = salary * 0.10

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return name, salary, total_deduction, net_salary


def data_parallelism_example():
    print("\n--- Data Parallelism for All Employees ---")

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

        for name, salary, total_deduction, net_salary in results:
            print(f"\nEmployee: {name}")
            print(f"Gross Salary: {salary:.2f}")
            print(f"Total Deduction: {total_deduction:.2f}")
            print(f"Net Salary: {net_salary:.2f}")


# -------------------------------
# MAIN (Required for Windows)
# -------------------------------

if __name__ == "__main__":
    task_parallelism_example()
    data_parallelism_example()
