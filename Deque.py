class Dque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0,item)
    def add_rear(self, item):
        self.__list.append(item)


    def pop_front(self):
        return self.__list.pop(0)
    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)