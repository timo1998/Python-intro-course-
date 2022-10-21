# multiprocessing, running task in parallel on different cpu cores
# better for cpu bound tasks while multithreading is better for IO tasks

from multiprocessing import Process, cpu_count
import time 

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    
# =============================================================================
#     a = Process(target = counter, args=(500000000,))
#     b = Process(target = counter, args=(500000000,))
#     
#     a.start()
#     b.start()
#     
#     a.join()
#     b.join()
# =============================================================================
    
      print("finished in: ",time.perf_counter()," seconds")
      print(cpu_count())


if __name__ == '__main__':
    main()
    
    


