class Factory:
    def __init__(self):
        pass

    def build_sequence(self):
        # self.seq = []
        return []

    def build_number(self, sub):
        self.sub = float(sub.strip())
        return self.sub    


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
