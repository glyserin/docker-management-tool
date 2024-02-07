FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu
ARG DEBIAN_FRONTEND=noninteractive
COPY requirements.txt /app/
RUN apt update \
    && apt -y install git python3 python3-pip \
              python-is-python3\
    && pip3 install -r /app/requirements.txt
