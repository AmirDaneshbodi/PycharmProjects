def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper
memo = {}
@counted
def f(x, y, z):
    if not (x, y, z) in memo:
        memo[(x, y, z)] = x + y * z ** 2.0
    print memo
    return memo[(x, y, z)]

print f(1,2,3)
print f(1,2,4)
print f(1,2,3)
print f(1,2,3)
print memo
print f.called