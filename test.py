from math import radians
from PIL import Image, ImageDraw
from FractalTree import PolyTree

im = Image.new('RGBA', (700, 700)) 
draw = ImageDraw.Draw(im)

bin_tree = PolyTree(350, 500, 100, 0.5, 2, radians(90), radians(0))

def draw_node(n):
    draw.point((n.x, n.y))

def draw_branch(b):
    draw.line((b.start_node.x, b.start_node.y, b.end_node.x, b.end_node.y))

def draw_nodes(t):
    for age in t.nodes:
        for node in age:
            draw_node(node)

def draw_branches(t):
    for age in t.branches:
        for branch in age:
            draw_branch(branch)

def draw_tree(t):
    draw_branches(t)
    draw_nodes(t)

for i in range(5):
    bin_tree.grow()

draw_tree(bin_tree)
box = bin_tree.get_box()
draw.rectangle(box)
im.show()
