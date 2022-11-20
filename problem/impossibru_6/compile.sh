#!/bin/sh

docker build --build-arg 'binary=faile' -t 'faile' .
docker run -p 30003:5000 -itd faile