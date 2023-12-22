#!/usr/bin/python3
import sys
import time


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def factors(file):
    with open(file) as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    for number in numbers:
        for i in range(2, number):
            if number % i == 0 and is_prime(i) and is_prime(number // i):
                p = i
                q = number // i
                print(f"{number}={p}*{q}")
                break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: rsa.py <filename>")
        sys.exit(1)

    else:
        file_path = sys.argv[1]
        #start_time = time.time()
        factors(file_path)
        #end_time = time.time()
        #elapsed_time = end_time - start_time
        #print(f"Execution Time: {elapsed_time:.4f} seconds")
