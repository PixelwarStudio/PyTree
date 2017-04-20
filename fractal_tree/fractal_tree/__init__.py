"""
Module for creating fractal trees
"""
from math import cos, sin, acos, sqrt

class Node:
    """A Node"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_new_node(self, length, angle):
        """Make a new one from an existing one"""
        return Node(cos(-angle)*length+self.x,
                    sin(-angle)*length+self.y)

    def copy(self):
        """Copy a Node"""
        return Node(self.x, self.y)

    def move(self, dx, dy):
        """Move the node"""
        self.x += dx
        self.y += dy

class Branch:
    """A Branch"""
    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node

    def get_dx(self):
        """Get the distance beetween the x-coordinates"""
        return self.start_node.x - self.end_node.x

    def get_dy(self):
        """Get the distance beetween the y-coordinates"""
        return self.start_node.y - self.end_node.y

    def get_length(self):
        """Get the length of the branch"""
        return sqrt(self.get_dx()**2 + self.get_dy()**2)

    def get_angle(self):
        """Get angle beetween the branch and the horizont"""
        #TODO: Fix THIS!
        return acos(self.get_dx() / self.get_length())

class Tree:
    """The standard tree"""
    def __init__(self, x, y, length, scale):
        self.x = x
        self.y = y
        self.length = length
        self.scale = scale

        self.age = 0
        self.nodes = [
            [Node(x, y - length)]
        ]
        self.branches = [
            [Branch(Node(x, y), Node(x, y - length))]
        ]

    def grow(self):
        """Let the tree grow"""
        self.age += 1

class PolyTree(Tree):
    def __init__(self, x, y, length, scale, complexity, branch_angle):
        Tree.__init__(self, x, y, length, scale)
        self.comp = complexity
        self.branch_angle = branch_angle

    def get_branch_length(self, age=None):
        if age is None:
            age = self.age

        return self.length * pow(self.scale, age)

    def get_branch_number(self, age=None):
        if age is None:
            age = self.age

        return (pow(self.comp, age+1) - 1) / (age - 1)

    def get_branch_age_number(self, age=None):
        if age is None:
            age = self.age

        return pow(self.comp, age)

    def get_total_angle(self, branch):
        return branch.get_angle() + self.branch_angle

    def grow(self):
        self.branches.append([])
        self.nodes.append([])

        for branch in self.branches[self.age]:
            node = branch.end_node
            for n in range(self.comp):
                #TODO: Define a angle method
                new_node = node.make_new_node(self.get_branch_length(self.age+1),
                                              branch.get_angle()
                                              + self.branch_angle-n*self.branch_angle*2)
                self.nodes[self.age+1].append(new_node)
                self.branches[self.age+1].append(Branch(node, new_node))

        self.age += 1

class BinaryTree(PolyTree):
    def __init__(self, x, y, length, scale, branch_angle, shift_angle):
        PolyTree.__init__(self, x, y, length, scale, 2, branch_angle)
        self.shift_angle = shift_angle
        