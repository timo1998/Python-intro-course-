# thread is a flow of execution. Like a seperate order of instructions. 

import threading
import time 

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
    
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")
    
def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target = eat_breakfast, args=())
x.start()

y = threading.Thread(target = drink_coffee, args=())
y.start()

z = threading.Thread(target = study, args=())
z.start()

# =============================================================================
# Met het volgende programma kunnen we de main thread laten wachten totdat een bepaalde thread klaar is
# x.join()
# y.join()
# z.join()
# =============================================================================
   
    
    
print(threading.active_count())
print(threading.enumerate())