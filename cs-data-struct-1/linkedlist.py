# Linked list with Node/LinkedList classes

class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data

# class ListNotLongEnough(Exception):
#     """Exception error."""

#     def return_error():
#         return 'Traceback (most recent call last):\n...\nException: List not long enough'


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    # def return_error():
    #     return 'Traceback (most recent call last):\n...\nException: List not long enough'

    def remove_node_by_index(self, index):
        """Remove node with given index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.print_list()
            dog
            cat
            fish
        """
        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def get_node_by_index(self, idx):
        """Return a node with the given index::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.get_node_by_index(0)
            <Node dog>

            >>> ll.get_node_by_index(2)
            <Node fish>

            >>> ll.get_node_by_index(4)
            Traceback (most recent call last):
            ...
            Exception: List not long enough
        """

        counter = 0
        current = self.head

        while current is not None:
            if counter != idx:
                counter += 1
                current = current.next
            else:
                return current

        # Wasn't sure how to raise the exception error. Also see lines 13 and 40.

        # counter = 0
        # current = self.head

        # while current is not None:
        #     if counter != idx:
        #         counter += 1
        #         current = current.next
        #     elif (current == None) and (idx > counter):
        #         return return_error()
        #     else:
        #         return current


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
