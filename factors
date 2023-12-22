#!/usr/bin/python3
import sys
import time


def factors(file):
    start_process_time = time.process_time()

    with open(file) as f:
        numbers = f.readlines()

    for number in numbers:
        number = int(number)
        factor_found = False
        for x in range(2, number):
            if number % x == 0:
                p = x
                q = number // x
                factor_found = True
                print(f"{number}={p}*{q}")
                break

        if not factor_found:
            print("Factors not found for", number)

    end_time = time.perf_counter()
    end_process_time = time.process_time()

    real_time = end_time - start_process_time
    user_time = end_process_time - start_process_time
    sys_time = real_time - user_time

    print(f"real\t{real_time:.3f}s")
    print(f"user\t{user_time:.3f}s")
    print(f"sys\t{sys_time:.3f}s")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: factors.py <filename>")
        sys.exit(1)

    else:
        file = sys.argv[1]
        factors(file)
