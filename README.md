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

### Config Options

`sphinxmermaid_mermaid_init` can be set as a dictionary of values.

These will be passed to `mermaid.initialize()`. Find more info at
[MermaidJS](https://mermaid.js.org/intro/n00b-syntaxReference.html)

Example:

```python
sphinxmermaid_mermaid_init = {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#BB2528',
    'primaryTextColor': '#fff',
    'primaryBorderColor': '#7C0000',
    'lineColor': '#F8B229',
    'secondaryColor': '#006100',
    'tertiaryColor': '#fff'
  }
}
```

## Usage

In your `rst` (or `md`) files, use the directive just like:

```rst
.. mermaid ::

    graph TD
    A --> B
    B -- Label --> C
```
