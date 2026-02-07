import threading, time

def hundredk_loop(name):
    for i in range(100_000):
        time.sleep(0.000_1)
    print(f'loop running {name}, 100_000 loops done\n')

def loop1_n_time(number):
    current_time = time.time()
    for n in range(number):
        name = f'sequentially {n+1}'
        hundredk_loop(name)
    elapse_time = time.time() - current_time
    print(f'Elapse time is: {elapse_time:.2f} for loop sequential\n')

def loop2_n_time(number):
    threads = list()
    current_time = time.time()
    for n in range(number):
        name = f'as thread {n+1}'
        th = threading.Thread(
            target = hundredk_loop,
            args = (name,)
        )
        threads.append(th)
        th.start()
    
    for thread in threads:
        thread.join()

    elapse_time = time.time() - current_time
    print(f'Elapse time is: {elapse_time:.2f} for thread')        

loop1_n_time(10)
loop2_n_time(10)