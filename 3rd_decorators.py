import time 

def cache(func):
    cache_value = {}
    print(cache_value,"intial state")
        
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        resuslt = func(*args)
        cache_value[args] = resuslt
        return resuslt

    return wrapper
@cache
def check(a,b):
    time.sleep(5)
    return a+b

print(check(9,2))