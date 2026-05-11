"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """

        return self.data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        count = 0
        current = self._head  
        while current is not None:
            count += 1
            current = current.next

        return count
    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved (zero-indexed).

        Returns
            item

        Raises
            IndexError if n >= length
        """
        # Replace the line below with your code
        raise NotImplementedError

    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        # Replace the line below with your code
        raise NotImplementedError

    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        new_node = Node(item)
        current = self._head
        if self._head is None:
            self._head = new_node
            return
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved (zero-indexed).

        Raises
            IndexError if n >= length
        """
        if n < 0:
            raise IndexError("n must be 0 or positive")
        if self._head is None:
            raise IndexError("linked list is empty")
        if n == 0: #head deletion
            self._head = self._head.next
            return
        prev = self._head
        while(
            n > 1
            and prev.next is not None
        ):
            prev = prev.next
            n -= 1
            if prev.next is None:
                raise IndexError("n >= length")
            prev.next = prev.next.next
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        # Replace the line below with your code
        raise NotImplementedError


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    pass
