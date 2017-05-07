from PIL import Image, ImageDraw

class TreeImage(object):
    def __init__(self, tree, size=None, color=(255, 255, 255), thickness=1):
        self.tree = tree
        self.color = color
        self.thickness = thickness

        self.rec = tree.get_rectangle()

        if size is None:
            self.size = (int(self.rec[2]-self.rec[0]), int(self.rec[3]-self.rec[1]))
        else:
            self.size = size

        self.im = Image.new("RGB", self.size)

    def get_thickness(self, age):
        return int((self.thickness*5)/(age+5))

    def get_color(self, age):
        color = self.color
        tree = self.tree
        if len(color) == 3:
            return color
        else:
            diff = (color[3]-color[0], color[4]-color[1], color[5]-color[2])
            per_age = (diff[0]/tree.age, diff[1]/tree.age, diff[2]/tree.age)
            return (int(color[0]+per_age[0]*age),
                    int(color[1]+per_age[1]*age),
                    int(color[2]+per_age[2]*age))

    def draw_branch(self, branch, color, thickness):
        ImageDraw.Draw(self.im).line(branch, color, thickness)

    def draw(self):
        tree = self.tree
        tree.move(-self.rec[0], -self.rec[1])
        for a, age in enumerate(tree.get_branches()):
            thickness = self.get_thickness(a)
            color = self.get_color(a)
            for branch in age:
                self.draw_branch(branch, color, thickness)
        tree.move(self.rec[0], self.rec[1])
        return self.im
