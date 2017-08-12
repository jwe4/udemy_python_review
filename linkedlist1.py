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

    def remove_end_from_list(self):
        marker = self.__root
        while marker:
            following = marker.get_next()
            if following is None:
                self.__root = None
                return marker
            if following.get_next() is None:
                marker.set_next(None)
                return following
            marker = following
        return marker

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Name: {} was not found".format(name))

    def size(self):
        s = 0
        marker = self.__root
        while marker:
            s += 1
            marker = marker.get_next()
        return s

