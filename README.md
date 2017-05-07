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
from Tree.Core import RealTree
from Tree.Draw import TreeImage

if __name__ == "__main__":
    # Create a Sierpinski Tree
    my_tree = RealTree(400, 300, 200, 0.7, 2, radians(30), radians(0), 0.2, 0.2)

    # Let the tree grow
    for i in range(12):
        my_tree.grow()

    tree_image = TreeImage(my_tree, None, (255, 255, 255)+(122, 123, 0), 8)
    im = tree_image.draw()
    im.show()
```
## License
See [License](https://github.com/PixelwarStudio/PyFractalTree/blob/master/LICENSE)
