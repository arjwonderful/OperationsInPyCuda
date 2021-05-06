import time
import random

NUM_ELEMENTS = 100000000

def Add(a, b):
    c = []
    for i in range(0,len(a)):
        c.append(a[i] + b[i])
    return c

def Subtract(a, b):
    c = []
    for i in range(0,len(a)):
        c.append(a[i] - b[i])
    return c

def Multiply(a, b):
    c = []
    for i in range(0,len(a)):
        c.append(a[i] * b[i])
    return c

def Modulus(a, b):
    c = []
    for i in range(0,len(a)):
        if b[i] == 0:
            c.append(0)
        else:
            c.append(a[i] % b[i])
    return c

def Encrypt(message, shift):
    Encrypted = []
    for i in range(0,len(message)):
        Encrypted.append(((message[i]+shift) % 26) + 97)
    return Encrypted

def Decrypt(message, shift):
    Decrypted= []
    for i in range(0,len(message)):
        Decrypted.append(((message[i]-shift) % 26) + 97)
    return Decrypted

def initialize_host_message(msg):
    message = []
    punctuation = []
    upper_case = []
    for i in range(0,len(msg)):
        if msg[i].isalpha():
            if msg[i].isupper():
               upper_case.append(i)
            message.append((ord(msg[i].lower()) - 97) % 26)
        else:
            punctuation.append((i, msg[i]))

    return message, punctuation, upper_case

def initialize_host_vectors():
    B = []
    A = [x for x in range(NUM_ELEMENTS)]
    for i in range(0, NUM_ELEMENTS):
        B.append(random.randint(0,5))

    return A, B


def print_output(add, sub, mult, mod):
    print("Vector Addition Output:\n", add)
    print("Vector subtraction Output:\n", sub)
    print("Vector Multiplication Output:\n", mult)
    print("Vector Modulus Output:\n", mod)
    #print("Encrypted Message:\n",(encrypt))

def print_caesar(encrypt, msg_len, puncutation, upper_case):
    scale_back = 0
    for i in range(0, msg_len):
        flag = 0
        upper_flag = 0
        for j in range(0, len(puncutation)):
            if i == puncutation[j][0]:
                print(puncutation[j][1], end='')
                scale_back += 1
                flag = 1
                break
        if flag == 1:
            continue

        for j in range(0, len(upper_case)):
            if i == upper_case[j]:
                print(chr(encrypt[i - scale_back]).upper(), end='')
                upper_flag = 1
                break
        if(upper_flag == 0):
            print(chr(encrypt[i - scale_back]), end='')
    print()

if __name__ == '__main__':
    msg_str = "Hello World!"
    shift = 6

    encr_str = "Nkrru Cuxrj!"
    dec_shift = 6
    # initialize host vectors
    A, B = initialize_host_vectors()
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

    # print output
    #print_output(add_output, sub_output, mult_output, mod_output)
    #print_caesar(encrypt_output, len(msg_str), punctuation, uppers)
    #print_caesar(decrypt_output, len(encr_str), encr_punctuation, enc_uppers)
    print("Vector operations took {} seconds".format(performance_time))
