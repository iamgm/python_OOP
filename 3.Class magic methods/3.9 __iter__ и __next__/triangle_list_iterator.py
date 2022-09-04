class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
    
    def __iter__(self):
        self.idx = [0,0]
        return self
        
    def __next__(self):
        r, c = self.idx
        if r > len(self.lst)-1:
            raise StopIteration
        self.idx = (r, c + 1) if c < r else (r + 1, 0)
        return self.lst[r][c]


l = [[y for y in range(x+1)] for x in range(10)]
# l = lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11'],
#        ['x20', 'x21', 'x22', 'x23', 'x24'],
#        ['x30', 'x31', 'x32', 'x33']]
[print(x) for x in l]
it = TriangleListIterator(l)
for x in it:
    print(x)

it_iter = iter(it)
# x = next(it_iter)

[([print(next(it), end = " ") for _ in range(x+1)], print()) for x in range(10)]
# it_iter = iter(it)
# x = next(it_iter)
