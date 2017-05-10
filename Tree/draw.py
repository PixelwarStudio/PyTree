"""
Module for drawing trees.
"""
from PIL import ImageDraw
import svgwrite
from Tree.utils import convert_color

class Drawer(object):
    """This drawer draws tree to an PIL/Pillow image."""
    def __init__(self, tree, canvas, color=(255, 255, 255), thickness=1):
        self.canvas = canvas
        self.tree = tree
        self.color = color
        self.thickness = thickness

    def get_thickness(self, age):
        """Get the thickness depending on age.

        Args:
            age (int): The age of the branch/es

        Returns:
            int: The thickness of the branch/es
        """
        return int((self.thickness*5)/(age+5))

    def get_color(self, age):
        """Get the fill color depending on age.

        Args:
            age (int): The age of the branch/es

        Returns:
            tuple: (r, g, b)
        """
        color = self.color
        tree = self.tree
        if len(color) == 3:
            return color
        else:
            diff = (color[3]-color[0], color[4]-color[1], color[5]-color[2])
            per_age = (diff[0]/tree.age, diff[1]/tree.age, diff[2]/tree.age)
            return (int(color[0]+per_age[0]*age),
                    int(color[1]+per_age[1]*age),
                    int(color[2]+per_age[2]*age))

    def draw_branch(self, branch, color, thickness, age=None):
        pass

    def draw(self):
        """Draws the tree."""
        for age, level in enumerate(self.tree.get_branches()):
            thickness = self.get_thickness(age)
            color = self.get_color(age)
            for branch in level:
                self.draw_branch(branch, color, thickness, age)

class PillowDrawer(Drawer):
    def draw_branch(self, branch, color, thickness, age=None):
        ImageDraw.Draw(self.canvas).line(branch, color, thickness)

class SvgDrawer(Drawer):
    def draw_branch(self, branch, color, thickness, age):
        color = convert_color(color)
        self.group[age].add(
            self.canvas.line(
                start=branch[:2],
                end=branch[2:],
                stroke=color,
                stroke_width=thickness
            )
        )

    def draw(self):
        self.group = []
        for age in range(self.tree.age+1):
            self.group.append(self.canvas.add(svgwrite.container.Group()))
        Drawer.draw(self)

