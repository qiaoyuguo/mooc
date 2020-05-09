# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

######################
#### Linked Lists ####
######################

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print_link(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"


def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"


def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    "*** YOUR CODE HERE ***"


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print_link(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print_link(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    "*** YOUR CODE HERE ***"


def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print_link(new)
    <1 4 1>
    """
    "*** YOUR CODE HERE ***"


## Optional Questions

def rotate(link, n):
    """Rotates the Link so that its elements are shifted to the right n times.

    >>> link = Link(1, Link(2, Link(3)))
    >>> link = rotate(link, 0)
    >>> link
    Link(1, Link(2, Link(3)))
    >>> link = rotate(link, 1)
    >>> link
    Link(3, Link(1, Link(2)))
    >>> link = rotate(link, 2)
    >>> link
    Link(1, Link(2, Link(3)))
    >>> rotate(link, 5)
    Link(2, Link(3, Link(1)))
    >>> link = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> rotate(link, 4)
    Link(3, Link(4, Link(5, Link(6, Link(1, Link(2))))))
    """
    "*** YOUR CODE HERE ***"



