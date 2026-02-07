import threading
import multiprocessing
import time

# ------------------------------------
# THREAD FUNCTION
# ------------------------------------
def compute_gwa_thread(grade, results, index):
    print(f"[Thread-{index}] Processing grade: {grade}")
        time.sleep(0.1)  # simulate processing time
            results[index] = grade

            # ------------------------------------
            # PROCESS FUNCTION
            # ------------------------------------
            def compute_gwa_process(grade, queue, index):
                print(f"[Process-{index}] Processing grade: {grade}")
                    time.sleep(0.1)  # simulate processing time
                        queue.put(grade)

                        # ------------------------------------
                        # MAIN PROGRAM
                        # ------------------------------------
                        if __name__ == "__main__":

                            # -----------------------------
                                # USER INPUT
                                    # -----------------------------
                                        n = int(input("Enter number of subjects: "))
                                            grades = []

                                                for i in range(n):
                                                        grade = float(input(f"Enter grade for subject {i + 1}: "))
                                                                grades.append(grade)

                                                                    print("\n==============================")
                                                                        print(" MULTITHREADING VERSION ")
                                                                            print("==============================")

                                                                                thread_results = [0] * n
                                                                                    threads = []

                                                                                        start_time = time.time()

                                                                                            for i, grade in enumerate(grades):
                                                                                                    t = threading.Thread(
                                                                                                                target=compute_gwa_thread,
                                                                                                                            args=(grade, thread_results, i)
                                                                                                                                    )
                                                                                                                                            threads.append(t)
                                                                                                                                                    t.start()

                                                                                                                                                        for t in threads:
                                                                                                                                                                t.join()

                                                                                                                                                                    gwa_thread = sum(thread_results) / len(thread_results)
                                                                                                                                                                        thread_time = time.time() - start_time

                                                                                                                                                                            print(f"\n[Multithreading] GWA: {gwa_thread:.2f}")
                                                                                                                                                                                print(f"[Multithreading] Execution Time: {thread_time:.6f} seconds")

                                                                                                                                                                                    print("\n==============================")
                                                                                                                                                                                        print(" MULTIPROCESSING VERSION ")
                                                                                                                                                                                            print("==============================")

                                                                                                                                                                                                processes = []
                                                                                                                                                                                                    queue = multiprocessing.Queue()

                                                                                                                                                                                                        start_time = time.time()

                                                                                                                                                                                                            for i, grade in enumerate(grades):
                                                                                                                                                                                                                    p = multiprocessing.Process(
                                                                                                                                                                                                                                target=compute_gwa_process,
                                                                                                                                                                                                                                            args=(grade, queue, i)
                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                            processes.append(p)
                                                                                                                                                                                                                                                                    p.start()

                                                                                                                                                                                                                                                                        process_results = []
                                                                                                                                                                                                                                                                            for _ in processes:
                                                                                                                                                                                                                                                                                    process_results.append(queue.get())

                                                                                                                                                                                                                                                                                        for p in processes:
                                                                                                                                                                                                                                                                                                p.join()

                                                                                                                                                                                                                                                                                                    gwa_process = sum(process_results) / len(process_results)
                                                                                                                                                                                                                                                                                                        process_time = time.time() - start_time

                                                                                                                                                                                                                                                                                                            print(f"\n[Multiprocessing] GWA: {gwa_process:.2f}")
                                                                                                                                                                                                                                                                                                                print(f"[Multiprocessing] Execution Time: {process_time:.6f} seconds")

                                                                                                                                                                                                                                                                                                                    print("\n==============================")
                                                                                                                                                                                                                                                                                                                        print(" SUMMARY ")
                                                                                                                                                                                                                                                                                                                            print("==============================")
                                                                                                                                                                                                                                                                                                                                print(f"Multithreading  -> GWA: {gwa_thread:.2f}, Time: {thread_time:.6f}s")
                                                                                                                                                                                                                                                                                                                                    print(f"Multiprocessing -> GWA: {gwa_process:.2f}, Time: {process_time:.6f}s")
