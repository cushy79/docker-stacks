FROM centos

RUN yum install -y epel-release
RUN yum install -y ansible vim

ADD . /work
WORKDIR /work
#ENTRYPOINT ["ansible-playbook"]
