class ArrayList:

    def __init__(self):
        self.list = []

    def insert(self, data):
        self.list.append(data)

    def delete_at_index(self, index):
        self.list.pop(index)

    def delete_after(self, index):
        if len(self.list) > index + 1:
            self.list.pop(index + 1)

    def delete_before(self, index):
        if index - 1 >= 0:
            self.list.pop(index - 1)

    def insert_at_index(self, index, newD):
        self.list.insert(index, newD)

    def insert_after(self, index, newD):
        self.list.insert(index + 1, newD)

    def insert_before(self, index, newD):
        if index - 1 >= 0:
            self.list.insert(index - 1, newD)

    def display(self):
        for i in self.list:
            print(i, end=',')

    def returnAllDesc(self):
        for i in reversed(self.list):
            print(i)

    def returnLength(self):
        return len(self.list)

    def sortAsc(self):
        for i in range(1, self.returnLength()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j+1] = key

    def sortDesc(self):
        for i in range(1, self.returnLength()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key > self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key