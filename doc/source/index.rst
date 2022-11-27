Mermaid in sphinx documentation
===============================

`Mermaid graphs <https://mermaid-js.github.io/mermaid/#/>`_ support for
`sphinx generated documentations <https://www.sphinx-doc.org/en/master/>`_.

- `GitHub repository at Doreapp/sphinx-mermaid <https://github.com/Doreapp/sphinx-mermaid/>`_
- `Pypi package sphinx-mermaid <https://pypi.org/project/sphinx-mermaid/>`_
- Example of usage: `GitHub pages of this repo <https://doreapp.github.io/sphinx-mermaid/>`_

.. toctree ::
   :maxdepth: 1

   examples


Quick example
-------------

.. code::

   .. mermaid::

      graph TD
      A --> B
      B -- With a label --> C

.. mermaid::

   graph TD
   A --> B
   B -- With a label --> C
