"""
Example: Svg generation
"""
from math import radians
from svgwrite import Drawing
from Tree.core import Tree
from Tree.draw import SvgDrawer

if __name__ == "__main__":
    tree = Tree(
        pos=(0, 0, 0, -300),
        complexity=3,
        angle=(radians(25), 0),
        sigma=(0.1, 0.2)
    )

    tree.grow(10)

    # Move the tree in the right position
    rec = tree.get_rectangle()
    tree.move((-rec[0], -rec[1]))

    # Create, draw and show the image/tree
    svg = Drawing(filename="mycoolsvg.svg", size=tree.get_size())
    SvgDrawer(tree, svg, color=(123, 60, 4)+(30, 78, 90), thickness=10).draw()
    svg.save()