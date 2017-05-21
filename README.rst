PyTree
======
Python package, which you can use to generate and drawing trees, realistic or fractal ones.

.. image:: https://img.shields.io/pypi/v/nine.svg?style=flat-square   :target: [![PyPI](https://img.shields.io/pypi/v/nine.svg?style=flat-square)](https://pypi.python.org/pypi/Tree/0.1b8)
.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square   :target: https://github.com/PixelwarStudio/PyTree

Usage
-----
.. code-block:: bash
    $ pip install Tree

.. code-block:: python
    from math import radians
    from PIL import Image
    from Tree.core import Tree
    from Tree.draw import PillowDrawer

    if __name__ == "__main__":
        # Create a Tree
        my_tree = Tree(
            pos = (0, 0, 0, -200),
            scale = 0.7,
            complexity = 2,
            angle = (radians(30), 0),
            sigma = (0.2, 5/180)
        )
        my_tree.grow(times=12)

        # Move the tree in the right position, so that the tree is completly in the image
        rec = my_tree.get_rectangle()
        my_tree.move((-rec[0], -rec[1]))

        # Create a image with the dimensions of the tree
        im = Image.new("RGB", my_tree.get_size())

        # Draw the tree on the image
        PillowDrawer(my_tree, im, (203, 40, 12)+(23, 90, 123), 10).draw()

        # Show the tree
        im.show()

Documentation
-------------
The documentation is hosted on Readthedocs_.

.. _Readthedocs: http://pytree.readthedocs.io/en/latest/ 