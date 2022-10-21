import time 

# =============================================================================
# print(time.ctime(0)) #geeft de datum aan die volgens de computer hoort bij het argument
# 
# print(time.time()) # geeft het aantal verstreken seconden sinds 1 januarie 1970
# 
# print(time.ctime(time.time())) #de actuele tijd verkrijgen. 
# 
# time_object = time.localtime()
# print(time_object)
# 
# local_time = time.strftime("%B", time_object)
# print(local_time)
# 
# =============================================================================

#Of van een string naar een getal:
    
# =============================================================================
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")    
# print(time_object)
# =============================================================================

time_tuple = (2020, 4, 20, 4, 20, 0, 0 , 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)