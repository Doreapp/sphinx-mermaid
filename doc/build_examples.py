"""
Script to build `examples.rst` file from
https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/examples.md
"""

import argparse
import logging
from urllib import request

LOGGER = logging.getLogger("build_examples")

EXAMPLES_URL = "https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/examples.md"
EXAMPLES_RAW_URL = "https://raw.githubusercontent.com/mermaid-js/mermaid/develop/packages/mermaid/src/docs/syntax/examples.md"


def get_example_raw() -> str:
    """
    Get the raw examples file from mermaid repo
    """
    LOGGER.debug("Fetching examples at %s", EXAMPLES_RAW_URL)
    with request.urlopen(EXAMPLES_RAW_URL) as response:
        result = response.read()
    return result.decode()

def examples() -> str:
    """
    From mermaid repo, fetch examples and build code blocks
    """
    raw = get_example_raw()
    raw_blocks = []
    current_block = None
    for line in raw.splitlines():
        if current_block is not None:
            if line.lstrip().startswith("```"):
                # Add the code block
                raw_blocks.append(current_block)
                current_block = None
            else:
                # Append the line
                current_block += line + "\n"
        elif line.lstrip().startswith("```mermaid-example"):
            current_block = "" # Open the current block write
        # Else: skip
    LOGGER.debug("Parsed %d code blocks", len(raw_blocks))
    return raw_blocks

def rst_examples() -> str:
    """
    Build rst content from mermaid repo
    """
    code_blocks = examples()
    LOGGER.debug("Building RST code")
    result = "Examples\n"
    result += "========\n\n"
    result += "Example of usage of mermaid library fetched from the "
    result += f"`offical repository <{EXAMPLES_URL}>`_.\n\n"
    for block in code_blocks:
        mermaid_block = ""
        for line in block.splitlines():
            mermaid_block += "\t" + line.strip() + "\n"
        result += ".. code-block:: rst\n\n"
        result += "\t .. mermaid::\n\n"
        result += "\n".join("\t" + line for line in mermaid_block.splitlines()) + "\n\n"
        result += ".. mermaid::\n\n"
        result += mermaid_block + "\n\n\n"
    return result

def save_file(filename: str, content: str):
    """Save a text content into a file"""
    LOGGER.debug("Writing %d characters into %s", len(content), filename)
    with open(filename, "w", encoding="utf8") as fos:
        fos.write(content)

def parse_args() -> argparse.Namespace:
    """
    Parse CLI arguments
    """
    parser = argparse.ArgumentParser("build_examples.py")
    parser.add_argument("output", type=str, default="examples.rst", help="Output file")
    parser.add_argument(
        "-l",
        "--level",
        "--log-level",
        type=str,
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
        default="INFO",
        help="Log level"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    logging.basicConfig(level=args.level)
    LOGGER.info("Using log level '%s'", args.level)
    save_file(args.output, rst_examples())

if __name__ == "__main__":
    main()