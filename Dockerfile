FROM python:3.8-slim

RUN pip install --no-cache notebook

### create user with a home directory
ARG NB_USER=nbuser
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

WORKDIR ${HOME}

COPY . ${HOME}