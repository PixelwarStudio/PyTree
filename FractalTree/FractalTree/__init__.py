"""
Module for creating fractal trees
"""
from math import cos, sin, sqrt, atan2, pi, log

class Node:
    """A Node"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_new_node(self, length, angle):
        """Make a new one from an existing one"""
        return Node(cos(-angle)*length+self.x,
                    sin(-angle)*length+self.y)

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
        return pi - atan2(self.get_dy(), self.get_dx())

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
    """A tree with multiple branches created per grow step"""
    def __init__(self, x, y, length, scale, complexity, branch_angle, shift_angle):
        Tree.__init__(self, x, y, length, scale)
        self.comp = complexity
        self.branch_angle = branch_angle
        self.shift_angle = shift_angle

    def get_branch_length(self, age=None):
        """Get the length of a branch"""
        if age is None:
            age = self.age

        return self.length * pow(self.scale, age)

    def get_branch_number(self, age=None):
        """Get sum of all branches in the tree"""
        if age is None:
            age = self.age

        if self.comp == 1:
            return age
        else:
            return (pow(self.comp, age+1) - 1) / (self.comp - 1)

    def get_branch_age_number(self, age=None):
        """Get the sum of branches grown in an specific age"""
        if age is None:
            age = self.age

        return pow(self.comp, age)

    def get_steps_branch_len(self, length):
        """Get, how much steps will needed for a given branch length"""
        return log(length/self.length, self.scale)

    def get_total_angle(self, branch, child_i):
        """Get the total angle"""
        return (branch.get_angle()
                + self.branch_angle * ((self.comp-1)/2-child_i)
                - self.shift_angle)

    def grow(self):
        """Let the tree grow"""
        self.branches.append([])
        self.nodes.append([])

        for parent_branch in self.branches[self.age]:
            parent_node = parent_branch.end_node
            for child_i in range(self.comp):
                new_node = parent_node.make_new_node(self.get_branch_length(self.age+1),
                                                     self.get_total_angle(parent_branch, child_i))
                self.nodes[self.age+1].append(new_node)
                self.branches[self.age+1].append(Branch(parent_node, new_node))

        Tree.grow(self)
