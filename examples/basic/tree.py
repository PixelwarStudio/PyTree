"""
Example: Tree
"""
from math import radians
from PIL import Image
from Tree.core import Tree
from Tree.draw import PillowDrawer

if __name__ == "__main__":
    tree = Tree(pos=(0, 0, 0, -400), complexity=3, angle=(radians(25), 0), sigma=(0.1, 0.1))

    # Calculate how much steps are needed to reach a branch len of 1
    # NOTE: In this case it is just a approximation!
    steps = tree.get_steps_branch_len(1)

    tree.grow(steps)

    # Move the tree in the right position
    rec = tree.get_rectangle()
    tree.move((-rec[0], -rec[1]))

    # Create, draw and show the image/tree
    im = Image.new("RGB", tree.get_size())
    PillowDrawer(tree, im).draw()
    im.show()
    