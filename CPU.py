#!/usr/bin/env python3

"""
Alejandro Rubio
EN605.617
CPU.py
"""

import time
import random

"""
The below functions execute vector addition, subtraction,
multiplication, modulus, and Caesar Encryption/Decryption.
"""

def Add(a, b):
    c_add= []
    for i in range(0,len(a)):
        c_add.append(a[i] + b[i])
    return c_add

def Subtract(a, b):
    c_sub = []
    for i in range(0,len(a)):
        c_sub.append(a[i] - b[i])
    return c_sub

def Multiply(a, b):
    c_mult = []
    for i in range(0,len(a)):
        c_mult.append(a[i] * b[i])
    return c_mult

def Modulus(a, b):
    c_mod = []
    for i in range(0,len(a)):
        if b[i] == 0:
            c_mod.append(0)
        else:
            c_mod.append(a[i] % b[i])
    return c_mod

def Encrypt(message, shift):
    # apply shift and normalize to ASCII
    Encrypted = []
    for i in range(0,len(message)):
        Encrypted.append(((message[i]+shift) % 26) + 97)
    return Encrypted

def Decrypt(message, shift):
    # apply shift and normalize to ASCII
    Decrypted= []
    for i in range(0,len(message)):
        Decrypted.append(((message[i]-shift) % 26) + 97)
    return Decrypted

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
            if msg[i].isupper():#catch upper case
               upper_case.append(i)

            message.append((ord(msg[i].lower()) - 97) % 26)
        else:#catch punctuation
            punctuation.append((i, msg[i]))

    return message, punctuation, upper_case

def initialize_host_vectors(NUM_ELEMENTS):
    B = []
    A = [x for x in range(NUM_ELEMENTS)]
    for i in range(0, NUM_ELEMENTS):
        B.append(random.randint(0,5))

    return A, B


def print_output(add, sub, mult, mod):
    """
    Prints the output of the vector operations
    """
    print("Vector Addition Output:\n", add)
    print("Vector subtraction Output:\n", sub)
    print("Vector Multiplication Output:\n", mult)
    print("Vector Modulus Output:\n", mod)
    #print("Encrypted Message:\n",(encrypt))

def print_caesar(encrypt, msg_len, puncutation, upper_case):
    """
    Prints Encrpyion/Decryption result restoring capitals and
    punctuation.
    """
    scale_back = 0 #shift index with inserted punctuation
    for i in range(0, msg_len):
        punc_flag = 0 #track punctuation
        upper_flag = 0 #track capitzaliztion

        for j in range(0, len(puncutation)):
            if i == puncutation[j][0]: # if punctuation
                print(puncutation[j][1], end='')
                scale_back += 1
                punc_flag = 1
                break

        if punc_flag == 1:
            continue

        for j in range(0, len(upper_case)):
            if i == upper_case[j]:#if upper case
                print(chr(encrypt[i - scale_back]).upper(), end='')
                upper_flag = 1
                break

        if(upper_flag == 0):#if lower case
            print(chr(encrypt[i - scale_back]), end='')

    print() #newline

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

    #print input vectors
    '''
    print("CPU Execution:")
    print("Input A Vector:\n", A)
    print("Input B Vector:\n", B)
    '''
    # start timer
    start = time.time()

    # call CPU functions
    add_output = Add(A, B)
    sub_output = Subtract(A, B)
    mult_output = Multiply(A, B)
    mod_output = Modulus(A, B)
    encrypt_output = Encrypt(message, shift)
    decrypt_output = Decrypt(encr_message, dec_shift)

    # stop timer, record
    performance_time = time.time() - start

    '''
    # print output
    print_output(add_output, sub_output, mult_output, mod_output)
    print("Caesar Encryption: ",end='')
    print_caesar(encrypt_output, len(msg_str), punctuation, uppers)
    print("Caesar Decryption: ",end='')
    print_caesar(decrypt_output, len(encr_str), encr_punctuation, enc_uppers)
    '''

    return performance_time