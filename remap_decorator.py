def skip_if(self, condition):
    def decorator(f):
        if condition:
            print("Success")
        else:
            print("Failure")
        return f
    return decorator

#These will likely work identically

def skip_if_alt(inst, condition):
    def dec(f):
        def func(*args, **kwargs):
            if condition:
                print("Alt Success")
            else:
                print("Alt Fail")
            return f(*args, **kwargs)
        return func
    return dec

#This is where the differnce occurs - class method vs generic
class A():
    def __init__(self):
        self.var = 1
        #self.test_skipif = skip_if(self, condition = self.var == 1)(self.test_skipif)

#Setup class method with alias, or as shown here
#How will the class be passed in?
a = A()
@skip_if_alt(a, condition=True)
def test_skipif():
    print("Executing Test")

test_skipif()
