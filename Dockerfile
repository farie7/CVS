FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y  libpq-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
RUN python3 init_db.py --i R

ENTRYPOINT ["python3"]

CMD [ "app.py" ]
