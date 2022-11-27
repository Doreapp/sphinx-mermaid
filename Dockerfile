FROM debian:bullseye-slim

# Global configuration
RUN mkdir /work/ /work/venv \
 && apt-get update \
 && apt-get install --no-install-recommends -y \
 python3 \
 python3-pip \
 python3-venv \
 make \
 && chmod 777 /work/
WORKDIR /work/

# Python configuration
ENV PYTHONDONTWRITEBYTECODE=1
ENV VIRTUAL_ENV=/work/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ADD requirements.txt requirements-dev.txt /work/
RUN python3 -m venv $VIRTUAL_ENV \
 && pip install -r requirements.txt -r requirements-dev.txt

ENV C_FORCE_ROOT=1

# Other project-specific files
ADD Makefile \
 setup.py \
 README.md \
 /work/
COPY sphinxmermaid/ /work/sphinxmermaid/

ENTRYPOINT [ "make" ]
CMD ["help"]
