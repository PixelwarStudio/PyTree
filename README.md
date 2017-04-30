# PyFractalTree
**FractalTree** is a python package, which you can use to generate fractal trees, for example a binary tree or dragon tree. The package itself only provides the low-level stuff, so tasks like drawing the tree/s aren't supported.
## Installation
The installation requires Python 3.5+ (other versions may work) and pip.
### Using Pip
1. Open Terminal
2. Type ```pip3 install FractalTree```
## Quick Example
```
from math import radians
from FractalTree import Tree

# Creates a Sierpisnkitree
my_tree = Tree(300, 400, 100, 0.5, 3, radians(120), radians(0))
# The tree "grows"
for i in range(10):
    my_tree.grow()

# Print out the nodes for every age
for age in my_tree.nodes:
    for node in age:
        print(node.x, node.y)
```
## License
See [License](https://github.com/PixelwarStudio/PyFractalTree/blob/master/LICENSE)
