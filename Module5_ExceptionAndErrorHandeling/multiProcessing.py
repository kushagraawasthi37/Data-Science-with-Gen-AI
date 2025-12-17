"""
===========================================================
PYTHON MULTIPROCESSING – COMPLETE INTERVIEW READY FILE
===========================================================

KEY POINTS (Interview):
----------------------
✔ Multiprocessing = TRUE PARALLELISM
✔ Each process has its own Python interpreter
✔ GIL does NOT block multiprocessing
✔ Best for CPU-bound tasks
✔ On Windows, __main__ guard is MANDATORY
"""

import time
import multiprocessing
import concurrent.futures


# ===========================================================
# 1️⃣ SEQUENTIAL EXECUTION (BASELINE – NO PARALLELISM)
# ===========================================================

def sequential_task():
    """
    Simple function jo 1 second sleep karta hai
    Sequential call → time add hota jayega
    """
    print("Sequential: doing something")
    time.sleep(1)
    print("Sequential: done sleeping")


# ===========================================================
# 2️⃣ BASIC MULTIPROCESSING TASK
# ===========================================================

def process_task():
    """
    Ye function alag process me run karega
    """
    print("Process: doing something")
    time.sleep(1)
    print("Process: done sleeping")


# ===========================================================
# 3️⃣ SHARED MEMORY USING multiprocessing.Array
# ===========================================================

def square_shared(index, shared_arr):
    """
    Shared memory ke ek element ka square
    """
    shared_arr[index] = shared_arr[index] ** 2


# ===========================================================
# 4️⃣ POOL WORKER FUNCTION
# ===========================================================

def square_pool(no):
    """
    Pool ke worker process me chalega
    """
    result = no * no
    print(f"Pool: square of {no} is {result}")


# ===========================================================
# 5️⃣ IPC USING QUEUE (PRODUCER – CONSUMER)
# ===========================================================

def enroll_students(student_queue):
    """
    Producer process
    """
    for student in ["Ajay", "Bijay", "Sanjay", "Rizwan"]:
        student_queue.put(f"Enroll {student}")

    # Signal consumer to stop
    student_queue.put(None)


def register_students(student_queue):
    """
    Consumer process
    """
    while True:
        msg = student_queue.get()
        if msg is None:
            break
        print(f"Registrar received: {msg}")


# ===========================================================
# 6️⃣ EXECUTOR TASK
# ===========================================================

def executor_task(i):
    """
    ProcessPoolExecutor ka worker
    """
    print(f"Executor task {i} started")
    time.sleep(1)
    print(f"Executor task {i} finished")


# ===========================================================
# 🔴 MAIN ENTRY POINT (MANDATORY FOR WINDOWS)
# ===========================================================

if __name__ == "__main__":
    multiprocessing.freeze_support()

    # -------------------------------------------------------
    # SEQUENTIAL EXECUTION
    # -------------------------------------------------------
    print("\n--- SEQUENTIAL EXECUTION ---")
    start = time.perf_counter()

    sequential_task()
    sequential_task()

    end = time.perf_counter()
    print(f"Sequential finished in {round(end - start, 2)} seconds\n")


    # -------------------------------------------------------
    # BASIC MULTIPROCESSING
    # -------------------------------------------------------
    print("--- MULTIPROCESSING WITH Process ---")
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=process_task)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f"Processes finished in {round(end - start, 2)} seconds\n")


    # -------------------------------------------------------
    # SHARED MEMORY
    # -------------------------------------------------------
    print("--- SHARED MEMORY USING Array ---")
    start = time.perf_counter()

    shared_arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])
    processes = []

    for i in range(len(shared_arr)):
        p = multiprocessing.Process(
            target=square_shared,
            args=(i, shared_arr)
        )
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Shared array result:", list(shared_arr))

    end = time.perf_counter()
    print(f"Shared memory finished in {round(end - start, 2)} seconds\n")


    # -------------------------------------------------------
    # PROCESS POOL
    # -------------------------------------------------------
    print("--- multiprocessing.Pool ---")
    start = time.perf_counter()

    numbers = [2, 3, 4, 5, 6000]
    with multiprocessing.Pool() as pool:
        pool.map(square_pool, numbers)

    end = time.perf_counter()
    print(f"Pool finished in {round(end - start, 2)} seconds\n")


    # -------------------------------------------------------
    # INTER PROCESS COMMUNICATION (QUEUE)
    # -------------------------------------------------------
    print("--- IPC USING Queue ---")

    student_queue = multiprocessing.Queue()

    enroll_proc = multiprocessing.Process(
        target=enroll_students,
        args=(student_queue,)
    )
    register_proc = multiprocessing.Process(
        target=register_students,
        args=(student_queue,)
    )

    enroll_proc.start()
    register_proc.start()

    enroll_proc.join()
    register_proc.join()

    print("IPC finished\n")


    # -------------------------------------------------------
    # ProcessPoolExecutor (MODERN WAY)
    # -------------------------------------------------------
    print("--- ProcessPoolExecutor ---")
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(executor_task, range(10))

    end = time.perf_counter()
    print(f"Executor finished in {round(end - start, 2)} seconds\n")


    print("✅ ALL MULTIPROCESSING DEMOS COMPLETED SUCCESSFULLY")
