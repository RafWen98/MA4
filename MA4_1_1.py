"""
Solutions to module 4
Review date:
"""

student = "Raffael Wendlinger"
reviewer = "somebody"


import random as r
import matplotlib.pyplot as plt

import math
import numpy as np 

def approximate_pi(n):
    n_in = 0
    n_out = 0

    for i in range(n):
        x = r.uniform(-1,1)
        y = r.uniform(-1,1)
        if x**2 + y**2 <= 1:
            n_in += 1
            plt.plot(x,y, 'ro')
        else:
            n_out += 1
            plt.plot(x,y, 'bo') 
    
    pi = 4 * n_in / n
    print("Approximation of pi with", n, "dots:", pi)
    plt.title("Approximation of pi with " + str(n) + " dots")
    plt.axis('equal')
    plt.show()
    plt.savefig('.\pi_approx_' + str(n) + '.png')
    return
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
