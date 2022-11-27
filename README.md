# Mermaid support for Sphinx documentation

[Mermaid graphs](https://mermaid-js.github.io/mermaid/#/) support for [sphinx generated documentations](https://www.sphinx-doc.org/en/master/).

- [GitHub repository at Doreapp/sphinx-mermaid](https://github.com/Doreapp/sphinx-mermaid/)
- [Pypi package sphinx-mermaid](https://pypi.org/project/sphinx-mermaid/)
- Example of usage: [GitHub pages of this repo](https://doreapp.github.io/sphinx-mermaid/)

## Install

```bash
pip install sphinx-mermaid
```

## Setup in `conf.py`

In the `conf.py` file of your documentation, add the extension:

```python
extensions = [
    ...,
    'sphinxmermaid'
]
```

## Usage

In your `rst` (or `md`) files, use the directive just like:

```rst
.. mermaid ::

    graph TD
    A --> B
    B -- Label --> C
```
