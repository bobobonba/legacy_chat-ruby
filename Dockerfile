FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y tzdata \
    ruby-full \
    apache2

RUN chmod 755 -R /var/www/html
RUN a2enmod cgid
COPY conf/* /etc/apache2/conf-available
RUN a2enconf cgi-enabled

# 環境変数を与えてapacheを起動するシェルスクリプト
COPY run_httpd.sh /usr/local/sbin
RUN chmod +x /usr/local/sbin/run_httpd.sh

# https://github.com/docker-library/httpd/blob/master/2.4/Dockerfile を参考にした
RUN sed -ri \
		-e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
		-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
		-e 's!^(\s*TransferLog)\s+\S+!\1 /proc/self/fd/1!g' \
    /etc/apache2/apache2.conf \
    /etc/apache2/envvars \
    /etc/apache2/sites-available/000-default.conf \
    /etc/apache2/sites-available/default-ssl.conf \
    /etc/apache2/conf-available/other-vhosts-access-log.conf

EXPOSE 80

CMD [ "/usr/local/sbin/run_httpd.sh" ]
