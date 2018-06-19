FROM ubuntu:16.04

MAINTAINER Muhammad Omar "Muhammad.Omar.EG@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:george-edison55/cmake-3.x -y
RUN apt-get update -y
RUN apt-get install cmake -y
copy . /
VOLUME [ "/Core" ] 
WORKDIR /
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora -y
ENTRYPOINT ["python"]
CMD ["app.py"]
