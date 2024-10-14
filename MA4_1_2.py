
"""
Solutions to module 4
Review date:
"""

student = "Raffael Wendlinger"
reviewer = "somebody"

import math as m
import numpy as np
import random as rnd
import functools

def sphere_vol_oneliner_for_lulz(n, d, r = 1):
    #readability is overrated
    return len(list(filter(lambda x: x <= r**2, [functools.reduce(lambda x, y: x + y, map(lambda x: x**2, coords)) for coords in [[rnd.uniform(-1, 1) for _ in range(d)] for _ in range(n)]]))) / n * (2 * r)**d

def sphere_volume(n, d, r = 1):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere
    if d <= 0:
        raise ValueError("The dimension of the sphere must be greater than 0")
    if n <= 0:
        raise ValueError("The number of points must be greater than 0")
    
    #creates a list of n lists which contain d number of dimesional coordiante values
    lst = [[rnd.uniform(-1,1) for _ in range(d)] for _ in range(n)]
    #print(lst)

    #creates a list of the distance from center of these multidimensional coords
    sq_lst = [functools.reduce(lambda x,y : x+y, map(lambda x: x**2, coords)) for coords in lst]
    #print(sq_lst)

    #creates a list of the number of points that are within the sphere
    in_sphere_lst = list(filter(lambda x: x <= r**2, sq_lst))
    #print(in_sphere_lst)

    #calculates the volume of the sphere
    vol = len(list(filter(lambda x: x <= r**2, sq_lst)))/n*(2*r)**d 
    return vol

def hypersphere_exact(n, d, r = 1):
    vol = m.pi**(d/2)/m.gamma(d/2 + 1)*r**d
    return vol
     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)

def testmain():
    n = 10000
    d = 3
    sphere_volume(n,d)
    hypersphere_exact(n,d)


if __name__ == '__main__':
    testmain()
	#main()
