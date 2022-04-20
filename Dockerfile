FROM python:3.9

WORKDIR /

RUN pip3 install luigi==3.0.3 sqlalchemy==1.3.16

ENV LUIGID_DATA_FOLDER=/usr/local/var
ENV LUIGID_STATE_PATH=${LUIGID_DATA_FOLDER}/luigi-state.pickle
ENV LUIGID_SQLITE_DB_FILE=${LUIGID_DATA_FOLDER}/luigi-task-hist.db
ENV LUIGID_SQLITE_DB_ADDRESS=sqlite:///${LUIGID_SQLITE_DB_FILE}

RUN mkdir -p $LUIGID_DATA_FOLDER
RUN python -c "import os, sqlite3; sqlite3.connect(os.getenv('LUIGID_SQLITE_DB_FILE'))"

COPY ./luigi.cfg luigi.cfg

CMD "/bin/bash"
