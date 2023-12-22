#!/usr/bin/python3
import sys
import time


def factors(file):
    with open(file) as f:
        numbers = f.readlines()
    print(numbers)

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

    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print("Please provide the filename as an argument.")
    else:
        file_path = sys.argv[1]
        factors(file_path)
