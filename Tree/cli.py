from math import radians

import click

from PIL import Image
import svgwrite

from Tree.core import Tree

def get_format(path):
    pos = path.find(".")

    if pos == -1:
        return False
    return path[pos+1:]

@click.command()
@click.option("--length", "-l", type=float, default=300)
@click.option("--branches", "-b", multiple=True, type=(float, int), default=())
@click.option("--sigma", "-s", nargs=2, type=float, default=(0, 0))
@click.option("--age", "-a", type=int, default=5)
@click.option("--path", "-p", default="tree.png")
@click.option("--show", is_flag=True)
@click.option("--color1", "-c1", nargs=3, type=int, default=(255, 0, 255))
@click.option("--color2", "-c2", nargs=3, type=int, default=(255, 255, 255))
@click.option("--thickness", "-t", type=int, default=5)
def create_tree(length, branches, sigma, age, path, show, color1, color2, thickness):
    #Convert angles to radians
    branches = [[branch[0], radians(branch[1])] for branch in branches]
    click.echo(show)
    tree = Tree((0, 0, 0, -length), branches, sigma)
    tree.grow(times=age)
    tree.move_in_rectangle()

    form = get_format(path)

    if form:
        if form == "svg":
            svg = svgwrite.Drawing(path)
            tree.draw_on(svg, color1+color2, thickness)
            svg.save()
        elif form != "svg" or show:
            im = Image.new("RGB", tree.get_size())
            tree.draw_on(im, color1+color2, thickness)
            if get_format(path) != "svg":
                im.save(path)

            if show:
                im.show()
    else:
        click.echo("Warning: Invalid path")

if __name__ == "__main__":
    create_tree()