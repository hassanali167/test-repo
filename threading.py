"""
Topic: Threading in Python

Explanation:
Threading enables parallel execution of tasks to improve performance.
The `threading` module allows running multiple threads simultaneously.
"""

import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # Simulating a delay
        print(f"Number: {i}")

# Creating two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Starting the threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()

print("Threads completed")

"""
Code Explanation:
- `threading.Thread(target=function)` creates a new thread.
- `start()` begins execution in parallel.
- `join()` ensures the main thread waits for completion.
"""
