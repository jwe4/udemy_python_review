class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        node.set_next(self.__root)
        self.__root = node

    def remove_start_from_list(self):
        if self.__root:
            node = self.__root
            self.__root = self.__root.get_next()
            return node
        else:
            raise RuntimeError("stack is empty")


    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        marker = self.__root
        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()
        raise LookupError("text: {} was not found".format(text))

    def size(self):
        s = 0
        marker = self.__root
        while marker:
            s += 1
            marker = marker.get_next()
        return s
