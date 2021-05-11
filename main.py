"""
Alejandro Rubio
EN606.617
main.py
"""


import CPU
import GPU

if __name__ == '__main__':
    for i in [10,100,1000,10000,100000,1000000,10000000,100000000,500000000]:
        #tests where i is the number of elements

        cpu_time = CPU.driver(i)
        gpu_time = GPU.driver(i)

        print(f"Time to run on CPU with {i} elements, is {cpu_time} seconds.")
        print(f"Time to run on GPU with {i} elements, is {gpu_time} seconds.")
        print()
