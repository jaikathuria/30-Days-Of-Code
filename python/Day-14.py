class Difference:
    def __init__(self, a):
        self.__elements = a
        # Add your code here
        self.maximumDifference = 0
    def max(self,a,b):
        if abs(a-b) > self.maximumDifference:
            self.maximumDifference = abs(a-b)
    def computeDifference(self):
        for _ in self.__elements:
            for __ in self.__elements:
                self.max(_,__)

# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
