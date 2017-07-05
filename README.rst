PyTree
======
.. image:: https://img.shields.io/pypi/v/tree.svg?style=flat-square
        :target: https://pypi.python.org/pypi/Tree

.. image:: https://img.shields.io/pypi/l/Tree.svg?style=flat-square
        :target: https://github.com/PixelwarStudio/PyTree/blob/master/LICENSE

Python package, which you can use to generate and drawing trees, realistic or fractal ones.

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

Examples
--------
See Examples_.

.. _Examples: https://github.com/PixelwarStudio/PyTree/tree/master/examples

Documentation
-------------
The documentation is hosted on Readthedocs_.

.. _Readthedocs: http://pytree.readthedocs.io/en/latest/ 