FROM python:3.7.15

RUN apt-get update && apt-get -y install vim curl python3-opencv

WORKDIR /home/app
COPY . /home/app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash"]

