import numpy as np

import time
import tracemalloc
import functools

def timedit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(
            f"Function '{func.__name__}' executed in "
            f"{end_time - start_time:.4f}s | "
            f"Peak memory: {peak / 1024 / 1024:.2f} MB"
        )

        return result
    return wrapper

@timedit
def functen(A,B):
    return A@B

def main():
    x = np.ones((10,10))

    A = np.ones((100,100))
    B = np.ones((100,100))*2
    functen(A,B)


    


if __name__ == "__main__":
    main()
