# -*- coding: utf-8 -*-
import time


def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


n = 35

if __name__ == "__main__":
    start_time = time.time()
    print(fib(n))
    print(time.time() - start_time)

print(2 % 19)
