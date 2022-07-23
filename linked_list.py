
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ["abc","cdf", "efg", "jkl", "mno"] # test data


class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data
    
    def link(self, obj):
        self.next_obj = obj


itt = iter(lst_in)
head_obj = ListObject(next(itt))

def fill_linked_list(obj, it):
    try:
        tail = obj.link(ListObject(next(it)))
        return fill_linked_list(obj.next_obj, it)    
    except StopIteration as e:
        pass
    

fill_linked_list(head_obj, itt)
