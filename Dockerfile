FROM python:3.9

WORKDIR /

RUN pip3 install luigi sqlalchemy

EXPOSE 8082/tcp

COPY ./luigi.cfg luigi.cfg
RUN mkdir -p /usr/local/var
RUN touch /usr/local/var/luigi-task-hist.db 

CMD "/bin/bash"
