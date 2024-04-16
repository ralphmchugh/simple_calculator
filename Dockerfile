#FROM python:3.13-alpine

FROM python:3.12.3-slim-bookworm

ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD=https://install.python-poetry.org
ARG PROJECT_URL=https://github.com/ralphmchugh/simple_calculator.git
ENV PATH="$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests curl git bash gcc \
  && ln -sf /bin/bash /bin/sh \ 
  && curl -sSL ${POETRY_DOWNLOAD} | python3 - --version ${POETRY_VERSION}

#RUN apk update \ 
#  && apk upgrade \ 
#  && apk add --no-cache bash curl git \
#  && ln -sf /bin/bash /bin/sh  
#&& curl -sSL ${POETRY_DOWNLOAD} | python3 - --version ${POETRY_VERSION}

WORKDIR /tmp/
RUN git clone ${PROJECT_URL}
WORKDIR  /tmp/simple_calculator

RUN poetry install

ENTRYPOINT ["poetry" , "run" , "pytest" , "tests"]









