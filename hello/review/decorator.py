# -*- coding: utf-8 -*-
import time, functools
def log(k):
    if isinstance(k,str):
        def log2(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print('{}: {}'.format(k, fn.__name__))
                return fn(*args, **kw)
            return wrapper
        return log2
        
    else:
        @functools.wraps(k)
        def wrapper(*args, **kw):
            print('call: {}'.format(k.__name__))
            return k
        return wrapper

@log("execute")
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

f = fast(11, 22)
print('{}'.format(fast.__name__))