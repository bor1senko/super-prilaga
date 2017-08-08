FROM ubuntu:16.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y  git  python-pip python-dev


ADD ./app/requirements.txt .
RUN pip install -r requirements.txt

CMD ["/bin/bash"]
