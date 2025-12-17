"""
=====================================================
PYTHON MULTITHREADING – COMPLETE INTERVIEW NOTES
=====================================================

IMPORTANT TERMINOLOGY:
----------------------
Program     → Complete application
Process     → Program in execution (has its own memory)
Thread      → Smallest unit of execution inside a process

MULTIPROCESSING:
----------------
✔ True parallelism
✔ Multiple CPU cores use hote hain
✔ Heavy CPU tasks ke liye best

MULTITHREADING:
---------------
✔ Same process ke andar multiple threads
✔ Memory share hoti hai
✔ Best for I/O bound tasks

NOTE:
❌ Python me true parallel multithreading nahi hoti (CPython)
✔ Reason: GIL (Global Interpreter Lock)
"""

import time
import threading


# =====================================================
# NORMAL FUNCTION (SEQUENTIAL EXECUTION)
# =====================================================

def test_func():
    """
    Ye function sequentially execute hota hai
    Har call me 1 second ka sleep
    """
    print("Do something")
    print("Sleeping for 1 second")
    time.sleep(1)
    print("Done with sleep")


# =====================================================
# MULTITHREADING FUNCTION
# =====================================================

def test_func_thread(args):
    """
    Ye function thread ke through run hoga
    Har thread independently sleep karega
    """
    print(f"[Thread {args}] Doing something")
    print(f"[Thread {args}] Sleeping for 1 second")
    time.sleep(1)
    print(f"[Thread {args}] Done sleeping\n")


# =====================================================
# THREAD CREATION + START + JOIN
# =====================================================

"""
Thread Lifecycle:
-----------------
1️⃣ Thread object create
2️⃣ start() → execution begin
3️⃣ join() → main thread wait karega
"""

# start = time.perf_counter()

# t1 = threading.Thread(target=test_func_thread, args=(1,))
# t2 = threading.Thread(target=test_func_thread, args=(2,))
# t3 = threading.Thread(target=test_func_thread, args=(3,))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# end = time.perf_counter()
# print(f"Program executed in {end - start} seconds")


# =====================================================
# MULTIPLE THREADS USING LOOP
# =====================================================

threads = []

# for i in range(5):
#     t = threading.Thread(target=test_func_thread, args=(i,))
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


# =====================================================
# WHY MULTITHREADING IS NOT PARALLEL IN PYTHON
# =====================================================

"""
GIL (Global Interpreter Lock):
-----------------------------
✔ CPython ek hi thread ko execute karne deta hai at a time
✔ CPU-bound task me performance improve nahi hoti
✔ Context switching hoti rehti hai

BUT:
----
✔ Jab thread I/O me busy hota hai (sleep, file, network)
✔ GIL release ho jata hai
✔ Dusra thread execute kar leta hai
"""


# =====================================================
# MULTITHREADING FOR I/O BOUND TASKS (BEST USE CASE)
# =====================================================

"""
Examples of I/O bound tasks:
----------------------------
✔ File reading/writing
✔ API calls
✔ Network downloads
✔ Database queries
"""

# Example (pseudo code):
# import urllib.request
#
# def file_download(url, filename):
#     urllib.request.urlretrieve(url, filename)
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(file_download, urlList, dataList)


# =====================================================
# RACE CONDITION EXAMPLE
# =====================================================

"""
Race Condition:
---------------
✔ Jab multiple threads same shared resource ko
✔ bina synchronization ke access karein
✔ Output unpredictable ho jata hai
"""

shared_counter = 0


# =====================================================
# LOCK (THREAD SAFETY)
# =====================================================

counter_lock = threading.Lock()
"""
Lock:
-----
✔ Ek time pe sirf ek thread critical section me ja sakta hai
✔ Data corruption prevent karta hai
"""


def increment_shared_counter(x):
    """
    Shared variable ko safely increment karna
    """
    global shared_counter

    # Critical section
    with counter_lock:
        shared_counter += 1
        print(f"Thread {x} incremented counter to {shared_counter}")
        time.sleep(1)   # lock hold rahega jab tak sleep complete nahi hota


# Creating multiple threads
threads = [
    threading.Thread(target=increment_shared_counter, args=(i,))
    for i in [1, 2, 3, 4, 5]
]

# Start threads
for thread in threads:
    thread.start()

# Wait for completion
for thread in threads:
    thread.join()


print("\nFinal counter value:", shared_counter)
