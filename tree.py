class Node:
    def __init__(self, value, parent = None, children = []):
        self._value = value
        self._parent = parent
        self._children = children

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        self._children.append(node)
        if (not node in self._children):
            node.parent = self

    def remove_child(self, node):
        self._children.remove(node)
        node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node
        node.add_child(self)
