import CPU
import GPU
import sys

if __name__ == '__main__':
    print(sys.maxsize)
    for i in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        cpu_time = CPU.driver(i)
        gpu_time = GPU.driver(i)

        print(f"Time to run on CPU with {i} elements, is {cpu_time}")
        print(f"Time to run on GPU with {i} elements, is {gpu_time}")
        print()
