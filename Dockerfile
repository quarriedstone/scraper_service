FROM python:3.7-slim

COPY requirements.txt /
RUN pip install -Ur requirements.txt

RUN mkdir /airbnb-scraper
RUN mkdir /amazon-scraper-master

COPY airbnb-scraper /airbnb-scraper
COPY amazon-scraper-master /amazon-scraper-master

WORKDIR /
COPY run.py .

EXPOSE 6379
CMD ["python", "run.py"]