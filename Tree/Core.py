"""
Module for creating trees
"""
from math import cos, sin, atan2, pi, log, sqrt
from random import gauss

class Node(object):
    """A node.

    Attributes:
        x (float): The x-position of the node.
        y (float): The y-position of the node.
    """
    def __init__(self, pos):
        self.pos = pos

    def make_new_node(self, distance, angle):
        """Make a new node from an existing one.

        This method creates a new node with a distance and angle given.
        The position of the new node is calculated with:
        x2 = cos(-angle)*distance+x1
        y2 = sin(-angle)*distance+y1

        Args:
            distance (float): The distance of the original node to the new node.
            angle (rad): The angle between the old and new node, relative to the horizont.

        Returns:
            object: Node(x, y)
        """
        return Node((cos(-angle)*distance+self.pos[0],
                    sin(-angle)*distance+self.pos[1]))

    def get_node_angle(self, node):
        """Get the angle beetween 2 nodes relative to the horizont

        Returns:
            rad: The angle
        """
        return atan2(self.pos[0]-node.pos[0], self.pos[1]-node.pos[1]) - pi / 2

    def get_tuple(self):
        """Get the position of the node as tuple.

        Returns:
            tupel: (x, y)
        """
        return self.pos

    def move(self, delta):
        """Move the node.

        Args:
            dx (float): Delta (Adjustment) of the x-pos.
            dy (float): Delta (Adjustment) of the y-pos.
        """
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])

class FractalTree:
    """The standard tree.

    Attributes:
        x (float): The x-position.
        y (float): The y-position.
        length (float): The start length.
        scale (float): A float indicating how the branch length develops from age to age.
        comp (int): An integer indicating how many new branches/nodes sprout from an older node.
        branch_angle (rad): A angle beetween two angles.
        shift_angle (rad): A float/radian angle indicating how much the angle is shifted.
        age (int): A counter increasing every time grow() is called by 1.
        nodes (list): A 2d-list holding the grown nodes for every age.
            Example:
            [
            [node1],
            [node2, node3],
            [node4, node5, ... ],
            [...]
            ]
    """
    def __init__(self, pos=(0, 0, 0, 100), scale=0.5, complexity=2, branch_angle=pi, shift_angle=0):
        self.pos = pos
        self.length = sqrt((pos[2]-pos[0])**2+(pos[3]-pos[1])**2)
        self.scale = scale
        self.comp = complexity
        self.branch_angle = branch_angle
        self.shift_angle = shift_angle

        self.age = 0

        self.nodes = [
            [Node(pos[2:])]
        ]

    def get_rectangle(self):
        """Get the coordinates of the rectangle, in which the tree can be put.

        Returns:
            tupel: (x1, y1, x2, y2)
        """
        min_x = self.pos[0]
        max_x = self.pos[0]
        min_y = self.pos[1]
        max_y = self.pos[1]
        for age in self.nodes:
            for node in age:
                if min_x > node.pos[0]:
                    min_x = node.pos[0]
                if max_x < node.pos[0]:
                    max_x = node.pos[0]
                if min_y > node.pos[1]:
                    min_y = node.pos[1]
                if max_y < node.pos[1]:
                    max_y = node.pos[1]
        return (min_x, min_y, max_x, max_y)

    def get_size(self):
        """Get the size of the tree.

        Returns:
            tupel: (width, height)
        """
        rec = self.get_rectangle()
        return (int(rec[2]-rec[0]), int(rec[3]-rec[1]))

    def get_branch_length(self, age=None):
        """Get the length of a branch.

        This method calculates the length of a branch in specific age.
        The used formula: length * scale^age.

        Args:
            age (int): The age, for which you want to know the branch length.
        Returns:
            float: The length of the branch
        """
        if age is None:
            age = self.age

        return self.length * pow(self.scale, age)

    def get_steps_branch_len(self, length):
        """Get, how much steps will needed for a given branch length.

        Returns:
            float: The age the tree must achieve to reach the given branch length.
        """
        return log(length/self.length, self.scale)

    def get_node_sum(self, age=None):
        """Get sum of all branches in the tree.

        Returns:
            int: The sum of all nodes grown until the age.
        """
        if age is None:
            age = self.age

        if self.comp == 1:
            return age
        else:
            return int((pow(self.comp, age+1) - 1) / (self.comp - 1))

    def get_node_age_sum(self, age=None):
        """Get the sum of branches grown in an specific age

        Returns:
            int: The sum of all nodes grown in an age.
        """
        if age is None:
            age = self.age

        return pow(self.comp, age)

    def get_nodes(self):
        """Get the tree nodes as list.

        Returns:
            list: A 2d-list holding the grown nodes coordinates as tupel for every age.
                Example:
                [
                [(10, 40)],
                [(20, 80), (100, 30)],
                [(100, 90), (120, 40), ...],
                ...
                ]
        """
        nodes = []
        for age, level in enumerate(self.nodes):
            nodes.append([])
            for node in level:
                nodes[age].append(node.get_tuple())
        return nodes

    def get_branches(self):
        """Get the tree branches as list.

        Returns:
            list: A 2d-list holding the grown branches coordinates as tupel for every age.
                Example:
                [
                [(10, 40, 90, 30)],
                [(90, 30, 100, 40), (90, 30, 300, 60)],
                [(100, 40, 120, 70), (100, 40, 150, 90), ...],
                ...
                ]
        """
        branches = []
        for age, level in enumerate(self.nodes):
            branches.append([])
            for n, node in enumerate(level):
                if age == 0:
                    p_node = Node(self.pos[:2])
                else:
                    p_node = self.get_node_parent(age-1, n)
                branches[age].append(p_node.get_tuple() + node.get_tuple())

        return branches

    def move(self, delta):
        """Move the tree

        Args:
            delta (tupel):
        """
        pos = self.pos
        self.pos = (pos[0]+delta[0], pos[1]+delta[1], pos[2]+delta[0], pos[3]+delta[1])

        # Move all nodes
        for age in self.nodes:
            for node in age:
                node.move(delta)

    def grow(self):
        """Let the tree grow."""
        self.nodes.append([])

        for n, node in enumerate(self.nodes[self.age]):
            if self.age == 0:
                p_node = Node(self.pos[:2])
            else:
                p_node = self.get_node_parent(self.age-1, n)
            angle = node.get_node_angle(p_node)
            for i in range(self.comp):
                pos = (self.comp-1) / 2 - i
                tot_angle = self.get_total_angle(angle, pos)
                length = self.get_branch_length(self.age+1)
                self.nodes[self.age+1].append(node.make_new_node(length, tot_angle))

        self.age += 1

    def get_total_angle(self, angle, pos):
        """Get the total angle."""
        return angle + self.branch_angle * pos - self.shift_angle

    def get_node_parent(self, age, pos):
        """Get the parent node of node, whch is located in tree's node list.

        Returns:
            object: The parent node.
        """
        return self.nodes[age][int(pos / self.comp)]

class RealTree(FractalTree):
    """A realistic Tree based on fractal trees with a little (or more) bit randomness."""
    def __init__(self, pos=(0, 0, 0, 100), scale=0.5, complexity=2, branch_angle=pi, shift_angle=0, branch_sigma=0, angle_sigma=0):
        FractalTree.__init__(self, pos, scale, complexity, branch_angle, shift_angle)
        self.branch_sigma = branch_sigma
        self.angle_sigma = angle_sigma

    def get_branch_length(self, age):
        return FractalTree.get_branch_length(self, age) * (1 + gauss(0, self.branch_sigma))

    def get_total_angle(self, angle, pos):
        return FractalTree.get_total_angle(self, angle, pos) + gauss(0, self.angle_sigma)

class SymetricTree(FractalTree):
    """A symetric Tree"""
    def __init__(self, x, y, length, scale, complexity, branch_angle):
        FractalTree.__init__(x, y, length, scale, complexity, branch_angle, 0)

class BinaryTree(FractalTree):
    """A binary Tree"""
    def __init__(self, x, y, length, scale, branch_angle, shift_angle):
        FractalTree.__init__(x, y, length, scale, 2, branch_angle, shift_angle)

class TernaryTree(FractalTree):
    """A ternary Tree"""
    def __init__(self, x, y, length, scale, branch_angle, shift_angle):
        FractalTree.__init__(x, y, length, scale, 3, branch_angle, shift_angle)

class DragonTree(FractalTree):
    """"A Dragontree"""
    def __init__(self, x, y, length, scale, shift_angle):
        FractalTree.__init__(x, y, length, scale, 2, pi/2, shift_angle)
