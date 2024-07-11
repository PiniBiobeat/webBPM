import subprocess
import threading
import time
import psutil
import os


def run_pytest():
    command = [
        "pytest",
        "-v",
        "-s",
        r"C:\Users\tester\Desktop\repositories\pytest-lupa\tests\TestCalendar\test_sending_calendar.py"
    ]
    subprocess.run(command, check=True)


def run_thread(thread_num):
    print(f"Thread {thread_num} starting")
    start_time = time.time()
    run_pytest()
    end_time = time.time()
    print(f"Thread {thread_num} finished in {end_time - start_time:.2f} seconds")


def get_safe_thread_count():
    # Get the number of CPU cores
    cpu_count = os.cpu_count()
    # Use a conservative number of threads, e.g., 2 times the number of cores
    return max(1, cpu_count * 2)


def main():
    target_cpu_percent = 80
    max_threads = get_safe_thread_count()

    print(f"Running with a maximum of {max_threads} threads")

    threads = []
    active_threads = 0

    while True:
        current_cpu = psutil.cpu_percent(interval=1)

        if current_cpu < target_cpu_percent and active_threads < max_threads:
            thread = threading.Thread(target=run_thread, args=(len(threads) + 1,))
            threads.append(thread)
            thread.start()
            active_threads += 1
        elif current_cpu > target_cpu_percent + 5:  # Allow some fluctuation
            time.sleep(1)  # Wait a bit before checking again

        # Clean up finished threads
        active_threads = sum(1 for t in threads if t.is_alive())

        if active_threads == 0 and len(threads) > 0:
            print("All threads completed")
            break

        time.sleep(1)  # Small delay to prevent tight looping


if __name__ == "__main__":
    main()