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
        if (node not in self._children):
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self.children:
            self._children.remove(node)
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if len(self._children) and self._parent != None:
            print('here')
            self._parent.remove_child(self)

        self._parent = node

        if (node and self not in node.children):
            node.add_child(self)


node1 = Node('root1')
node2 = Node('root2')
node3 = Node('root3')

node3.parent = node1
node1.remove_child(node3)

print('_______________________________________')

