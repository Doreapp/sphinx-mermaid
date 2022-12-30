"""
Main file of the sphinx extension
"""

import json
from typing import TYPE_CHECKING, List

import sphinx
from docutils import nodes
from sphinx.locale import _
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

LOGGER = logging.getLogger(__name__)
MERMAID_JS_URL = "https://unpkg.com/mermaid/dist/mermaid.min.js"
DEFAULT_MERMAID_INIT = "mermaid.initialize({startOnLoad:true});"

if TYPE_CHECKING:
    from docutils.nodes import Node
    from sphinx.application import Sphinx
    from sphinx.util.docutils import SphinxTranslator


class MermaidNode(nodes.General, nodes.Inline, nodes.Element):
    """Mermaid node"""


class Mermaid(SphinxDirective):
    """
    ``.. mermaid ::`` directive. Able of drawing mermaid graph from code
    """

    has_content: bool = True

    def code_content(self) -> str:
        """Build and return mermaid code from content"""
        code = "\n".join(self.content)
        if len(code.strip()) == 0:
            raise self.error("Empty content")
        return code

    def run(self) -> List["Node"]:
        """Visit the directrive"""
        node = MermaidNode()
        node["code"] = self.code_content()
        return [node]


def append_mermaid_div(self: "SphinxTranslator", code: str):
    """
    Append a mermaid div to the HTML body of `self`
    """
    div = '<div class="mermaid" align="center">\n' + code + "\n</div>"
    self.body.append(div)


def html_mermaid(self: "SphinxTranslator", node: "Node"):
    """
    Visit handler for HTML
    """
    LOGGER.debug("HTML visit mermaid node at %s", node.line)
    append_mermaid_div(self, node["code"])
    raise nodes.SkipNode


def install_js(app: "Sphinx", *_):
    """
    Install the Javascript code needed for mermaid.
    """
    LOGGER.debug("Installing mermaid JavaScript from %s", MERMAID_JS_URL)
    app.add_js_file(MERMAID_JS_URL, priority=500)

    mermaid_init = create_mermaid_init(app)
    app.add_js_file(None, body=mermaid_init, priority=501)


def create_mermaid_init(app):
    """
    Returns the `mermaid.initialize({...})` code string from the value
    specified in conf.py or the default value.
    """

    mermaid_init = app.config.mermaid_init

    if mermaid_init:
        check_mermaid_init(mermaid_init)

        params = json.dumps(mermaid_init)
        return f"mermaid.initialize({params})"

    return DEFAULT_MERMAID_INIT


def check_mermaid_init(mermaid_init):
    """
    Checks whether `mermaid_init` is valid. If not, raises an error.
    """

    if not isinstance(mermaid_init, dict):
        raise TypeError("mermaid_init must be a dict.")


def setup(app: "Sphinx"):
    """
    Setup the extension
    """
    app.add_config_value("mermaid_init", None, "html")
    app.add_node(MermaidNode, html=(html_mermaid, None))
    app.add_directive("mermaid", Mermaid)
    app.connect("html-page-context", install_js)
    return {
        "version": sphinx.__display_version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
