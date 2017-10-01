"""
Module for drawing trees.
"""
from PIL import ImageDraw
import svgwrite
from Tree.utils import convert_color

class Drawer(object):
    """A generic class for drawing tree on acanvas.

    Attributes:
        canvas: The canvas for drawing the tree.
        tree (object): The tree, which should drawn on canvas.
        color (tupel): Color or gradient for coloring the tree.
        thickness (int): The start thickness of the tree.
    """
    def __init__(self, tree, canvas, color=(255, 255, 255), thickness=1):
        self.canvas = canvas
        self.tree = tree
        self.color = color
        self.thickness = thickness

    def _get_thickness(self, age):
        """Get the thickness depending on age.

        Args:
            age (int): The age of the branch/es

        Returns:
            int: The thickness of the branch/es
        """
        return int((self.thickness*5)/(age+5))

    def _get_color(self, age):
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

        diff = [color[i+3]-color[i] for i in range(3)]
        per_age = [diff[i]/tree.age for i in range(3)]

        return tuple([int(color[i]+per_age[i]*age) for i in range(3)])

    def _draw_branch(self, branch, color, thickness, age):
        """Placeholder for specific draw methods for a branch.

        Args:
            branch (tupel): The coordinates of the branch.
            color (tupel): The color of the branch.
            thickness (int): The thickness of the branch.
            age (int): The age of the tree the branch is drawn.
        """
        pass

    def draw(self):
        """Draws the tree."""
        for age, level in enumerate(self.tree.get_branches()):
            thickness = self._get_thickness(age)
            color = self._get_color(age)
            for branch in level:
                self._draw_branch(branch, color, thickness, age)

class PilDrawer(Drawer):
    """A drawer class for drawing on PIL/Pillow images."""
    def _draw_branch(self, branch, color, thickness, age):
        ImageDraw.Draw(self.canvas).line(branch, color, thickness)

class SvgDrawer(Drawer):
    """A drawer class for drawing on svg documents.

    Attributes:
        group (list): Saves the groups created for every age.
    """
    def __init__(self, tree, canvas, color=(255, 255, 255), thickness=1):
        super(SvgDrawer, self).__init__(tree, canvas, color, thickness)
        self.group = []

    def _draw_branch(self, branch, color, thickness, age):
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
        for _ in range(self.tree.age+1):
            self.group.append(self.canvas.add(svgwrite.container.Group()))
        Drawer.draw(self)

SUPPORTED_CANVAS = {
    "PIL.Image": PilDrawer,
    "svgwrite.Drawing": SvgDrawer
}