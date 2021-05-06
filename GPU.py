#!/usr/bin/env python3

"""
Alejandro Rubio
EN606.617
GPU.py
"""

import numpy as np
import time
from numba import vectorize, cuda


"""
The below kernels execute vector addition, subtraction,
multiplication, modulus, and Caesar Encryption/Decryption.
Executed using CUDA library.
"""

@vectorize(['int8(int8, int8)'], target='cuda')
def Add(a, b):
    return a + b

@vectorize(['int8(int8, int8)'], target='cuda')
def Subtract(a, b):
    return a - b

@vectorize(['int8(int8, int8)'], target='cuda')
def Multiply(a, b):
    return a * b

@vectorize(['int8(int8, int8)'], target='cuda')
def Modulus(a, b):
    return a % b

@vectorize(['int8(int8, int8)'], target='cuda')
def Encrypt(message, shift):
    #apply shift and normalize to ASCII
    return (((message+shift) % 26) + 97)

@vectorize(['int8(int8, int8)'], target='cuda')
def Decrypt(message, shift):
    #apply shift and normalize to ASCII
    return (((message - shift) % 26) + 97)

def initialize_host_vectors(NUM_ELEMENTS):
    # A contains 0-NUM_ELEMETNS ascending
    A = [x for x in range(NUM_ELEMENTS)]
    A = np.array(A, dtype=np.int8)

    #B contains random numbers between 0,5, leng NUM_ELEMENTS
    B = np.random.randint(0, 5, len(A), dtype=np.int8)

    return A, B

def initialize_host_message(msg):
    """
    Initilizes array from string, tracking letters, capitalization
    and punctuation.
    """
    message = []
    punctuation = []
    upper_case = []

    for i in range(0,len(msg)):
        if msg[i].isalpha():
            if msg[i].isupper(): #catch upper case
               upper_case.append(i)

            message.append((ord(msg[i].lower()) - 97) % 26)
        else: #catch punctuation
            punctuation.append((i, msg[i]))

    #convert to numpyarray
    message = np.array(message, dtype=np.int8)
    return message, punctuation, upper_case

def print_output(add, sub, mult, mod, ):
    """
    Prints the output of the vector operations
    """
    print("Vector Addition Output:\n", add)
    print("Vector subtraction Output:\n", sub)
    print("Vector Multiplication Output:\n", mult)
    print("Vector Modulus Output:\n", mod)

def print_caesar(encrypt, msg_len, punctuation, upper_case):
    """
    Prints Encrpyion/Decryption result restoring capitals and
    punctuation.
    """
    scale_back = 0 #shift index with inserted punctuation

    for i in range(0, msg_len):
        punc_flag = 0 #track punctuation
        upper_flag = 0 #track capitzaliztion

        for j in range(0, len(punctuation)):
            if i == punctuation[j][0]: # if punctuation
                print(punctuation[j][1], end='')
                scale_back += 1
                punc_flag = 1
                break

        if punc_flag == 1:
            continue

        for j in range(0, len(upper_case)):
            if i == upper_case[j]: #if upper case
                print(chr(encrypt[i - scale_back]).upper(), end='')
                upper_flag = 1
                break
        if(upper_flag == 0): #if lower case
            print(chr(encrypt[i - scale_back]), end='')

    print()#newline

def driver(NUM_ELEMENTS):
    """
    Driver code for vector operations and 
    performance metrics.
    """
    msg_str = "Hello World!"
    shift = 6

    encr_str = "Nkrru Cuxrj!"
    dec_shift = 6

    # initialize host vectors
    A, B = initialize_host_vectors(NUM_ELEMENTS)
    message, punctuation, uppers = initialize_host_message(msg_str)
    encr_message, encr_punctuation, enc_uppers = initialize_host_message(encr_str)

    # print input vectors
    #print("Input A Vector:\n", A)
    #print("Input B Vector:\n", B)

    # start timer
    start = time.time()

    # call kernel functions
    add_output = Add(A, B)
    sub_output = Subtract(A, B)
    mult_output = Multiply(A, B)
    mod_output = Modulus(A, B)
    encrypt_output = Encrypt(message, shift)
    decrypt_output = Decrypt(encr_message, dec_shift)

    # stop timer, record
    performance_time = time.time() - start

    #print output
    #print_output(add_output, sub_output, mult_output, mod_output)
    #print_caesar(encrypt_output, len(msg_str), punctuation, uppers)
    #print_caesar(decrypt_output, len(encr_str), encr_punctuation, enc_uppers)
    return performance_time