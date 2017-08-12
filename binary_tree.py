class BinaryTree:
    """
    This class is a binary tree implementation.

    Don't modify class or method names, just implement methods that currently raise
    a NotImplementedError!
    """

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add(self, node):
        """
        You should implement this method.
        It should add a node to the binary tree.
        If a node with that value already exists, raise a ValueError
        :param node: The Node to add
        :return: None
        """
        # The root is None, so set the root to be the new Node.
        if not self.__root:
            self.__root = node
        else:
            # Start iterating over the tree.
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    # Raise a ValueError, because the node's value already exists.
                    raise NotImplementedError()
                elif node.value > marker.value:
                    slot = marker.get_right()
                    if slot is None:
                        marker.set_right(node)
                    marker = slot
                else:
                    slot = marker.get_left()
                    if slot is None:
                        marker.set_left(node)
                    marker = slot

    def find(self, value):

        marker = self.__root
        while marker:
            if marker:
                if value == marker.value:
                    return marker
                if value > marker.value:
                    marker = marker.get_right()
                else:
                    marker = marker.get_left()
        raise LookupError("value: {} not found".format(value))


    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        print(current_node.print_details())
        self.__print_inorder_r(current_node.get_right())