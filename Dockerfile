FROM debian:bullseye-slim

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

COPY . /app
# WORKDIR /app 

RUN pip3 install -r requirements.txt

CMD ["python3","assesmnent.py"]
