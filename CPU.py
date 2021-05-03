import numpy as np
import time
from numba import vectorize, cuda

NUM_ELEMENTS = 16

def Add(a, b):
    return a + b

def Subtract(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Modulus(a, b):
    return a % b

# TODO: Implement Caesar Cipher Encryption, Decryption, and Exhaustive
"""
def Encrypt(a, b):
    return 

def Decrypt(a, b):
    return 

def Exhaust(a, b):
    return 

"""


def initialize_host_vectors():
    A = [x for x in range(NUM_ELEMENTS)]
    A = np.array(A, dtype=np.int8)
    B = np.random.randint(0, 5, len(A), dtype=np.int8)
    return A, B


def print_output(add, sub, mult, mod):
    print("Vector Addition Output:\n", add)
    print("Vector subtraction Output:\n", sub)
    print("Vector Multiplication Output:\n", mult)
    print("Vector Modulus Output:\n", mod)


if __name__ == '__main__':
    # initialize host vectors
    A, B = initialize_host_vectors()

    # print input vectors
    print("Input A Vector:\n", A)
    print("Input B Vector:\n", B)

    # start timer
    start = time.time()

    # call kernel functions
    add_output = Add(A, B)
    sub_output = Subtract(A, B)
    mult_output = Multiply(A, B)
    mod_output = Modulus(A, B)

    # stop timer, record
    performance_time = time.time() - start

    # print output
    print_output(add_output, sub_output, mult_output, mod_output)
    print("Vector operations took {} seconds".format(performance_time))
