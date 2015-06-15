# HTTP echo service

# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Emiliano Molina <emiliano.g.molina@gmail.com>

# Labels
LABEL name=echo_service version=1.0.0

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libcurl4-openssl-dev \
    libev4 libev-dev python \
    python-dev \
    python-distribute \
    python-pip

# Deploy application
RUN mkdir /var/log/echo_service/
COPY ./ /tmp/echo_service/
WORKDIR /tmp/echo_service
RUN python setup.py sdist \
    && pip install dist/echo_service-1.0.0.tar.gz \
    && rm -rf /tmp/echo_service/

# Expose port
EXPOSE 8080

# Run app
ENTRYPOINT ["echo_service"]
CMD ["--port", "8080"]
