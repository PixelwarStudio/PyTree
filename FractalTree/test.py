from math import radians
from PIL import Image, ImageDraw
from FractalTree import PolyTree

im = Image.new('RGBA', (700, 700)) 
draw = ImageDraw.Draw(im)

bin_tree = PolyTree(350, 700, 200, 0.9, 1, radians(0), radians(90))

def draw_node(n):
    draw.point((n.x, n.y))

def draw_branch(b):
    draw.line((b.start_node.x, b.start_node.y, b.end_node.x, b.end_node.y))

def draw_tree(t):
    for age in t.branches:
        for branch in age:
            draw_branch(branch)

for i in range(20):
    bin_tree.grow()

draw_tree(bin_tree)
im.show()
