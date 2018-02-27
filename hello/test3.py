import time
from multiprocessing import Process, current_process


def func():
    time.sleep(1)
    proc = current_process()
    proc.name, proc.pid


sub_proc = Process(target=func, args=())
sub_proc.start()
sub_proc.join()
proc = current_process()
proc.name, proc.pid
