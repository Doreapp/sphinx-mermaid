# Mermaid support for Sphinx documentation

Mermaid graph support for sphinx generated documentations

## Install

```bash
pip install sphinxmermaid
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
    A --> B : label
    B --> C
```
