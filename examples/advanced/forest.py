"""
Example: Forest
"""
from math import radians
from random import randint
from PIL import Image
from Tree.core import Tree
from Tree.draw import Drawer

im = Image.new("RGB", (700, 350))

for y in range(180, 330, 15):
    dx = 0
    if (y / 15) % 2 == 0:
        dx = 50
    for x in range(100+dx, 600+dx, 50):
        # Vary the length of the tree
        length = randint(35, 65)
        # Vary the color of the tree
        r, g, b = randint(200, 250), randint(100, 200), randint(100, 200)
        tree = Tree((x, y, x, y - length), 0.6, 3, (radians(25), 0), (0.1, 15/180))
        for n in range(8):
            tree.grow()
        Drawer(tree, im, color=(119, 83, 21)+(r, g, b)).draw()
im.show()