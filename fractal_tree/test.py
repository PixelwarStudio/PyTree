import math
from PIL import Image, ImageDraw
from fractal_tree import Tree, BinaryTree, Node, Branch

im = Image.new('RGBA', (400, 400)) 
draw = ImageDraw.Draw(im)

bin_tree = BinaryTree(200, 400, 150, 0.5, math.radians(90), 0)

def draw_branch(b):
    draw.line((b.start_node.x, b.start_node.y, b.end_node.x, b.end_node.y))

def draw_tree(t):
    for age in t.branches:
        for branch in age:
            draw_branch(branch)

for i in range(10):
    bin_tree.grow()

draw_tree(bin_tree)
im.show()
