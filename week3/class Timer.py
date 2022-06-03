'''
# SIMPLE VERSION

import time
class Timer:
    
    def __init__(self):
        self._start_time = 0
        self._elapsed_time = 0
        
    def start(self):
        self._start_time = time.perf_counter()
        
    def stop(self):
        self._elapsed_time = time.perf_counter() - self._start_time
        
    def elapsed(self):
        return self._elapsed_time
'''        

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
           raise TimerError("Timer is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
           raise TimerError("Timer has not been run yet. Use .start()")
        return(self_elapsed_time)

    def __str__(self):
        """print() prints elapsed time"""
        return(str(self._elapsed_time))
        
    



















