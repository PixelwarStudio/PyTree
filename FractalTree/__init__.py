"""
Module for creating fractal trees
"""
from math import cos, sin, sqrt, atan2, pi, log

class Node(object):
    """A node.

    Attributes:
        x (float): The x-position of the node.
        y (float): The y-position of the node.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
            object: Returns the new node as object.
            Example:
            Node(403.125, 129.601)
        """
        return Node(cos(-angle)*distance+self.x,
                    sin(-angle)*distance+self.y)

    def get_tuple(self):
        """Get the position of the node as tuple.

        Returns:
            tupel: A tupel with the x/y-position. The first element is the x-position
            and the second element is the y-position.
            Example:
            (100.1, 30.0)
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
        """Get the coordinates of the rectangle, in which the tree can be put.

        #TODO: Add extended description.

        Returns:
            tupel: Contains x1, y1, x2, y2 of the rectangle.
            Example:
            (100.1, 200.3, 400.2, 300.34)
        """
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
        
        #TODO: Add more info.

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
                    p_node = Node(self.x, self.y)
                else:
                    p_node = self._get_node_parent(age-1, n)
                branches[age].append(p_node.get_tuple() + node.get_tuple())

        return branches

    def move(self, dx, dy):
        """Move the tree

        Args:
            dx (float): Delta (Adjustment) of the x-pos.
            dy (float): Delta (Adjustment) of the y-pos.
        """
        # Move the tree start position
        self.x += dx
        self.y += dy

        # Move all nodes
        for age in self.nodes:
            for node in age:
                node.move(dx, dy)

    def grow(self):
        """Let the tree grow

        #TODO: Describe the grow process."""
        self.nodes.append([])

        for n, node in enumerate(self.nodes[self.age]):
            node = self.nodes[self.age][n]
            if self.age == 0:
                p_node = Node(self.x, self.y)
            else:
                p_node = self._get_node_parent(self.age-1, n)
            angle = self._get_node_angle(node, p_node)
            for i in range(self.comp):
                pos = (self.comp-1) / 2 - i
                tot_angle = angle + self.branch_angle * pos - self.shift_angle
                self.nodes[self.age+1].append(
                    node.make_new_node(self.get_branch_length(self.age+1), tot_angle)
                )

        self.age += 1

    def _get_node_parent(self, age, pos):
        return self.nodes[age][int(pos / self.comp)]

    def _get_node_angle(self, node1, node2):
        return atan2(node1.x-node2.x, node1.y-node2.y) - pi / 2

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
