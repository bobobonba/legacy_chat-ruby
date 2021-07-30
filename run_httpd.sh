#!/bin/sh

export APACHE_RUN_USER="www-data"
export APACHE_RUN_GROUP="www-data"
export APACHE_RUN_DIR="/var/run/apache2"
mkdir -p "${APACHE_RUN_DIR}"

exec /usr/sbin/apache2 -DFOREGROUND
