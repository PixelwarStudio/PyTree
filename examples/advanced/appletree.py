from math import radians
from random import random
from PIL import Image, ImageDraw
from Tree.Core import RealTree
from Tree.Draw import Drawer

class AppleTree(RealTree):
    MIN_AGE = 8
    RATE = 1/5000
    def get_apples(self):
        apples = []
        for a, age in enumerate(self.nodes):
            apples.append([])
            if a >= AppleTree.MIN_AGE:
                for node in age:
                    if AppleTree.RATE >= random():
                        apples[a].append(node.get_tuple())
        return apples


class AppleTreeDrawer(Drawer):
    def __init__(self, tree, im, color=(255, 255, 255), thickness=1, apple_color=(255, 0, 0), apple_width=4):
        Drawer.__init__(self, tree, im, color, thickness)
        self.apple_color = apple_color
        self.apple_width = apple_width

    def draw_apple(self, apple):
        width, color = self.apple_width, self.apple_color
        ImageDraw.Draw(self.im).ellipse(
            (apple[0]-width, apple[1]-width+5, apple[0]+width, apple[1]+width+5),
            fill=color)

    def draw(self):
        apples = self.tree.get_apples()
        for a, age in enumerate(self.tree.get_branches()):
            thickness = self.get_thickness(a)
            color = self.get_color(a)
            for branch in age:
                self.draw_branch(branch, color, thickness)
            for apple in apples[a]:
                self.draw_apple(apple)

if __name__ == "__main__":
    appletree = AppleTree((0, 0, 0, -200), 0.65, 3, radians(40), radians(0), 0.2, radians(10))

    for n in range(10):
        appletree.grow()

    rec = appletree.get_rectangle()
    appletree.move((-rec[0], -rec[1]))

    im = Image.new("RGB", appletree.get_size(), color=(231, 231, 231))

    AppleTreeDrawer(appletree, im, (127, 73, 15)+(68, 196, 39), 15, (221, 12, 8), 10).draw()
    im.show()