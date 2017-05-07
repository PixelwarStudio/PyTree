from PIL import Image, ImageDraw

class Drawer(object):
    """This drawer draws tree to an PIL/Pillow image"""
    def __init__(self, tree, im, color=(255, 255, 255), thickness=1):
        self.im = im
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

    def draw_branch(self, branch, color, thickness):
        """Draws a branch using PIL

        Args:
            branch (tuple): (x1, y1, x2, y2)
            color (tuple): (r, g, b)
            thickness (int): The thickness of the branch.
        """
        ImageDraw.Draw(self.im).line(branch, color, thickness)

    def draw(self):
        """Draws the tree."""
        for a, age in enumerate(self.tree.get_branches()):
            thickness = self.get_thickness(a)
            color = self.get_color(a)
            for branch in age:
                self.draw_branch(branch, color, thickness)
