"""
Example: Binary tree
"""
from math import radians
from PIL import Image
from Tree.core import Tree
from Tree.draw import PillowDrawer

if __name__ == "__main__":
    # Just modify angle[0] or scale to generate other binarytrees
    bin_tree = Tree(pos=(0, 0, 0, -400), angle=(radians(45), 0))

    # Calculate how much steps are needed to reach a branch len of 1
    steps = bin_tree.get_steps_branch_len(1)

    bin_tree.grow(steps)

    # Move the tree in the right position
    bin_tree.move_in_rectangle()

    # Create, draw and show the image/tree
    im = Image.new("RGB", bin_tree.get_size())
    PillowDrawer(bin_tree, im).draw()
    im.show()
