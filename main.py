class Node:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next

    def get_data(self):
        return self.__data

    def __str__(self):
        s1, s2 = "", ""

        if self.__prev__ == None:
            s1 = "None"
        else:
            s1 = str(self.__prev__.get_data())

        if self.__next__ == None:
            s2 = "None"
        else:
            s2 = str(self.__next__.get_data())

        return "data: {}, prev: {}, next: {}".format(self.__data, s1, s2)


class LinkedList:
    def __init__(self, first=None, last=None):
        if (first == None) and (last == None):
            self.__length = 0
            self.__first__ = None
            self.__last__ = None
        elif (first == None) and (last != None):
            raise ValueError("invalid value for last")
        elif (first != None) and (last == None):
            self.__length = 1
            self.__first__ = Node(first)
            self.__last__ = self.__first__
        else:
            self.__length = 2
            self.__first__ = Node(first, next=self.__last__)
            self.__last__ = Node(last, prev=self.__prev__)

    def __len__(self):
        return self.__length

    def __str__(self):
        begin = self.__first__
        values = []

        while begin != None:
            values.append(str(begin))
            begin = begin.__next__

        if self.__length > 0:
            return "LinkedList[length = {}, [{}]]".format(self.__length, "; ".join(values))
        else:
            return "LinkedList[]"

    def append(self, element):
        if self.__length == 0:
            self.__first__ = Node(element)
            self.__last__ = self.__first__
        else:
            self.__last__.__next__ = Node(element, prev=self.__last__)
            self.__last__ = self.__last__.__next__

        self.__length += 1

    def clear(self):
        self.__length = 0
        self.__first__ = None
        self.__last__ = None

    def pop(self):
        if self.__length <= 0:
            raise IndexError("LinkedList is empty!")
        else:
            self.__length -= 1
            self.__last__.__prev__.__next__ = None
            self.__last__ = self.__last__.__prev__

    def popitem(self, element):
        if self.__length <= 0:
            raise IndexError("LinkedList is empty!")
        else:
            begin = self.__first__
            isExists = False

            for i in range(self.__length):
                if begin.get_data() == element:
                    isExists = True
                    break
                else:
                    begin = begin.__next__

            if isExists:
                if begin is self.__last__:
                    self.__last__.__prev__.__next__ = None
                    self.__last__ = self.__last__.__prev__
                elif begin is self.__first__:
                    self.__first__.__next__.__prev__ = None
                    self.__first__ = self.__first__.__next__
                else:
                    begin.__next__.__prev__ = begin.__prev__
                    begin.__prev__.__next__ = begin.__next__
                self.__length -= 1
            else:
                raise KeyError("{} doesn't exist!".format(element))


linked_list = LinkedList()
print(linked_list) # LinkedList[]
print(len(linked_list)) # 0

linked_list.append(10)
print(linked_list) # LinkedList[length = 1, [data: 10, prev: None, next: None]]
print(len(linked_list)) # 1

linked_list.append(20)
print(linked_list)
# LinkedList[length = 2, [data: 10, prev: None, next: 20; data: 20, prev: 10, next: None]]
print(len(linked_list)) # 2

linked_list.popitem(20)
print(linked_list)
print(linked_list) # LinkedList[length = 1, [data: 10, prev: None, next: None]]
print(len(linked_list)) # 1
