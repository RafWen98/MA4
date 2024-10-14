
"""
Solutions to module 4
Review date:
"""

student = "Raffael Wendlinger"
reviewer = "somebody"

import math as m
import random as rnd
import functools

from time import perf_counter as pc
from time import sleep as pause

import concurrent.futures as future
import multiprocessing as mp

def sphere_volume(n, d, r = 1):
    #readability is overrated
    return len(list(filter(lambda x: x <= r**2, [functools.reduce(lambda x, y: x + y, map(lambda x: x**2, coords)) for coords in [[rnd.uniform(-1, 1) for _ in range(d)] for _ in range(n)]]))) / n * (2 * r)**d

def hypersphere_exact(n, d, r = 1):
    return m.pi**(d/2)/m.gamma(d/2 + 1)*r**d

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function 

    # Create a pool of processes
    with mp.Pool(np) as pool:
        # Run 10 parallel invocations of the sphere_volume function
        results = pool.starmap(sphere_volume, [(n, d) for _ in range(10)])
    
    #return what??? a single result? makes nooooo snese that function.... pls
    return results[0]
   
def sphere_chunk(n,d, r=1):
    return len(list(filter(lambda x: x <= r**2, [functools.reduce(lambda x, y: x + y, map(lambda x: x**2, coords)) for coords in [[rnd.uniform(-1, 1) for _ in range(d)] for _ in range(n)]])))


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np, r=1):
    
    # Divide the total number of samples 'n' into 'np' chunks
    chunk_size = n // np
    
    # Create a pool of processes
    with mp.Pool(np) as pool:
        # Run each process with a chunk of the total data
        counts = pool.starmap(sphere_chunk, [(chunk_size, d) for _ in range(np)])
        print(counts)
    
    n_total = functools.reduce(lambda x, y: x + y, counts)
    print(n_total)

    vol = n_total / n * (2 * r)**d
    return vol

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    #time normal sphere calc
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    end = pc()
    print(f"Normal process took {round(end-start, 2)} seconds")

    #time parallel sphere calc
    start = pc()
    sphere_volume_parallel1(n,d,10)
    end = pc()
    print(f"Parallel process took {round(end-start, 2)} seconds")

    #time data splitting parallel sphere calc
    start = pc()
    sphere_volume_parallel2(n,d,10)
    end = pc()
    print(f"Data split Parallel process took {round(end-start, 2)} seconds")
    


if __name__ == '__main__':
	main()
