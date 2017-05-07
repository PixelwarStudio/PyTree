# PyTree
**PyTree** is a python package, which you can use to generate trees, realistic or fractal one.
However the whole pricipale is based on fractals.
## Requirements
Python 2.x or 3.x
Pip
Pillow
## Installation
### Using Pip
1. Open Terminal
2. Type ```pip3 install Tree```
## Quick Example
```python
from math import radians
from PIL import Image
from Tree.Core import RealTree
from Tree.Draw import TreeDrawer

if __name__ == "__main__":
    # Create a Sierpinski Tree
    my_tree = RealTree(0, 0, 200, 0.7, 2, radians(30), radians(0), 0.2, 0.2)

    # Let the tree grow
    for i in range(12):
        my_tree.grow()

    # Move the tree in the right position, so that the tree is completly in the image
    rec = my_tree.get_rectangle()
    my_tree.move(-rec[0], -rec[1])

    # Create a image with the dimensions of the tree
    im = Image.new("RGB", my_tree.get_size())

    # Draw the tree on the image
    TreeDrawer(my_tree, im, (203, 40, 12)+(23, 90, 123), 10).draw()

    # Show the tree
    im.show()
```
## License
See [License](https://github.com/PixelwarStudio/PyFractalTree/blob/master/LICENSE)
