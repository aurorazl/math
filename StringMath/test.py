def wrap(cls):
    def inner():
        if not cls.instance:
            cls.instance = cls()
        return cls.instance
    return inner
@wrap
class foo:
    instance = None
    def __init__(self):
        self.name = 'czl'
    def func(self):
        print('666')
a = foo()
b = foo()

print(id(a))
print(id(b))