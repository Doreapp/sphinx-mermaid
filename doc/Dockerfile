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
ADD requirements.txt /work/
RUN python3 -m venv $VIRTUAL_ENV \
 && pip install --upgrade -r requirements.txt

ENV C_FORCE_ROOT=1

# Other project-specific files
ADD Makefile \
 build_examples.py \
 /work/

ENTRYPOINT [ "make" ]
CMD ["html"]
