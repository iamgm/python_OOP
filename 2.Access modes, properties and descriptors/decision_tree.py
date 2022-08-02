class TreeObj:
    def __init__(self, indx, value = None):
        if type(indx) == int:
            self.indx = indx
        if type(value) == str:
            self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val

class DecisionTree:
    def __init__(self):
        pass

    @classmethod
    def predict(cls, root, x):
        x.reverse()
        node = root
        while len(x)>1:
            item = x.pop()
            if item:
                node = node.left
            else:
                node = node.right
        print(node.value)

    @classmethod
    def add_obj(cls, obj, node = None, left = True):
        if node:
            print(node)
            if left:
                node.left = obj
                return node.left
            else:
                node.right = obj 
                return node.right
        else:
            return obj



root = DecisionTree.add_obj(TreeObj(0))
print("root ", root)
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
print(v_11, v_12)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)