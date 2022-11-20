#!/bin/sh

docker build --build-arg 'binary=bash_3.py' -t 'bash_3' .
docker run -p 30003:5000 -itd bash_3