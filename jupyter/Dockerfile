FROM jupyter/pyspark-notebook

USER root

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends python-pip python-dev libmysqlclient-dev mysql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install ipython-sql pymysql

RUN apt-get update
RUN apt-get install -y pkg-config libzmq-dev build-essential

RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.5.linux-amd64.tar.gz
ENV PATH /usr/local/go/bin:$PATH
ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

RUN go get golang.org/x/tools/cmd/goimports
RUN go get github.com/gophergala2016/gophernotes
RUN mkdir -p /opt/conda/share/jupyter/kernels/gophernotes
RUN cp -r $GOPATH/src/github.com/gophergala2016/gophernotes/kernel/* /opt/conda/share/jupyter/kernels/gophernotes

VOLUME /notebooks
WORKDIR /notebooks
