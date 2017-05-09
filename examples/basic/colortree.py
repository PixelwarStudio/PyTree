"""
Example: Color tree
"""
from math import radians
from PIL import Image
from Tree.core import Tree
from Tree.draw import Drawer

if __name__ == "__main__":
    sier_tree = Tree(pos=(0, 0, 0, -300), complexity=3, scale=0.7, angle=(radians(20), 0), sigma=(0.2, 0.1))

    sier_tree.grow(10)

    # Move the tree in the right position
    rec = sier_tree.get_rectangle()
    sier_tree.move((-rec[0], -rec[1]))

    # Create, draw and show the image/tree
    im = Image.new("RGB", sier_tree.get_size())
    # Set the color of the tree
    gradient = (96, 65, 6)+(9, 158, 19)
    Drawer(sier_tree, im, color=gradient, thickness=10).draw()
    im.show()
    