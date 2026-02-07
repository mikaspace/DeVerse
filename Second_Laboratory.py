import threading
import multiprocessing
import time

# Grade Computing System
class GradeComputer:
    def __init__(self):
        self.scores = []
        self.lock = threading.Lock()

    def add_score(self, score):
        with self.lock:
            self.scores.append(score)

    def compute_average(self):
        with self.lock:
            if not self.scores:
                return 0
            return sum(self.scores) / len(self.scores)

# Thread worker function
def thread_worker(grade_computer, scores):
    for score in scores:
        grade_computer.add_score(score)

# Process worker function
def process_worker(grade_computer, scores):
    for score in scores:
        grade_computer.add_score(score)

# Interactive input system
def interactive_input(grade_computer):
    while True:
        score = input('Enter a score (or type "exit" to finish): ')
        if score.lower() == "exit":
            break
        try:
            grade = float(score)
            grade_computer.add_score(grade)
        except ValueError:
            print("Invalid input. Please enter a number.")

# Demo mode for showing how the system works
def demo_mode():
    print("Demo Mode: Adding scores...")
    demo_scores = [85, 90, 78, 92, 88]
    grade_computer = GradeComputer()
    for score in demo_scores:
        grade_computer.add_score(score)
    print(f"Demo average score: {grade_computer.compute_average()}")

# Performance analysis
start_time = time.time()

# Create instance of GradeComputer
grade_computer = GradeComputer()

# Simulating multithreading
scores_thread_1 = [80, 90, 100]
_scores_thread_2 = [75, 85, 95]
thread_1 = threading.Thread(target=thread_worker, args=(grade_computer, scores_thread_1))
thread_2 = threading.Thread(target=thread_worker, args=(grade_computer, scores_thread_2))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

print(f"Average score after multithreading: {grade_computer.compute_average()}")

# Simulating multiprocessing
scores_process_1 = [80, 85, 90]
scores_process_2 = [75, 70, 80]
process_1 = multiprocessing.Process(target=process_worker, args=(grade_computer, scores_process_1))
process_2 = multiprocessing.Process(target=process_worker, args=(grade_computer, scores_process_2))
process_1.start()
process_2.start()
process_1.join()
process_2.join()

print(f"Average score after multiprocessing: {grade_computer.compute_average()}")

# Execute the interactive input system
interactive_input(grade_computer)

# Performance analysis output
end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
print(f"Final average score: {grade_computer.compute_average()}")
