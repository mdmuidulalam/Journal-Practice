FROM badouralix/python-scrapy
MAINTAINER  Md. Muidul Alam <2hin2222@gmail.com>

WORKDIR /crawler

RUN apt-get update && \
	apt-get install -y \
		vim \
        tmux \
        bpython3 && \
	apt-get clean && \
	rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME /crawler
