class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, arg1, *args):
        total = 0
        if isinstance(arg1, int) or isinstance(arg1, float):
            total += arg1
        else:
            for i in arg1:
                total += i

        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                total += arg
            else:
                for i in arg:
                    total += i
        
        self.result += total
        return self

    def subtract(self, arg1, *args):
        total = 0
        if isinstance(arg1, int) or isinstance(arg1, float):
            total += arg1
        else:
            for i in arg1:
                total += i

        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                total += arg
            else:
                for i in arg:
                    total += i

        self.result -= total
        return self

md = MathDojo()
print md.add([1], 3, 4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2, 3], [1.1, 2.3]).result
