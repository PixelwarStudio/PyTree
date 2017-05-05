"""
Module for creating fractal trees
"""
from math import cos, sin, sqrt, atan2, pi, log

class Node:
    """A Node"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_new_node(self, distance, angle):
        """Make a new one from an existing one.

        Args:
            distance (float): The distance of the original node to the new node.
            angle (radians): The angle between the old and new node, relative to the horizont.

        Returns:
            Node: Returns the new node.
        """
        return Node(cos(-angle)*distance+self.x,
                    sin(-angle)*distance+self.y)

    def get_tuple(self):
        """Get the position of the node as tuple.

        Returns:
            Tupel: Contains x- and y-coordinate
        """
        return (self.x, self.y)

    def move(self, dx, dy):
        """Move the node.

        Args:
            dx (float): Delta (Adjustment) of the x-pos.
            dy (float): Delta (Adjustment) of the y-pos.
        """
        self.x += dx
        self.y += dy

class Tree:
    """The standard tree"""
    def __init__(self, x, y, length, scale, complexity, branch_angle, shift_angle):
        self.x = x
        self.y = y
        self.length = length
        self.scale = scale
        self.comp = complexity
        self.branch_angle = branch_angle
        self.shift_angle = shift_angle

        self.age = 0

        self.nodes = [
            [Node(x, y - length)]
        ]

    def get_rectangle(self):
        """Get the coordinates of the rectangle, in which the tree can be putted"""
        min_x = self.x
        max_x = self.x
        min_y = self.y
        max_y = self.y
        for age in self.nodes:
            for node in age:
                if min_x > node.x:
                    min_x = node.x
                if max_x < node.x:
                    max_x = node.x
                if min_y > node.y:
                    min_y = node.y
                if max_y < node.y:
                    max_y = node.y
        return (min_x, min_y, max_x, max_y)

    def get_branch_length(self, age=None):
        """Get the length of a branch"""
        if age is None:
            age = self.age

        return self.length * pow(self.scale, age)
    
    def get_steps_branch_len(self, length):
        """Get, how much steps will needed for a given branch length"""
        return log(length/self.length, self.scale)

    def get_node_number(self, age=None):
        """Get sum of all branches in the tree"""
        if age is None:
            age = self.age

        if self.comp == 1:
            return age
        else:
            return int((pow(self.comp, age+1) - 1) / (self.comp - 1))

    def get_node_age_number(self, age=None):
        """Get the sum of branches grown in an specific age"""
        if age is None:
            age = self.age

        return pow(self.comp, age)

    def get_nodes(self):
        nodes = []
        for age, level in enumerate(self.nodes):
            nodes.append([])
            for node in level:
                nodes[age].append(node.get_tuple())
        return nodes

    def get_branches(self):
        branches = []
        for age, level in enumerate(self.nodes):
            branches.append([])
            for n, node in enumerate(level):
                if age == 0:
                    p_node = Node(self.x, self.y)
                else:
                    p_node = self.nodes[age-1][int(n / self.comp)]
                branches[age].append(p_node.get_tuple() + node.get_tuple())

        return branches

    def move(self, dx, dy):
        """Move the tree"""
        # Move the tree start position
        self.x += dx
        self.y += dy

        # Move all nodes
        for age in self.nodes:
            for node in age:
                node.move(dx, dy)

    def grow(self):
        """Let the tree grow"""
        self.nodes.append([])

        for n, node in enumerate(self.nodes[self.age]):
            node = self.nodes[self.age][n]
            if self.age == 0:
                p_node = Node(self.x, self.y)
            else:
                p_node = self.nodes[self.age-1][int(n / self.comp)]
            angle = atan2(node.x-p_node.x, node.y-p_node.y) - pi / 2
            for i in range(self.comp):
                pos = (self.comp-1)/2 - i
                tot_angle = angle + self.branch_angle * pos - self.shift_angle
                self.nodes[self.age+1].append(
                    node.make_new_node(self.get_branch_length(self.age+1), tot_angle)
                )

        self.age += 1

class SymetricTree(Tree):
    """A symetric Tree"""
    def __init__(self, x, y, length, scale, complexity, branch_angle):
        Tree.__init__(x, y, length, scale, complexity, branch_angle, 0)

class BinaryTree(Tree):
    """A binary Tree"""
    def __init__(self, x, y, length, scale, branch_angle, shift_angle):
        Tree.__init__(x, y, length, scale, 2, branch_angle, shift_angle)

class TernaryTree(Tree):
    """A ternary Tree"""
    def __init__(self, x, y, length, scale, branch_angle, shift_angle):
        Tree.__init__(x, y, length, scale, 3, branch_angle, shift_angle)

class DragonTree(Tree):
    """"A Dragontree"""
    def __init__(self, x, y, length, scale, shift_angle):
        Tree.__init__(x, y, length, scale, 2, pi/2, shift_angle)
