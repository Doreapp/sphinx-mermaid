# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

DOCKER_IMAGE=sphinx

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

$(SOURCEDIR)/examples.rst: ## Generates the examples.rst file from https://github.com/mermaid-js/mermaid repo
	python3 build_examples.py $(SOURCEDIR)/examples.rst

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile $(SOURCEDIR)/examples.rst
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docker_html:
	mkdir -p build build/html build/doctrees
	docker build -t $(DOCKER_IMAGE) .
	docker run --rm \
		-u $(shell id -u):$(shell id -g) \
		-v $(shell pwd)/$(SOURCEDIR):/work/$(SOURCEDIR) \
		-v $(shell pwd)/$(BUILDDIR):/work/$(BUILDDIR) \
		-t $(DOCKER_IMAGE) \
		html
