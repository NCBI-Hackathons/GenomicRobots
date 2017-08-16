# Set the base image to Ubuntu
FROM ubuntu:16.04

LABEL description="Base image for Genomic Robots Hackathon"

# File Author / Maintainer
MAINTAINER Alexander Goncearenco <alexander.goncearenco@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Setup packages
USER root

RUN apt-get -y -m update && apt-get -y upgrade
RUN apt-get -y install wget unzip zip bzip2 curl ca-certificates \
    libgsl-dev libgsl2 \
    build-essential \
    git \
    libcurl4-openssl-dev

RUN apt-get -y clean
RUN apt-get -y autoclean

# switch back to the ubuntu user so this tool (and the files written) are not owned by root
RUN groupadd -r -g 1000 ubuntu && useradd -m -r -g ubuntu -u 1000 ubuntu
RUN mkdir -p /home/ubuntu
RUN chown ubuntu:ubuntu -R /home/ubuntu

# Add Tini
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

USER ubuntu
WORKDIR /home/ubuntu

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /home/ubuntu/anaconda
RUN rm ~/miniconda.sh

ENV PATH=$PATH:/home/ubuntu/anaconda/bin

RUN conda config --add channels r
RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge
RUN conda config --add channels defaults

RUN conda update conda
RUN conda upgrade conda

# RUN pip install cwltool
# pip install cwlref-run

RUN conda clean -a

CMD ["/bin/bash"]

