# PyFractalTree
**FractalTree** is a python package, which you can use to generate fractal trees, for example a binary tree or dragon tree. The package itself only provides the low-level stuff, so tasks like drawing the tree/s aren't supported.
## Installation
### Using Pip
1. Open Terminal
2. Type ```pip3 install FractalTree```
## Quick Example
```python
from math import radians
from PIL import Image, ImageDraw
from FractalTree import Tree

# Define dimensions of the pic
WIDTH = 600
HEIGHT = 500

# Create a PIL Image
im = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)

# Create a Sierpinski Tree
my_tree = Tree(WIDTH / 2, HEIGHT, 100, 0.5, 3, radians(120), radians(0))

# Let the tree grow 
for i in range(10):
    my_tree.grow()

# Draw the tree
for age in my_tree.get_branches():
    for branch in age:
        draw.line(branch)

# Give out the image
im.show()
```
## License
See [License](https://github.com/PixelwarStudio/PyFractalTree/blob/master/LICENSE)
