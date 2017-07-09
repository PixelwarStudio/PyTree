"""
Example: Sierpinski tree
"""
from math import radians
from PIL import Image
from Tree.core import Tree
from Tree.draw import PillowDrawer

if __name__ == "__main__":
    tree = Tree(pos=(0, 0, 0, -500), complexity=3, angle=(radians(120), 0))

    # Calculate how much steps are needed to reach a branch len of 1
    steps = tree.get_steps_branch_len(1)

    tree.grow(steps)

    # Move the tree in the right position
    tree.move_in_rectangle()

    # Create, draw and show the image/tree
    im = Image.new("RGB", tree.get_size())
    PillowDrawer(tree, im).draw()
    im.show()
    