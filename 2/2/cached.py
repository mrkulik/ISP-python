my_cache = dict()


def cached(func):
    def wrapper(*args, **kwargs):
        if not my_cache.get(func.__name__):
            my_cache[func.__name__] = {}

        if my_cache[func.__name__].get((args, frozenset(kwargs.items()))):
            print "from cache"
            return my_cache[func.__name__].get((args, frozenset(kwargs.items())))

        result = func(*args, **kwargs)
        my_cache[func.__name__][(args, frozenset(kwargs.items()))] = result
        print "cached"
        return result
    return wrapper


@cached
def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)


print fact(6)
print my_cache
print fact(7)