FROM ubuntu:xenial

RUN apt-get -y update \
 && apt-get -y install chromium-browser fonts-ipafont-gothic fonts-ipafont-mincho \
 && apt-get -y install build-essential unzip libgconf2-4 wget python3-pip \
 && pip3 install slackweb selenium

RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip \
 && unzip chromedriver_linux64.zip \
 && mv chromedriver /usr/bin/

COPY cost.py /usr/local/

CMD ["python3", "/usr/local/cost.py"]
