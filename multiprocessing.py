"""
Topic: Multiprocessing in Python

Explanation:
The `multiprocessing` module allows execution of multiple processes in parallel,
which is useful for CPU-intensive tasks.
"""

import multiprocessing
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Process Number: {i}")

# Creating multiple processes
process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_numbers)

# Starting the processes
process1.start()
process2.start()

# Waiting for processes to complete
process1.join()
process2.join()

print("Processes completed")

"""
Code Explanation:
- `multiprocessing.Process(target=function)` creates a new process.
- `start()` begins execution in a separate process.
- `join()` ensures the main process waits for completion.
"""
