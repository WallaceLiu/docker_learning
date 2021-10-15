FROM python:3.8-slim

RUN mkdir -p /app/
COPY . /app/
WORKDIR /app
RUN python -m pip install -r requirements.txt
ENV PATH /usr/bin/python:$PATH
EXPOSE 8888
CMD ['/bin/bash','run.sh']
start_component.sh