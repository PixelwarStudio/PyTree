"""
Module for creating trees
"""
from math import pi, log, sqrt
from random import gauss
from Tree.utils import Node

class Tree:
    """The standard tree.

    Attributes:
        length (float): The start length.
        age (int): A counter increasing every time grow() is called by 1.
        nodes (list): A 2d-list holding the grown nodes for every age.
    """
    def __init__(self, pos=(0, 0, 0, -100), scale=0.5, complexity=2, angle=(pi, 0), sigma=(0, 0)):
        """The contructor.

        Args:
            pos (tupel): A tupel, holding the start and end point of the tree. (x1, y1, x2, y2)
            scale (float): Indicating how the branch length develops from age to age.
            complexity (int): Indicating how many new branches/nodes sprout from an older node.
            angle (tuple): Holding the branch and shift angle in radians. e.g.(pi, p1/2)
            sigma (tuple): Holding the branch and angle sigma. e.g.(0.1, 0.2)
        """
        self.pos = pos
        self.length = sqrt((pos[2]-pos[0])**2+(pos[3]-pos[1])**2)
        self.scale = scale
        self.comp = complexity
        self.angle = angle
        self.sigma = sigma

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

        return age if self.comp == 1 else int((pow(self.comp, age+1) - 1) / (self.comp - 1))

    def get_node_age_sum(self, age=None):
        """Get the sum of branches grown in an specific age.

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
                    p_node = self._get_node_parent(age-1, n)
                branches[age].append(p_node.get_tuple() + node.get_tuple())

        return branches

    def move(self, delta):
        """Move the tree.

        Args:
            delta (tupel): The adjustment of the position.
        """
        pos = self.pos
        self.pos = (pos[0]+delta[0], pos[1]+delta[1], pos[2]+delta[0], pos[3]+delta[1])

        # Move all nodes
        for age in self.nodes:
            for node in age:
                node.move(delta)
    
    def move_in_rectangle(self):
        """Move the tree so that the tree fits in the rectangle."""
        rec = self.get_rectangle()
        self.move((-rec[0], -rec[1]))

    def grow(self, times=1):
        """Let the tree grow.

        Args:
            times (integer): Indicate how many times the tree will grow.
        """
        self.nodes.append([])

        for n, node in enumerate(self.nodes[self.age]):
            if self.age == 0:
                p_node = Node(self.pos[:2])
            else:
                p_node = self._get_node_parent(self.age-1, n)
            angle = node.get_node_angle(p_node)
            for i in range(self.comp):
                pos = (self.comp-1) / 2 - i
                tot_angle = self.__get_total_angle(angle, pos)
                length = self.__get_total_length(self.age+1)
                self.nodes[self.age+1].append(node.make_new_node(length, tot_angle))

        self.age += 1

        if times > 1:
            self.grow(times-1)


    def __get_total_angle(self, angle, pos):
        """Get the total angle."""
        tot_angle = angle + self.angle[0] * pos - self.angle[1]
        if self.sigma[1] != 0:
            tot_angle += gauss(0, self.sigma[1]) * pi
        return tot_angle

    def __get_total_length(self, age):
        length = self.get_branch_length(age)
        if self.sigma[0] != 0:
            length *= (1+gauss(0, self.sigma[0]))
        return length

    def _get_node_parent(self, age, pos):
        """Get the parent node of node, whch is located in tree's node list.

        Returns:
            object: The parent node.
        """
        return self.nodes[age][int(pos / self.comp)]
