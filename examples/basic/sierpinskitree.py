"""
Example: Sierpinski tree
"""
from math import radians
from PIL import Image
from Tree.core import Tree
from Tree.draw import Drawer

if __name__ == "__main__":
    sier_tree = Tree(pos=(0, 0, 0, -500), complexity=3, angle=(radians(120), 0))

    # Calculate how much steps are needed to reach a branch len of 1
    steps = sier_tree.get_steps_branch_len(1)

    sier_tree.grow(steps)

    # Move the tree in the right position
    rec = sier_tree.get_rectangle()
    sier_tree.move((-rec[0], -rec[1]))

    # Create, draw and show the image/tree
    im = Image.new("RGB", sier_tree.get_size())
    Drawer(sier_tree, im).draw()
    im.show()
    