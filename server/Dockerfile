FROM python:3.6-alpine

RUN apk update
RUN apk add python3

#COPY . /app
#WORKDIR /app
#
#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
#CMD ["app.py"]
