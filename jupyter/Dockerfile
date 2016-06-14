FROM jupyter/pyspark-notebook

USER root

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends python-pip python-dev libmysqlclient-dev mysql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install ipython-sql pymysql

VOLUME /notebooks
WORKDIR /notebooks
