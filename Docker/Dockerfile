FROM ubuntu:16.04
FROM johanneskoester/snakemake

# adding label to the docker
LABEL SNPBOTS.version="0.0.1-alpha"
LABEL description="SNPBOTs to find presence of the users query snp\
in the host dataset."


RUN apt-get update && apt-get -y upgrade && apt-get -y install cron python python3
RUN apt-get install -y python3-pip
RUN apt-get -y install r-base
RUN apt-get -y install libcurl4-gnutls-dev
RUN apt-get -y install libssl-dev


# get the latest verison of magicblast 
#wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST//ncbi-magicblast-1.2.0-x64-linux.tar.gz
#tar zxvf ncbi-magicblast-1.2.0-x64-linux.tar.gz
#cp ncbi-magicblast-1.2.0/bin/magicblast ~/bin/
#cp ncbi-magicblast-1.2.0/bin/makeblastdb ~/bin/


# Run the command upon initiating conatiner
#CMD python integritycheck.py # to check there are no modifications in docker image
#CMD python botchecker1.py # to check if there are any additions to docker image
#CMD python botchecker2.py # to run the original bot and process the query

 
