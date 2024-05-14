FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y apache2 
RUN apt install -y php 
RUN apt install -y libapache2-mod-php
RUN rm /var/www/html/index.html
COPY ./index.php /var/www/html/index.php

EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
#ENTRYPOINT ["apache2ctl", "-D", "FOREGROUND"]

