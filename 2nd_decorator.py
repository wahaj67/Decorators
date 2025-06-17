
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kw_args_value = ', '.join(f'{k}={v}' for k,v, in kwargs.items())
        print(f'Calling function name: {func.__name__} with args {args_value} and kwargs {kw_args_value}')
        return func(*args,**kwargs)
    return wrapper
@debug
def add(n1,n2):
    return n1 + n2

print(add(56,87),'haha')