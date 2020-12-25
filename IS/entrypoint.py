import time

from src.pool import Pool
from config import (
    GOAL,
    GENES,
)

if __name__ == '__main__':
    start_time = time.time()
    breed_pool = Pool(100, GOAL, GENES)
    steps = breed_pool.evolution()
    print(f"Steps: {steps}")
    print(f"Execution time: {time.time() - start_time}")
