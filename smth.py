import random
class smth:
    def __init__(self, from_range, to_range, length):
        if from_range > to_range:
            raise ValueError("from_range must be less than or equal to to_range")
        self.from_range = from_range
        self.to_range = to_range
        self.length = length
    def para(self):
        arr = [random.randint(self.from_range, self.to_range) for i in range(self.length)]
        return arr
s1 = smth(5, 100, 10)
print(s1.para())
