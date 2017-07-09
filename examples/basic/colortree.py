"""
Example: Color tree
"""
from math import radians
from PIL import Image
from Tree.core import Tree
from Tree.draw import PillowDrawer

if __name__ == "__main__":
    tree = Tree(pos=(0, 0, 0, -250), complexity=3, scale=0.7, angle=(radians(20), 0), sigma=(0.2, 0.1))

    tree.grow(10)

    # Move the tree in the right position
    tree.move_in_rectangle()

    # Create, draw and show the image/tree
    im = Image.new("RGB", tree.get_size())
    # Set the color of the tree
    gradient = (96, 65, 6)+(9, 158, 19)
    PillowDrawer(tree, im, color=gradient, thickness=10).draw()
    im.show()
    