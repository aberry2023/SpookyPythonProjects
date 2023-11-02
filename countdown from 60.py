import time

start_time = time.time()
for count in range(60, -1, -1):
    print(count)
    time.sleep(1)

stop_time = time.time()

execution_time = stop_time - start_time
print('Program run time:', execution_time, 'seconds.')