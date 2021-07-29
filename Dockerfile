FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y tzdata \
    ruby-full \
    apache2

RUN a2enmod cgid
COPY conf/* /etc/apache2/conf-available
RUN a2enconf cgi-enabled

EXPOSE 80